import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from escola.models import Curso

dados = [
    ('CPOO1', 'Curso de Python Orientação à Objetos 01'),
    ('CPOO2', 'Curso de Python Orientação à Objetos 02'),
    ('CPOO3', 'Curso de Python Orientação à Objetos 03'),
    ('CDJ01', 'Curso de Django 01'),
    ('CDJ02', 'Curso de Django 02'),
    ('CDJ03', 'Curso de Django 03'),
    ('CDJ04', 'Curso de Django 04'),
    ('CDJ05', 'Curso de Django 05'),
    ('CDJRF01', 'Curso de Django REST Framework 01'),
    ('CDJRF02', 'Curso de Django REST Framework 02'),
    ('CDJRF03', 'Curso de Django REST Framework 03'),
    ('CDJRF04', 'Curso de Django REST Framework 04')
]

niveis = ['B', 'I', 'A']

def criar_cursos():
    for codigo, descricao in dados:
        nivel = random.choice(niveis)
        Curso.objects.create(codigo=codigo, descricao=descricao, nivel=nivel)

criar_cursos()