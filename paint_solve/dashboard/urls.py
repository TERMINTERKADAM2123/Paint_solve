
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.product_view,name="products"),
    path('supplier/',views.supplier,name="supplier"),
    path('add_record/',views.add_record,name="add_record"),
    path('issue_product/',views.issue_product,name="issue_product"),
    path('add_supplier/',views.add_supplier,name="add_supplier"),
    path('records/<int:pk>',views.product_record,name="records"),
    path('supplier_records/<int:pk>',views.supplier_record,name="supplier_records"),
    path('delete_records/<int:pk>',views.delete_record,name="delete_records"),
    path('update_records/<int:pk>',views.update_records,name="update_records"),
    # path('view_stock/', views.view_stock, name='view_stock'),    

    
]
