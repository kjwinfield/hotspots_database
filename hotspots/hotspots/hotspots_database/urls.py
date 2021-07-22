#Database urls
from django.urls import path 
from . import views
from .views import GeneListView, GRCh37View, GRCh38View


urlpatterns = [
    path('',views.home, name='home'),
    path('genes', GeneListView.as_view()),
    path('grch37', GRCh37View.as_view()),
    path('grch38', GRCh38View.as_view()),
    ]