from django import urls
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ProductViewset
router = routers.DefaultRouter()
router.register(r"product_api", ProductViewset)
urlpatterns = [
    path('', views.ProductView.as_view(), name="products"),
    path('<int:products_id>/', views.ProductView.post, name="rate_change"),
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls'))
]
