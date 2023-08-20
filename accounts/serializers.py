from rest_framework import serializers
from .models import Account, UserProfile
from phonenumber_field.serializerfields import PhoneNumberField


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'username', 'password', 'phone_number')

    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user


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
    phone_number = PhoneNumberField(region="KR", max_length=13)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
