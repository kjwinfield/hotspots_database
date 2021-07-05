#Database urls

from django.urls import path 
from . import views
from .views import GeneListView, GRCh37ListView, GRCh38ListView


urlpatterns = [
    #path('',views.home, name='home'),
    path('grch37', GRCh37ListView.as_view()),
    path('grch38', GRCh38ListView.as_view()),
    path('genes', GeneListView.as_view()),
    ]