from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

from utility.password_validate import validate_password

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(
        required=True,
    )
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Email already exists",
            )
        ],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        # error_messages={
        #     "required": "Please provide your  password.",
        #     "write_only": "This field is write-only and cannot be read.",
        #     "blank": "Password field cannot be blank.",
        # },
    )
    class Meta:
        model = User
        fields = ['id', 'first_name',"last_name", 'email', 'role', 'password']
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
