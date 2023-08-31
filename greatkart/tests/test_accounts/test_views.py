from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from accounts.models import Account, UserProfile
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
# from carts.models import Cart, CartItem


# class RegisterViewTest(TestCase):
#     def test_register_view_success(self):
#         data = {
#             "first_name": "John",
#             "last_name": "Doe",
#             "username": "johndoe",
#             "email": "johndoe@example.com",
#             "password": "testpassword",
#             "confirm_password": "testpassword",
#             "phone_number": "010-1234-5678",
#         }

#         response = self.client.post(reverse("register"), data)
#         self.assertEqual(response.status_code, 302)  # 리다이렉트 예상

#         # 사용자가 생성되었는지 확인
#         user = Account.objects.get(email=data["email"])
#         self.assertIsNotNone(user)

#         # 사용자 프로필이 생성되었는지 확인
#         profile = UserProfile.objects.get(user=user)
#         self.assertIsNotNone(profile)

#     def test_register_view_invalid_data(self):
#         # 유효하지 않은 POST 데이터 생성
#         data = {
#             "first_name": "John",
#             "last_name": "Doe",
#             "username": "johndoe",
#             "email": "johndoe@example.com",
#             "password": "testpassword",
#             "confirm_password": "testpassword",
#             "phone_number": "",
#         }

#         response = self.client.post(reverse("register"), data)
#         self.assertEqual(response.status_code, 200)  # 폼이 다시 보여져야 함

#     def test_register_view_get(self):
#         response = self.client.get(reverse("register"))
#         self.assertEqual(response.status_code, 200)  # 폼 보여주기를 기대

#         # 반환된 응답에서 폼이 제대로 보여지는지 확인
#         self.assertContains(response, "<form")
#         self.assertContains(response, 'name="email"')
#         self.assertContains(response, 'name="password"')


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

    def test_activate_valid_link(self):
        # Create a valid token
        token = default_token_generator.make_token(self.user)
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))

        # Make a request to activate link
        response = self.client.get(reverse("activate", args=[uidb64, token]))
        print(f"response : {response}")
        
        # Check if user is activated
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_active)

        # Check response status and message
        self.assertEqual(response.status_code, 302)  # 리다이렉트 예상
        self.assertTrue(response.url.endswith("login/"))  # 활성화 후 로그인 페이지로 리다이렉트

    def test_activate_invalid_link(self):
        # Make a request with invalid token
        response = self.client.get(reverse("activate", args=["invalid_uidb64", "invalid_token"]))

        # Check if user is not activated
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)

        # Check response status and message
        self.assertEqual(response.status_code, 302)  # 리다이렉트 예상
        self.assertTrue(response.url.endswith("register/"))  # 잘못된 링크로 리다이렉트







    # def test_login_valid_credentials(self):
    #     client = Client()
    #     response = client.post(
    #         reverse("login"), {"email": "test@example.com", "password": "testpassword"}
    #     )
    #     self.assertEqual(response.status_code, 302)  # 리다이렉트 예상
    #     print(f"sss : {response.url.startswith('dashboard')}")
    #     print(f"sss : {response.url}")
    #     self.assertTrue(response.url.endswith("dashboard"))  # 로그인 성공 후 대시보드로 리다이렉트됨을 예상

    # def test_login_invalid_credentials(self):
    #     client = Client()
    #     response = client.post(
    #         reverse("login"), {"email": "test@example.com", "password": "wrongpassword"}
    #     )

    #     self.assertEqual(response.status_code, 302)  # 리다이렉트 예상
    #     self.assertTrue(
    #         response.url.endswith("login")
    #     )  # 로그인 실패 후 다시 로그인 페이지로 리다이렉트됨을 예상
