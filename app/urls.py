from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserDetailsView
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView, BulkProductCreateAPI

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', UserDetailsView.as_view(), name='user-details'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/bulk/', BulkProductCreateAPI.as_view(),
         name='bulk-product-create'),
   	# Bulk create products
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(),
         name='product-detail'),

]
