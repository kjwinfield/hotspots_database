from django.db import models
from django.utils import timezone
from datetime import datetime
from convert_excel import input1

# Create your models here.

# class HugoSymbol(models.Model):
#     hugo_symbol = models.CharField(max_length=10)

# class NumberOfMutations(models.Model)
#     total_mutations = models.CharField(max_length=30)

# class PanelType(models.Model):

class HugoSymbol(models.Model):
    hugo_symbol = []

    for hugo_symbol in input1.hugo_symbol:
        hugo_symbol.append((panel_type, panel_type))

    type = models.CharField(max_length=50, choices=hugo_symbol)

    class Meta:
        db_table = "hugo_symbol"