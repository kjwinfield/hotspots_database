import django_tables2 as tables
from .models import (
                    GeneName,
                    GrCh37,
                    GrCh38,
                    Chromosome
                    )

class CompleteTable(tables.Table):
    chromosome=tables.Column(accessor='chromosome')
    genomic_position_start_37=tables.Column(accessor='genomic_position_start_37')
    genomic_position_start_38=tables.Column(accessor='genomic_position_end_37')

    class Meta:
        model=GrCh37


