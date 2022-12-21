from django.db import models
from users.models import User

# Create your models here.
class Services(models.Model):
    MY_CHOICES = (
        (1, 'Netflix'),
        (2, 'Amazon Video'),
        (3, 'Star +'),
        (4, 'Paramount +'),
    )
    servicio = models.CharField(max_length=1, choices=MY_CHOICES)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.FloatField(default=0.0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")