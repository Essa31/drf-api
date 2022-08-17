from django.urls import path

from .views import BikeListView, BikeDetailView

urlpatterns = [
    path('', BikeListView.as_view(), name='bike_list'),
    path('<int:pk>/', BikeDetailView.as_view(), name='bike_detail'),
]