from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PizzaBaseViewSet,
    CheeseViewSet,
    ToppingViewSet,
    PizzaViewSet,
    OrderViewSet,
)

router = DefaultRouter()
router.register(r"pizza_bases", PizzaBaseViewSet)
router.register(r"cheeses", CheeseViewSet)
router.register(r"toppings", ToppingViewSet)
router.register(r"pizzas", PizzaViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
