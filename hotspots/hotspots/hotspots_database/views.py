from django.shortcuts import render
from django_tables2 import SingleTableView
from .models import (
                    Hotspots
                    )
# Create your views here.

def home(request):
    #return HttpResponse("Welcome to the Something Snappy Database")
    number = Hotspots.objects.count()
    context = {"number": number}

    return render (request,'hotspots_database/base.html',context)

class GenomicPositionListView(SingleTableView):
    model = Hotspots
    #table_class = VariantTable
    template_name='hotspots_database/genomic_positions.html'