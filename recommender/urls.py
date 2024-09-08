from django.urls import path
from .views import RecommenderView


urlpatterns = [
    path('recommend/<str:pk>', RecommenderView.as_view(), name='recommend'),
]
