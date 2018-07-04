from django.db import models
from carts.models import Cart

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),  #(value in databaase, value displayed)
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded')
)

class Order(models.Model):
    cart           = models.ForeignKey(Cart)
    status         = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    order_id       = models.CharField(max_length=120, blank=True)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total          = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    # billing_profile
    # shipping_address
    # billing_address

    def __str__(self):
        return self.order_id
