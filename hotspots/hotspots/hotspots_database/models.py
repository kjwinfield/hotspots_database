from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.

# class HugoSymbol(models.Model):
#     hugo_symbol = models.CharField(max_length=10)

# class NumberOfMutations(models.Model)
#     total_mutations = models.CharField(max_length=30)

# class PanelType(models.Model):

class Codon(models.Model):
    codon_position_id = models.AutoField(primary_key=True)
    gene_name = models.CharField(max_length=30)
    amino_acid_position = models.CharField(max_length=30)
    trinucleotides = models.CharField(max_length=30)

class AminoAcidChange(models.Model):
    codon_position_id = models.AutoField(primary_key=True)
    gene_name = models.CharField(max_length=30)
    amino_acid_position = models.CharField(max_length=30)
    trinucleotides = models.CharField(max_length=30)

class Hotspots(models.Model):
    codon_position_id = models.AutoField(primary_key=True)
    gene_name = models.CharField(max_length=30)
    amino_acid_position = models.CharField(max_length=30)
    genomic_position = models.CharField(max_length=30)

class Gene(models.Model):
    hgnc_id = models.CharField(max_length=30)
    gene_name = models.CharField(max_length=30)
    q_value = models.CharField(max_length=30)

class Sample(models.Model):
    codon_position_id = models.ForeignKey(Codon, on_delete=models.CASCADE)
