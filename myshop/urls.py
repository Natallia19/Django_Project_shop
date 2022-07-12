from django.urls import path, include, re_path
from . import views

app_name = 'myshop'

urlpatterns = [
    re_path(r'^orders/', include('orders.urls', namespace='orders')),
    path('', views.product_list, name='product_list'),  # на главной странице будем отображать весь product_list
    path('<slug:category_slug>/', views.product_list,   # будем отображать товар по категориям
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,  # будем отображать каждый товар по отдельности
         name='product_detail'),

]
