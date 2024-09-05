from django.contrib import admin
import main.models as mod

# Register your models here.

admin.site.register(mod.Genotype)
admin.site.register(mod.Species)
admin.site.register(mod.Plant)