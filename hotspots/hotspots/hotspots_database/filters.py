import django_filters
from django import forms
from .models import GrCh37, GrCh38

class HotspotsFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(HotspotsFilter, self).__init__(*args, **kwargs)
        self.filters['genomic_position_end_37'].label = 'Positions Matching'

    grch37_start = django_filters.CharFilter(
        field_name='genomic_position_start_37',
        label='Start position on 37:',
        help_text = '(Genomic start position on GRCh37)',
        lookup_expr='icontains',
        )

    grch37_end = django_filters.CharFilter(
        field_name='genomic_position_end_37',
        label='End position on 37:',
        help_text = '(Genomic end position on GRCh37)',
        lookup_expr='icontains',
        )
    grch38_start = django_filters.CharFilter(
        field_name='genomic_position_start_38',
        label='Start position on 38:',
        help_text = '(Genomic start position on GRCh38)',
        lookup_expr='icontains',
        )

    grch38_end = django_filters.CharFilter(
        field_name='genomic_position_end_38',
        label='End position on 38:',
        help_text = '(Genomic end position on GRCh38)',
        lookup_expr='icontains',
        )

class GRCh37HotspotFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(GRCh37HotspotFilter, self).__init__(*args, **kwargs)
        #self.filters['genomic_position_end_37'].label = 'Positions Matching'

    # grch37_start = django_filters.CharFilter(
    #     field_name='genomic_position_start_37',
    #     label='Genomic start position on 37:',
    #     lookup_expr='icontains',
    #     )

    # grch37_end = django_filters.CharFilter(
    #     field_name='genomic_position_end_37',
    #     label='Genomci end position on 37:',
    #     lookup_expr='icontains',
    #     )

    class Meta:
        model = GrCh37
        fields = ['genomic_position_start_37', 'genomic_position_end_37']

class GRCh38HotspotFilter(django_filters.FilterSet):
    class Meta:
        model = GrCh38
        fields = ['genomic_position_start_38', 'genomic_position_end_38']