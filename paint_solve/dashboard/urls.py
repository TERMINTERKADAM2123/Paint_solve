
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.product_view,name="products"),
    path('add_record/',views.add_record,name="add_record"),
    path('records/<int:pk>',views.product_record,name="records"),
    path('delete_records/<int:pk>',views.delete_record,name="delete_records"),
    path('update_records/<int:pk>',views.update_records,name="update_records"),
    
]
