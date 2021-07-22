#Database urls
from django.urls import path 
from . import views
from .views import GeneListView, GRCh37View, GRCh38View, GRCh37ViewAgain


urlpatterns = [
    path('',views.home, name='home'),
    path('genes', GeneListView.as_view()),
    path('grch37', GRCh37View.as_view()),
    path('grch38', GRCh38View.as_view()),
    path('grch37_2', GRCh37ViewAgain.as_view()),
    path('results/',views.search, name='search'),
    path('search_by_position/<str:chromosome>/<str:position>/',
			    	views.search_by_position, 
			    	name='search_by_position'),
    path('grch37_search',views.filter_grch37, name='grch37_filter'),
    path('grch38_search',views.filter_grch38, name='grch38_filter'),
    ]