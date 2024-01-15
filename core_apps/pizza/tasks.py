from celery import shared_task
from core_apps.pizza.models import Order, Task
from datetime import datetime, timedelta


@shared_task
def update_order_status(order_id):
    order = Order.objects.get(id=order_id)
    current_time = datetime.now()

    if (current_time - order.created_at).total_seconds() < 60:
        order.status = "Accepted"
    elif (current_time - order.created_at).total_seconds() < 180:
        order.status = "Preparing"
    elif (current_time - order.created_at).total_seconds() < 300:
        order.status = "Dispatched"
    else:
        order.status = "Delivered"

    order.save()

    task = Task(
        order=order,
        task_type="UpdateOrderStatus",
        status="Completed",
        completed_at=current_time,
    )
    task.save()
