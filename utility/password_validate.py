import re
from rest_framework import serializers
from django.core.validators import RegexValidator

def validate_password(password):
    # Check for at least one capital letter
    if not re.search(r"[A-Z]", password):
        raise serializers.ValidationError(
            "Password must contain at least one capital letter."
        )
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()_+{}|:"<>?`~\-=[\];\',./]', password):
        raise serializers.ValidationError(
            "Password must contain at least one special character."
        )
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        raise serializers.ValidationError(
            "Password must contain at least one lowercase letter."
        )
    # Check for at least eight characters
    if len(password) < 8:
        raise serializers.ValidationError(
            "Password must be at least eight characters long."
        )
    return password

