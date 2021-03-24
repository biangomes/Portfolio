from django.contrib import admin
from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]

# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)