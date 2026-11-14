
from django.db import models
CATEGORY_CHOICES = [
    ('Electronics', 'Electronics'),
    ('Mobiles', 'Mobiles'),
    ("Men's Fashion", "Men's Fashion"),
    ("Women's Fashion", "Women's Fashion"),
    ('Kids Fashion', 'Kids Fashion'),
    ('Footwear', 'Footwear'),
    ('Beauty & Personal Care', 'Beauty & Personal Care'),
    ('Home & Kitchen', 'Home & Kitchen'),
    ('Grocery', 'Grocery'),
    ('Watches', 'Watches'),
    ('Sports', 'Sports'),
    ('Bags', 'Bags'),
]

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='Electronics'
        )
    subcategory = models.CharField(
            max_length=100,
            blank=True
        )
        

    def __str__(self):
        return self.name
class Order(models.Model):
    payment_method = models.CharField(
    max_length=50,
    default='Cash on Delivery'
)

    payment_status = models.CharField(
    max_length=30,
    default='Pending'
)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='Electronics'
    )
    
    subcategory = models.CharField(
        max_length=100,
        blank=True
    )
    
    
    def __str__(self):
        return self.customer_name