from rest_framework.generics import ListCreateAPIView

from bedu_travels.models import Producto
from bedu_travels.serializers import ProductSerializer,RetrieveUpdateDestroyAPIView

class producto_list_view(ListCreateAPIView):
    
    queryset = Producto.objects.all()
    serializer_class= ProductSerializer
    
class ProductoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer
