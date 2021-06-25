#Database urls

from django.urls import path 
from . import views
from .views import GenomicPositionListView

urlpatterns = [
    path('',views.home, name='home'),
    path('genomic_positions', GenomicPositionListView.as_view()),
]