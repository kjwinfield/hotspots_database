from django.db import models

# Create your models here.
class GeneName(models.Model):
    gene_name = models.CharField(max_length=100)
    hgnc_id = models.CharField(max_length=100)
    gene_id = models.AutoField(primary_key=True)

class Chromosome(models.Model):
    chromosome_id = models.AutoField(primary_key=True)
    chromosome = models.CharField(max_length=10)

class GrCh37(models.Model):
    grch37_id = models.AutoField(primary_key=True)
    genomic_position_start_37 = models.CharField(max_length=100)
    genomic_position_end_37 = models.CharField(max_length=100)

class GrCh38(models.Model):
    grch38_id = models.AutoField(primary_key=True)
    genomic_position_start_38 = models.CharField(max_length=100)
    genomic_position_end_38 = models.CharField(max_length=100)

class Hotspots(models.Model):
    gene_id = models.ForeignKey(GeneName, on_delete=models.CASCADE)
    hotspot_id = models.AutoField(primary_key=True)
    grch37_id = models.ForeignKey(GrCh37, on_delete=models.CASCADE)
    grch38_id = models.ForeignKey(GrCh38, on_delete=models.CASCADE)
    chromosome_id = models.ForeignKey(Chromosome, on_delete=models.CASCADE)