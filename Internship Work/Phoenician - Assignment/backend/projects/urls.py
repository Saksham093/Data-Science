from django.urls import path
from .views import ItemDetailView

urlpatterns = [
    path('items/', ItemDetailView.as_view(), name='item-detail'),
]
