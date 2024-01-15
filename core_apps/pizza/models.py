from django.db import models


class PizzaBase(models.Model):
    name = models.CharField(max_length=50)


class Cheese(models.Model):
    name = models.CharField(max_length=50)


class Topping(models.Model):
    name = models.CharField(max_length=50)


class Pizza(models.Model):
    base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Placed")
    created_at = models.DateTimeField(auto_now_add=True)
    test = models.CharField(max_length=200)


class Task(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
