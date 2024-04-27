from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('book/', views.book_register, name='book_register'),
    path('<slug:slug_c>/',views.home,name="product_by_category"),
    path('<slug:slug_c>/<slug_p>/',views.product_details,name="product_details")

]