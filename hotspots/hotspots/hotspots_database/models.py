from django.db import models

# Create your models here.
class GeneName(models.Model):
    gene_name = models.CharField(max_length=100)
    hgnc_id = models.CharField(max_length=100)
    hotspot_id = models.AutoField(primary_key=True)

class GrCh37(models.Model):
    hotspot_id = models.ForeignKey(GeneName, on_delete=models.CASCADE)
    genomic_position_start_37 = models.CharField(max_length=100)
    genomic_position_end_37 = models.CharField(max_length=100)

class GrCh38(models.Model):
    hotspot_id = models.ForeignKey(GeneName, on_delete=models.CASCADE)
    genomic_position_start_38 = models.CharField(max_length=100)
    genomic_position_end_38 = models.CharField(max_length=100)