from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import Account, UserProfile
from carts.models import Cart, CartItem


class RegisterViewTest(TestCase):
    def test_register_view_success(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "testpassword",
            "confirm_password": "testpassword",
            "phone_number": "010-1234-5678",
        }

        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 302)  # 리다이렉트 예상

        # 사용자가 생성되었는지 확인
        user = Account.objects.get(email=data["email"])
        self.assertIsNotNone(user)

        # 사용자 프로필이 생성되었는지 확인
        profile = UserProfile.objects.get(user=user)
        self.assertIsNotNone(profile)

    def test_register_view_invalid_data(self):
        # 유효하지 않은 POST 데이터 생성
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "testpassword",
            "confirm_password": "testpassword",
            "phone_number": "",
        }

        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 200)  # 폼이 다시 보여져야 함

    def test_register_view_get(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)  # 폼 보여주기를 기대

        # 반환된 응답에서 폼이 제대로 보여지는지 확인
        self.assertContains(response, "<form")
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="password"')


class LoginViewTest(TestCase):
    def setUp(self):
        # 사용할 테스트 유저 생성
        self.user = Account.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
            first_name="John",
            last_name="Doe",
        )

    def test_login_valid_credentials(self):
        client = Client()
        response = client.post(
            reverse("login"), {"email": "test@example.com", "password": "testpassword"}
        )
        print(111111111111111111111111111111111111111)
        print(f"sss : {response.url}")
        self.assertEqual(response.status_code, 302)  # 리다이렉트 예상
        
        
        self.assertTrue(response.url.endswith("dashboard"))  # 로그인 성공 후 대시보드로 리다이렉트됨을 예상

    def test_login_invalid_credentials(self):
        client = Client()
        response = client.post(
            reverse("login"), {"email": "test@example.com", "password": "wrongpassword"}
        )

        self.assertEqual(response.status_code, 302)  # 리다이렉트 예상
        self.assertTrue(
            response.url.endswith("login")
        )  # 로그인 실패 후 다시 로그인 페이지로 리다이렉트됨을 예상
