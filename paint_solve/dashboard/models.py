from django.db import models

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
    Color_name = models.CharField(max_length=100,null=False)
    Category = models.CharField(max_length=100,null=False,choices=CATEGORY)
    Brand = models.CharField(max_length=100,null=False,choices=BRAND)
    Color_code = models.CharField(max_length=10,null=False)
    quantity = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)
    
    class Meta:
        verbose_name_plural = 'product'
    
    def __str__(self):
        return f'{self.Color_name}-{self.Category}-{self.Brand}-{self.Color_code}-{self.quantity}-{self.price}'