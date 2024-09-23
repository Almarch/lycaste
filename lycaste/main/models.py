from django.db import models

# Create your models here.

class Taxon(models.Model):

    def __str__(self):
        return f'{self.name}'

    name  = models.fields.CharField(null=False, max_length=100)
    supra = models.ForeignKey('self', related_name='infra', null=True, blank=True, on_delete=models.SET_NULL)
    photo = models.fields.CharField(null=True)
    description_fr = models.fields.CharField(null=True)
    description_es = models.fields.CharField(null=True)
    description_en = models.fields.CharField(null=True)
    
class Genotype(models.Model):
    name = models.fields.CharField(null=True, max_length=100)
    taxon = models.ForeignKey(Taxon, related_name='all_genotypes', null=True, on_delete=models.SET_NULL)
    cross = models.ForeignKey('Cross', related_name='siblings', null=True, on_delete=models.SET_NULL)
    location = models.fields.CharField(null=True, max_length=255)
    photo = models.fields.CharField(null=True)
    description_fr = models.fields.CharField(null=True)
    description_es = models.fields.CharField(null=True)
    description_en = models.fields.CharField(null=True)

class Cross(models.Model):
    mother = models.ForeignKey(Genotype, related_name='offspring_as_mother', null=True, on_delete=models.SET_NULL)
    father = models.ForeignKey(Genotype, related_name='offspring_as_father', null=True, on_delete=models.SET_NULL)
    who_crossed  = models.fields.CharField(null=True, max_length=255)
    date_crossed = models.fields.DateField(null=True)
    date_sown    = models.fields.DateField(null=True)

class Event(models.Model):
    name        = models.fields.CharField(null=False, max_length=100)
    date        = models.fields.DateField(null=False)
    country     = models.fields.CharField(null=False, max_length=50)
    city        = models.fields.CharField(null=False, max_length=50)
    description = models.fields.CharField(null=True, max_length=255)

class Distinction(models.Model):
    genotype = models.ForeignKey(Genotype, related_name='all_prices', null=True, on_delete=models.SET_NULL)
    event    = models.ForeignKey(Event,    related_name='all_prices', null=True, on_delete=models.SET_NULL)
    description = models.fields.CharField(null=True, max_length=255)