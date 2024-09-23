from django.contrib import admin
import main.models as mod

# Register your models here.

admin.site.register(mod.Taxon)
admin.site.register(mod.Genotype)
admin.site.register(mod.Cross)
admin.site.register(mod.Event)
admin.site.register(mod.Distinction)
