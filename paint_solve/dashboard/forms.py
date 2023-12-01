from django import forms
from .models import Product ,Supplier
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
class AddRecordForm(forms.ModelForm):
    # Color_name = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Color Name","class":"form-control"}),label="")
    # Category = forms.CharField(required=True,choices=CATEGORY,widget=forms.widgets.ChoiceWidget(attrs={"placeholder":"Category ","class":"form-control"}),label="")
    # Brand = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Brand ","class":"form-control"}),label="")
    # Color_code = forms.CharField(required=True,widget=forms.widgets.NumberInput(attrs={"placeholder":"Color Code","class":"form-control"}),label="")
    # quantity = forms.CharField(required=True,widget=forms.widgets.NumberInput(attrs={"placeholder":"Quantity","class":"form-control"}),label="")
    # price = forms.CharField(required=True,widget=forms.widgets.NumberInput(attrs={"placeholder":"Price","class":"form-control"}),label="")
    
    class Meta:
        model = Product
        fields = '__all__'

class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Product
     fields = ['Category','Brand',]
     
# class SupplierAddForm(forms.ModelForm):
#     class Meta:
#      model = Supplier
#      fields = '__all__'
     
class SupplierAddForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['Supplier_Name', 'Supplier_Phone_number', 'color_name','Color_code', 'category', 'brand', 'quantity', 'price']

    color_name = forms.CharField(max_length=100)
    category = forms.ChoiceField(choices=CATEGORY)
    brand = forms.ChoiceField(choices=BRAND)
    Color_code = forms.CharField(max_length=100)
    quantity = forms.IntegerField()
    price = forms.IntegerField()



# class SupplierForm(forms.ModelForm):
#     class Meta:
#         model = Supplier
#         fields = ['Supplier_Name', 'Supplier_Phone_number', 'product']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Add fields from the Product model to the form
#         product_fields = ['Color_name', 'Category', 'Brand', 'Color_code', 'quantity', 'price']
#         for field in product_fields:
#             self.fields[field] = forms.CharField()  
            
            
            # You can use appropriate form field types here

# class SupplierAddForm(forms.ModelForm):
#     class Meta:
#         model = Supplier
#         fields = ['Supplier_Name', 'Supplier_Phone_number', 'color_name', 'Color_code', 'category', 'brand', 'quantity', 'price']

#     color_name = forms.CharField(max_length=100)
#     category = forms.ChoiceField(choices=CATEGORY)
#     brand = forms.ChoiceField(choices=BRAND)
#     Color_code = forms.CharField(max_length=100)
#     quantity = forms.IntegerField()
#     price = forms.IntegerField()

#     def clean(self):
#         cleaned_data = super().clean()
#         quantity = cleaned_data.get('quantity')
#         price = cleaned_data.get('price')

#         # Check if quantity or price is not provided
#         if quantity is None or price is None:
#             raise forms.ValidationError("Quantity and price must be provided.")

#         return cleaned_data
