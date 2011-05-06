# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import Enquete, Opcao

class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 3

class EnqueteAdmin(admin.ModelAdmin):
    inlines = [OpcaoInline, ]

admin.site.register(Enquete, EnqueteAdmin)
