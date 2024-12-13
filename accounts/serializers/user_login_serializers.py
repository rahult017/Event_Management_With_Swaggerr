from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginSeriaizer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        error_messages={
            "required": "Please provide your email.",
            "blank": "Email field cannot be blank.",
            "invalid": "Please provide a valid email address.",
        },
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={
            "required": "Please provide your password.",
            "write_only": "This field is write-only and cannot be read.",
            "blank": "Password field cannot be blank.",
        },
    )

    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]

    def validate(self, attrs):
        try:
            user = User.objects.only("email").get(email=attrs["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError("Incorrect Email")
        except User.MultipleObjectsReturned:
            raise serializers.ValidationError("Multiple entries found")

        if not user.check_password(attrs["password"]):
            raise serializers.ValidationError("Incorrect password")

        return attrs
