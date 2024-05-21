from django.contrib import admin
from escola.models import Estudante,Curso, Matricula

class Estudantes(admin.ModelAdmin):
    list_display = ('id','nome','email','cpf','data_nascimento','celular')
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome', 'cpf',)
    ordering = ('nome',)

admin.site.register(Estudante,Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo','descricao')
    list_display_links = ('id','codigo',)
    search_fields = ('codigo',)

admin.site.register(Curso,Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id','estudante','curso','periodo')
    list_display_links = ('id',)

admin.site.register(Matricula,Matriculas)