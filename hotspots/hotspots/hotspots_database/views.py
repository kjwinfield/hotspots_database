from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django_tables2 import SingleTableView, RequestConfig
from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView
from .tables import CompleteTable
from .models import (
                    GeneName,
                    GrCh37,
                    GrCh38,
                    Chromosome,
                    Hotspots
                    )
# Create your views here.

def home(request):
    #return HttpResponse("Welcome to the Database")
    number = GeneName.objects.count()
    context = {"number": number}

    return render (request,'hotspots_database/base.html',context)

class GeneListView(SingleTableView):
    model = GeneName
    template_name='hotspots_database/genomic_positions.html'

class GRCh37View(TemplateView):
    #table_class = CompleteTable
    template_name = 'hotspots_database/multiple_table_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        queryset_chr = Chromosome.objects.all()
        for chrom in queryset_chr:
            queryset_grch37 = GrCh37.objects.filter(hotspots__chromosome_id=chrom.chromosome_id)

            for grch37_coor in queryset_grch37:
                data.append([chrom.chromosome, grch37_coor.genomic_position_start_37, grch37_coor.genomic_position_end_37])

        context["data"] = data
        return context


class GRCh38View(TemplateView):
    #table_class = CompleteTable
    template_name = 'hotspots_database/multiple_table_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        queryset_chr = Chromosome.objects.all()
        for chrom in queryset_chr:
            queryset_grch38 = GrCh38.objects.filter(hotspots__chromosome_id=chrom.chromosome_id)

            for grch37_coor in queryset_grch38:
                data.append([chrom.chromosome, grch37_coor.genomic_position_start_38, grch37_coor.genomic_position_end_38])

        context["data"] = data
        return context
