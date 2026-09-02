from django.contrib import admin

# Register your models here.
from forum.models import Pergunta, Resposta
admin.site.register(Pergunta)
admin.site.register(Resposta)