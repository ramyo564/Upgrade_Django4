from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from .models import Account, UserProfile


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
            "password",
            "phone_number",
        )


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ModelSerializer

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    phone_number = PhoneNumberField(region="KR", max_length=13)

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password does not match.")
        return data


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class EmailVerificationSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
