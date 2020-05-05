from rest_framework import serializers
from bedu_travels.models import Producto

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields = ("id","descripcion","precio","iva",)