from django.shortcuts import render, redirect
from django_tables2 import SingleTableView, RequestConfig
from django.views.generic.base import TemplateView
from .models import (
                    GeneName,
                    GrCh37,
                    GrCh38,
                    Chromosome,
                    Hotspots
                    )
from .filters import GRCh37HotspotFilter, GRCh38HotspotFilter, HotspotsFilter
from .tables import Hotspots_Table_37
# Create your views here.

def home(request):
    #return HttpResponse("Welcome to the Database")
    number = GeneName.objects.count()
    context = {"number": number}

    return render (request,'hotspots_database/base.html',context)

class GeneListView(SingleTableView):
    model = GeneName
    template_name='hotspots_database/multiple_table_view.html'

class GRCh37ViewAgain(SingleTableView):
    model = Hotspots_Table_37
    template_name='hotspots_database/genomic_positions.html'

class GRCh37View(TemplateView):
    template_name = 'hotspots_database/datatables_template.html'
    model = GrCh37

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        queryset_positions = GrCh37.objects.all()
        for position in queryset_positions:
            list1 =[]
            queryset_chrom = Chromosome.objects.filter(hotspots__grch37_id=position.grch37_id)
            for chromosome in queryset_chrom:
                list1.append(chromosome.chromosome)
                list1.append(position.genomic_position_start_37)
                list1.append(position.genomic_position_end_37)
                query_gene_2 = GeneName.objects.filter(hotspots__grch37_id=position.grch37_id)
                #print(gene_name
                for each_query in query_gene_2:
                    list1.append(each_query.gene_name)
            data.append(list1)
        context["hotspots"] = data
        return context


class GRCh38View(TemplateView):
    template_name = 'hotspots_database/multiple_table_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        queryset_positions = GrCh38.objects.all()
        for position in queryset_positions:
            list1 =[]
            queryset_chrom = Chromosome.objects.filter(hotspots__grch38_id=position.grch38_id)
            for chromosome in queryset_chrom:
                list1.append(chromosome.chromosome)
                list1.append(position.genomic_position_start_38)
                list1.append(position.genomic_position_end_38)
                query_gene_2 = GeneName.objects.filter(hotspots__grch38_id=position.grch38_id)
                #print(gene_name
                for each_query in query_gene_2:
                    list1.append(each_query.gene_name)
            data.append(list1)

        context["data"] = data
        filter = HotspotsFilter(self.request.GET)
        context["filter"] = filter
        return context

def search_by_position(request, chromosome, position):
    """
    View that checks if there are hotspots at a position
    """
    variants = query_hotspots_at_position(chromosome, position)
    context = {"variants" : variants,
                "position": position,
                "chromosome": chromosome,
                }
    return render(request,
                'hotspots_database/search_by_position.html',
                context)

def query_hotspots_at_position(chromosome, position):
    """
    Performs the django query to look for variants at a position.
    Includes the interpretations and genome build information
    """
    variants_at_pos = GrCh37.objects.all().filter(
                         grch37_id=position)
    variants_at_pos = variants_at_pos.prefetch_related("interpretation_set").all()
    return variants_at_pos

def search(request):
    query = request.GET['query']
    if ":" in query:
        chromosome = int(query.split(":")[0])
        position = query.split(":")[1]
        return redirect('search_by_position', 
                        chromosome=chromosome,
                        position=position)
    else:
        return redirect('home')

def filter_grch37(request):
    filter = GRCh37HotspotFilter(request.GET, queryset=GrCh37.objects.all())
    return render(request, 'hotspots_database/search_by_position.html', {'filter': filter})

def filter_grch38(request):
    filter = GRCh38HotspotFilter(request.GET, queryset=GrCh38.objects.all())
    return render(request, 'hotspots_database/search_by_position.html', {'filter': filter})

