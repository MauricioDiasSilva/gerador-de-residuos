# residuos/admin.py
from django.contrib import admin
from .models import Residuo, Coleta,Recompensa

class RecompensaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pontos_necessarios', 'empresa')
    search_fields = ('nome', 'empresa')
    
admin.site.register(Residuo)
admin.site.register(Coleta)
admin.site.register(Recompensa, RecompensaAdmin)





