from django.contrib import admin

# Register your models here.
from agenda.models import *

admin.site.register(Usuario)
admin.site.register(Compromisso)
admin.site.register(Tipo)
admin.site.register(Agenda)
admin.site.register(CompromissoUsuario)
admin.site.register(AgendaUsuario)



