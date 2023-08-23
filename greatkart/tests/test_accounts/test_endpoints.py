import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status

pytestmark = pytest.mark.django_db


User = get_user_model()


@pytest.fixture
def create_user():
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "testpassword",
    }
    return User.objects.create_user(**user_data)


class TestAccountEndpoints:

    def test_user_registration(self, api_client):
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "testpassword",
            "confirm_password": "testpassword",
            "phone_number": "010-1234-5678",
        }
        response = api_client().post("/api/account/register/", user_data)
        assert response.status_code == status.HTTP_200_OK

    def test_fail_user_registration(self, api_client):
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "tpassword",
            "confirm_password": "testpassword",
            "phone_number": "010-1234-5678",
        }
        response = api_client().post("/api/account/register/", user_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_login(self, create_user, api_client):

        # Valid_email_verification
        uid_encode = urlsafe_base64_encode(force_bytes(create_user.pk))
        token = default_token_generator.make_token(create_user)
        data = {
            "uidb64": uid_encode,
            "token": token,
        }
        response = api_client().post("/api/account/check_email_verification/", data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"message": "This account is activated."}

        # User Login
        login_data = {
            "email": "johndoe@example.com",
            "password": "testpassword",
        }
        response = api_client().post("/api/account/login/", login_data)
        access_token = response.data['access_token']
        api_client().credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "User logged in successfully."

    def test_fail_wrong_email_verification(self, create_user, api_client):

        # Valid_email_verification
        uid_encode = urlsafe_base64_encode(force_bytes(create_user.pk))
        data = {
            "uidb64": uid_encode,
            "token": "token",
        }
        response = api_client().post("/api/account/check_email_verification/", data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"message": "Invalid activation link"}

        # Account does not exist
        uid_encode = urlsafe_base64_encode(force_bytes(100))
        data = {
            "uidb64": uid_encode,
            "token": "token",
        }
        response = api_client().post("/api/account/check_email_verification/", data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"message": "Invalid activation link"}

    def test_fail_login(self, create_user, api_client):

        # Valid_email_verification
        uid_encode = urlsafe_base64_encode(force_bytes(create_user.pk))
        token = default_token_generator.make_token(create_user)
        data = {
            "uidb64": uid_encode,
            "token": token,
        }
        response = api_client().post("/api/account/check_email_verification/", data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"message": "This account is activated."}

        # User Login
        login_data = {
            "email": "johndoe@example.com",
            "password": "testpassword44",
        }
        response = api_client().post("/api/account/login/", login_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_logout(self, create_user, api_client):

        # Valid_email_verification
        uid_encode = urlsafe_base64_encode(force_bytes(create_user.pk))
        token = default_token_generator.make_token(create_user)
        data = {
            "uidb64": uid_encode,
            "token": token,
        }
        response = api_client().post("/api/account/check_email_verification/", data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"message": "This account is activated."}
        # 로그인
        login_data = {
            "email": "johndoe@example.com",
            "password": "testpassword",
        }
        response = api_client().post("/api/account/login/", login_data)
        assert response.status_code == status.HTTP_200_OK
        access_token = response.data['access_token']

        # 로그아웃
        headers = {'Authorization': f'Bearer {access_token}'}
        response = api_client().get("/api/account/logout/", headers=headers)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "Logged out successfully."
