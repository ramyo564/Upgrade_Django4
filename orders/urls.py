from django.urls import path
from . import views

urlpatterns = [
    path("place_order/", views.place_order, name="place_order"),
    path("payments/", views.payments, name="payments"),
    path("order_complete/", views.order_complete, name="order_complete"),
    # Kakao
    path("kakao_pay/", views.kakao_pay, name="kakao_pay"),
    path("kakao_pay_approval/", views.kakao_pay_approval, name="kakao_pay_approval"),
    path("kakao_pay_cancel/", views.kakao_pay_cancel, name="kakao_pay_cancel"),
]
