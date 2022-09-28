from django.contrib import admin
from .models import Automobilio_modelis, Automobilis, Paslauga, Uzsakymas, Uzsakymo_eilute
# Register your models here.


class UzsakymoEiluteInline(admin.TabularInline):
    model = Uzsakymo_eilute
    can_delete = False
    extra = 0


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('automobilis_id', 'vartotojas', 'data', 'status', 'atsiimti_iki')
    inlines = [UzsakymoEiluteInline]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'auto_modelis_id', 'valst_nr', 'vin')
    list_filter = ('klientas', 'auto_modelis_id')
    search_fields = ('valst_nr', 'vin')


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')


admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Automobilio_modelis)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Uzsakymo_eilute)
