import logging

import requests
from django.contrib import auth, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status, viewsets
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from carts.models import Cart, CartItem
from carts.views import _cart_id

from .helpers import get_current_host
from .models import Account, UserProfile
from .serializers import AccountSerializer, UserLoginSerializer, UserRegisterSerializer

User = get_user_model()


class AccountViewSet(viewsets.ViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(
        detail=False,
        methods=["post"],
        url_path="register",
        authentication_classes=[],
        permission_classes=[AllowAny],
    )
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get("first_name")
            last_name = serializer.validated_data.get("last_name")
            password = serializer.validated_data.get("password")
            hashed_password = make_password(password)
            email = serializer.validated_data.get("email")
            phone_number = serializer.validated_data.get("phone_number")

            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=email.split("@")[0],
                phone_number=phone_number,
            )
            user.set_password(hashed_password)
            user.save()
            UserProfile.objects.create(user=user, profile_picture="default/avatar.webp")

            # Send email verification
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            data = request.data
            host = get_current_host(request)
            link = "{host}api/account/check_verification/{uid}/{token}".format(
                host=host, uid=uid, token=token
            )
            body = (
                "Please click on the link below to confirm your registration.\n"
                "{link}".format(link=link)
            )
            send_mail(
                "Please activate your account", body, "noreply@eshop.com", [data["email"]]
            )

        return Response(
            {
                "details": "Verification email sent to: {email}".format(
                    email=data["email"]
                )
            }
        )

    @action(
        detail=False,
        methods=["post"],
        url_path=(r"check_verification/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)"),
        authentication_classes=[],
        permission_classes=[AllowAny],
    )
    def check_verification(self, request, uidb64=None, token=None):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = Account._default_manager.get(pk=uid)
            print(
                f"user : {user} , token : {default_token_generator.check_token(user, token)}"
            )
        except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response(
                {
                    "message": "Thank you! Your account is activated."
                }
            )
        else:
            return Response(
                {
                     "message": "Invalid activation link"
                }
            )


    # @action(detail=False, methods=["POST"], url_path="login")
    # def login(self, request):
    #     serializer = UserLoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         email = serializer.validated_data["email"]
    #         password = serializer.validated_data["password"]
    #         user = auth.authenticate(request, email=email, password=password)

    #     if user is not None:
    #         try:
    #             cart = Cart.objects.get(cart_id=_cart_id(request))
    #             is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
    #             if is_cart_item_exists:
    #                 cart_item = CartItem.objects.filter(cart=cart)
    #                 # Getting the product variations by cart id
    #                 product_variation = []
    #                 for item in cart_item:
    #                     variation = item.variations.all()
    #                     product_variation.append(list(variation))
    #                 # Get the cart items from the user to access his product variations
    #                 cart_item = CartItem.objects.filter(user=user)
    #                 ex_var_list = []
    #                 id = []
    #                 for item in cart_item:
    #                     existing_variation = item.variations.all()
    #                     ex_var_list.append(list(existing_variation))
    #                     id.append(item.id)
    #                 for pr in product_variation:
    #                     if pr in ex_var_list:
    #                         index = ex_var_list.index(pr)
    #                         item_id = id[index]
    #                         item = CartItem.objects.get(id=item_id)
    #                         item.quantity += 1
    #                         item.user = user
    #                         item.save()
    #                     else:
    #                         cart_item = CartItem.objects.filter(cart=cart)
    #                         for item in cart_item:
    #                             item.user = user
    #                             item.save()
    #         except Exception as e:
    #             logging.error(f"An error occurred: {e}")
    #             pass

    #         auth.login(request, user)
    #         messages.success(request, "You are now logged in.")
    #         url = request.META.get("HTTP_REFERER")
    #         try:
    #             query = requests.utils.urlparse(url).query
    #             print("query -> ", query)
    #             print("---------")
    #             # next=/cart/checkout/
    #             params = dict(x.split("=") for x in query.split("&"))
    #             print("params -> ", params)
    #             if "next" in params:
    #                 nextPage = params["next"]
    #                 return redirect(nextPage)
    #         except Exception as e:
    #             logging.error(f"An error occurred: {e}")
    #             return redirect("dashboard")
    #     else:
    #         messages.error(request, "Invalid login credentials")
    #         return Response(
    #             {"error": "Invalid login credentials."},
    #             status=status.HTTP_401_UNAUTHORIZED,
    #         )
    #     return Response(
    #         {"message": "User logged in successfully."}, status=status.HTTP_200_OK
    #     )

    # @action(detail=False, url_path="logout")
    # def logout(self, request):
    #     auth.logout(request)
    #     messages.success(request, "You are logged out")
    #     return Response(
    #         {"message": "Logged out successfully."}, status=status.HTTP_200_OK
    #     )

    # @action(
    #     detail=False,
    #     url_path=(
    #         r"activate/(?P<uidb64>[0-9A-Za-z_\\-]+)/(?P<token>[0-9A-Za-z]{1,13}-"
    #         r"[0-9A-Za-z]{1,20})/$"
    #     ),
    # )
    # def activate(self, request, uidb64, token):
    #     try:
    #         uid = urlsafe_base64_decode(uidb64).decode()
    #         user = Account._default_manager.get(pk=uid)
    #     except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
    #         user = None
    #     if user is not None and default_token_generator.check_token(user, token):
    #         user.is_active = True
    #         user.save()
    #         messages.success(request, "Thank you! Your account is activated.")
    #         return Response(
    #             {"message": "Account activated successfully."},
    #             status=status.HTTP_200_OK,
    #         )
    #     else:
    #         messages.error(request, "Invalid activation link")
    #         return Response(
    #             {"error": "Invalid activation link."},
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )


# class EmailVerificationViewSet(viewsets.ViewSet):

#     @action(
#         methods=["get"],
#         detail=False,
#     )
#     def activate_api(self, request, uidb64=None, token=None):

#         # uidb64 = request.GET.get('uidb64')
#         # token = request.GET.get('token')
#         print(f"uidb64 : {uidb64}")
#         print(f"token : {token}")
#         # try:
#         #     uid = urlsafe_base64_decode(uidb64).decode()
#         #     user = User._default_manager.get(pk=uid)
#         # except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         #     user = None

#         # if user is not None and default_token_generator.check_token(user, token):
#         #     user.is_active = True
#         #     user.save()
#         #     messages.success(request, "Thank you! Your account is activated.")
#         #     return redirect("login")  # Replace with your actual login URL
#         # else:
#         #     messages.error(request, "Invalid activation link")
#         #     return redirect("register")  # Replace with your actual registration URL
