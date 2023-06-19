from django.urls import path

from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("category/<str:category_slug>/", views.store, name="products_by_category"),
    path(
        "category/<str:category_slug>/<str:product_slug>/",
        views.product_detail,
        name="product_detail",
    ),
    # path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    # path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path("search/", views.search, name="search"),
    path("submit_review/<int:product_id>/", views.submit_review, name="submit_review"),
    path("update_results/", views.update_results, name="update_results"),
]
