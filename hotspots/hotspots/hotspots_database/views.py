from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django_tables2 import SingleTableView
from .models import (
                    GeneName,
                    GrCh37,
                    GrCh38
                    )
# Create your views here.

def home(request):
    #return HttpResponse("Welcome to the Database")
    number = GeneName.objects.count()
    context = {"number": number}

    return render (request,'hotspots_database/base.html',context)

class GeneListView(SingleTableView):
    model = GeneName
    #table_class = VariantTable
    template_name='hotspots_database/genomic_positions.html'

class GRCh37ListView(SingleTableView):
    model = GrCh37
    #table_class = VariantTable
    template_name='hotspots_database/genomic_positions.html'

class GRCh38ListView(SingleTableView):
    model = GrCh38
    #table_class = VariantTable
    template_name='hotspots_database/genomic_positions.html'