import django_tables2 as tables
from .models import Hotspots

class Hotspots_Table_37(tables.Table):


    class Meta:
        model = Hotspots
        fields = [
            'chromosome_id__chromosome_chromosome',
            'grch37_id__grch37__genomic_position_start_37',
            'grch37_id__grch37__genomic_position_end_37',
            'gene_id__genename_gene_name',
            ]
