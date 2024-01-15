from rest_framework import serializers
from .models import PizzaBase, Cheese, Topping, Pizza, Order


class PizzaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaBase
        fields = "__all__"


class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = "__all__"


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = "__all__"


class PizzaSerializer(serializers.ModelSerializer):
    base = PizzaBaseSerializer()
    cheese = CheeseSerializer()
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = Pizza
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
