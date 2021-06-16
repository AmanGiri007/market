from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'product_rate')
