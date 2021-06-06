from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductView.as_view(), name="products"),
    path('<int:products_id>/', views.ProductView.post, name="rate_change"),
]
