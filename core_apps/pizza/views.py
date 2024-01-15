from rest_framework import viewsets
from .models import PizzaBase, Cheese, Topping, Pizza, Order
from .serializers import (
    PizzaBaseSerializer,
    CheeseSerializer,
    ToppingSerializer,
    PizzaSerializer,
    OrderSerializer,
)


class PizzaBaseViewSet(viewsets.ModelViewSet):
    queryset = PizzaBase.objects.all()
    serializer_class = PizzaBaseSerializer


# Similar viewsets for Cheese, Topping, Pizza, and Order
class CheeseViewSet(viewsets.ModelViewSet):
    queryset = Cheese.objects.all()
    serializer_class = CheeseSerializer


class ToppingBaseViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
