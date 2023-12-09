from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import Signal
from django.dispatch import receiver
BRAND = (
    ('Asian Paints','Asian Paints'),
    ('Berger Paints','Berger Paints'),
    ('Kansai Nerolac Paints','Kansai Nerolac Paints'),
    ('AkzoNobel India','AkzoNobel India'),
    ('Indigo Paints','Indigo Paints'),
    ('Nippon Paints','Nippon Paints'),
    ('Shalimar Paints','Shalimar Paints'),	
    ('Dulux Paints','Dulux Paints'),
    ('Jenson & Nicholson Paints','Jenson & Nicholson Paints'),	
    ('Sheenlac Paints','Sheenlac Paints'),
    )
CATEGORY = (
    ('Oil Paint','Oil Paint'),
    ('Cement Paint','Cement Paint'),
    ('Distemper Paint','Distemper Paint'),
    ('Emulsion Paint','Emulsion Paint'),
    ('Whitewash','Whitewash'),
    ('Enamel Paint','Enamel Paint'),
    ('Acrylic Emulsion Paint','Acrylic Emulsion Paint'),
    ('Bituminous Paint','Bituminous Paint'),
    ('Synthetic Rubber Paint','Synthetic Rubber Paint'),
    ('Anti-Corrosion Paint','Anti-Corrosion Paint'),
    
)




class Product(models.Model):
    Color_name = models.CharField(max_length=100, null=False)
    Category = models.CharField(max_length=100,choices=CATEGORY, null=False)
    Brand = models.CharField(max_length=100,choices=BRAND, null=False)
    Color_code = models.CharField(max_length=10, null=False)
    quantity = models.PositiveIntegerField(null=False, default=0)
    price = models.PositiveIntegerField(null=False)
    alert_threshold = models.IntegerField(default=10, help_text="Set the alert threshold for low stock")
    
    

    def __str__(self):
        return f'{self.Color_name}'

    def check_quantity_threshold(self):
        if self.quantity <= self.alert_threshold:
            stock_alert.send(sender=self.__class__, product=self)

# Signal
stock_alert = Signal()

# Signal handler
@receiver(stock_alert)
def stock_alert_handler(sender, **kwargs):
    product = kwargs['product']

    

#need changes
class Supplier(models.Model):
    Supplier_Name = models.CharField(max_length=100,null=False)
    Supplier_Phone_number = models.CharField(max_length=100,null=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False )
    
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.Supplier_Name}-{self.Supplier_Phone_number} supplied the {self.product.Category}  {self.product.Brand}  {self.product.Color_code}and ordered by  on {self.date}'
    
    

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
    issued_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.Color_name} - {self.quantity} issued on {self.issued_date}"


def update_product_quantity(sender, instance, **kwargs):
    """
    Signal handler to update product quantity when new stock is added.
    """
    product = instance.product
    product.quantity += instance.quantity
    product.save()


