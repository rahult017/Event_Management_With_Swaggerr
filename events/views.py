from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets, status

from events.models.event_models import Event
from events.serializers.event_serializers import EventSerializer

from utility.serializers_errors import serializer_error

class EventListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        if serializer.data:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.user.role != "ORGANIZER":
            return Response({"error": "Only event organizers can create events."}, status=status.HTTP_403_FORBIDDEN)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organizer=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer_error(serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class EventDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({"error": "Event not found."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            event = Event.objects.get(pk=pk)
            if request.user.role not in ["ADMIN", "ORGANIZER"] or event.organizer != request.user:
                return Response({"error": "You do not have permission to delete this event."}, status=status.HTTP_403_FORBIDDEN)
            event.delete()
            return Response({"message": "Event deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

class EventJoinAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if event.attendees.filter(id=request.user.id).exists():
            return Response({"detail": "You have already joined this event."}, status=status.HTTP_400_BAD_REQUEST)

        if event.available_slots() > 0:
            event.attendees.add(request.user)
            event.save()
            return Response({"detail": "Successfully joined the event."}, status=status.HTTP_200_OK)
        return Response({"detail": "No slots available."}, status=status.HTTP_400_BAD_REQUEST)
