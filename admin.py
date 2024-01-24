from django.contrib import admin
from .models import Producto, DetalleBoleta, Boleta,Solicitud
from .views import SolicitudView
# Register your models here.

admin.site.register(Producto)
admin.site.register(DetalleBoleta)
admin.site.register(Boleta)
admin.site.register(Solicitud)
class DetalleBoletaInline(admin.TabularInline):
    model = DetalleBoleta

class BoletaAdmin(admin.ModelAdmin):
    inlines = [DetalleBoletaInline]
    list_display = ('id', 'fecha', 'total', 'solicitud_link')


