from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.models.event_models import Event
from events.serializers.event_serializers import EventSerializer

class EventListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_class = JWTAuthentication()

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.user.role != "organizer":
            return Response({"error": "Only event organizers can create events."}, status=403)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organizer=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EventDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response({"error": "Event not found."}, status=404)

    def delete(self, request, pk, *args, **kwargs):
        try:
            event = Event.objects.get(pk=pk)
            if request.user.role not in ["admin", "organizer"] or event.organizer != request.user:
                return Response({"error": "You do not have permission to delete this event."}, status=403)
            event.delete()
            return Response({"message": "Event deleted successfully."}, status=204)
        except Event.DoesNotExist:
            return Response({"error": "Event not found."}, status=404)
