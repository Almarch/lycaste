from django.db import models

# Create your models here.

class Genotype(models.Model):
    name=models.fields.CharField(max_length=100)
    father=models.fields.CharField(max_length=100)
    mother=models.fields.CharField(max_length=100)
    location=models.fields.CharField(max_length=100)
    species=models.fields.CharField(max_length=100)
    distinction=models.fields.CharField(max_length=100)
    picture=models.fields.CharField(max_length=100)

class Species(models.Model):
    name=models.fields.CharField(max_length=100)
    picture=models.fields.CharField(max_length=100)

class Plant(models.Model):
    genotype=models.fields.CharField(max_length=100)
    price=models.fields.CharField(max_length=100)