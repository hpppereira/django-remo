from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings
from django.utils import timezone
from django.core.paginator import Paginator
from .models import *
import os
import csv
import json
import ast
from datetime import datetime
# from .forms import NoticiaForm
from filemanager import FileManager


def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    noticias_f = Noticia.objects.all().order_by('-published_date')[0:4]
    dest = Destaque.objects.all()

    index_informs = Index.objects.all()
    # Render the HTML template index.html with the data in the context variable
    auth.logout(request)
    return render(request,'index.html',{"noticias_f": noticias_f, "dest":dest, "index_informs": index_informs})

def index_en(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    noticias_f = Noticia.objects.all().order_by('-published_date')[0:4]
    dest = Destaque.objects.all()

    index_informs = Index.objects.all()
    # Render the HTML template index.html with the data in the context variable
    auth.logout(request)
    return render(request,'index_en.html',{"noticias_f": noticias_f, "dest":dest, "index_informs": index_informs})

def equipe(request):
    lista_coor = Person.objects.filter(position="A").order_by("name")
    lista_pesq = Person.objects.filter(position="B").order_by("name")
    lista_alun_pos = Person.objects.filter(position="C").order_by("name")
    lista_alun_gra = Person.objects.filter(position="D").order_by("name")
    lista_tecn = Person.objects.filter(position="E").order_by("name")
    lista_pesq_eg = Person.objects.filter(position="F").order_by("name")
    lista_colab_ext = Person.objects.filter(position="G").order_by("name")
    auth.logout(request)
    return render(request, 'equipe.html', {"lista_coor": lista_coor,
                                           "lista_pesq": lista_pesq,
                                           "lista_alun_pos": lista_alun_pos, 
                                           "lista_alun_gra": lista_alun_gra,
                                           "lista_tecn": lista_tecn,
                                           "lista_pesq_eg": lista_pesq_eg,
                                           "lista_colab_ext": lista_colab_ext})

def equipe_en(request):
    lista_coor = Person.objects.filter(position="A").order_by("name")
    lista_pesq = Person.objects.filter(position="B").order_by("name")
    lista_alun_pos = Person.objects.filter(position="C").order_by("name")
    lista_alun_gra = Person.objects.filter(position="D").order_by("name")
    lista_tecn = Person.objects.filter(position="E").order_by("name")
    lista_pesq_eg = Person.objects.filter(position="F").order_by("name")
    lista_colab_ext = Person.objects.filter(position="G").order_by("name")
    auth.logout(request)
    return render(request, 'equipe_en.html', {"lista_coor": lista_coor,
                                              "lista_pesq": lista_pesq,
                                              "lista_alun_pos": lista_alun_pos, 
                                              "lista_alun_gra": lista_alun_gra,
                                              "lista_tecn": lista_tecn,
                                              "lista_pesq_eg": lista_pesq_eg,
                                              "lista_colab_ext": lista_colab_ext})

def publicacoes(request):
    artigo = Publicacao.objects.filter(position="A").order_by('-ano')
    livro = Publicacao.objects.filter(position="B").order_by('-ano')
    congresso = Publicacao.objects.filter(position="C").order_by('-ano')
    monografia = Publicacao.objects.filter(position="D").order_by('-ano')
    mestrado = Publicacao.objects.filter(position="E").order_by('-ano')
    doutorado = Publicacao.objects.filter(position="F").order_by('-ano')
    auth.logout(request)
    return render(request, 'publicacoes.html', {"artigo": artigo,
                                                "livro": livro,
                                                "congresso": congresso,
                                                "monografia": monografia,
                                                "mestrado": mestrado,
                                                "doutorado": doutorado})    

def publicacoes_en(request):
    artigo = Publicacao.objects.filter(position="A").order_by('-ano')
    livro = Publicacao.objects.filter(position="B").order_by('-ano')
    congresso = Publicacao.objects.filter(position="C").order_by('-ano')
    monografia = Publicacao.objects.filter(position="D").order_by('-ano')
    mestrado = Publicacao.objects.filter(position="E").order_by('-ano')
    doutorado = Publicacao.objects.filter(position="F").order_by('-ano')
    auth.logout(request)
    return render(request, 'publicacoes_en.html', {"artigo": artigo,
                                                "livro": livro,
                                                "congresso": congresso,
                                                "monografia": monografia,
                                                "mestrado": mestrado,
                                                "doutorado": doutorado})    

def noticias_list(request):
    posts_list = Noticia.objects.order_by('-published_date')
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    auth.logout(request)
    return render(request, 'noticias_list.html', {'posts': posts})

def noticias_list_en(request):
    posts_list = Noticia.objects.order_by('-published_date')
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    auth.logout(request)
    return render(request, 'noticias_list_en.html', {'posts': posts})

def noticias_detail(request, pk):
    post = Noticia.objects.get(pk=pk)
    auth.logout(request)
    return render(request, 'noticias_detail.html', {'post': post})

def noticias_detail_en(request, pk):
    post = Noticia.objects.get(pk=pk)
    auth.logout(request)
    return render(request, 'noticias_detail_en.html', {'post': post})

# @login_required
def modelagem(request):
    return render(request, 'modelagem.html')

# @login_required
def modelagem_en(request):
    return render(request, 'modelagem_en.html')

# @login_required
def dados(request):
    lista_esta = Estacao.objects.all()
    dados_esta = []
    for linha in lista_esta:
        lista_sec = Campanha.objects.filter(estacao=linha)
        for linha2 in lista_sec:
            print(linha2.id)
            try:
                a = {
                'id': linha.id,'nome': linha.nome,
                'lat': str(linha.lat).replace(",","."),
                'lon': str(linha.lon).replace(",","."),
                'prof': linha2.prof,
                'id_serie': linha2.id,
                'data_i': linha2.data_i.strftime("%d/%m/%Y"),
                'data_f': linha2.data_f.strftime("%d/%m/%Y"),
                'dados': linha2.csv
                }
            except:
                a = {
                'id': linha.id,'nome': linha.nome,
                'lat': str(linha.lat).replace(",","."),
                'lon': str(linha.lon).replace(",","."),
                'prof': linha2.prof,
                'id_serie': linha2.id,
                'data_i': "Sem Infos",
                'data_f': "Sem Infos",
                'dados': linha2.csv
                }                
            dados_esta.append(a)
    return render(request, 'dados.html', {'lista_esta': dados_esta})

# @login_required
def dados_en(request):
    lista_esta = Estacao.objects.all()
    dados_esta = []
    for linha in lista_esta:
        lista_sec = Campanha.objects.filter(estacao=linha)
        for linha2 in lista_sec:
            print(linha2.id)
            try:
                a = {
                'id': linha.id,'nome': linha.nome,
                'lat': str(linha.lat).replace(",","."),
                'lon': str(linha.lon).replace(",","."),
                'prof': linha2.prof,
                'id_serie': linha2.id,
                'data_i': linha2.data_i.strftime("%d/%m/%Y"),
                'data_f': linha2.data_f.strftime("%d/%m/%Y"),
                'dados': linha2.csv
                }
            except:
                a = {
                'id': linha.id,'nome': linha.nome,
                'lat': str(linha.lat).replace(",","."),
                'lon': str(linha.lon).replace(",","."),
                'prof': linha2.prof,
                'id_serie': linha2.id,
                'data_i': "Sem Infos",
                'data_f': "Sem Infos",
                'dados': linha2.csv
                }                
            dados_esta.append(a)
    return render(request, 'dados_en.html', {'lista_esta': dados_esta})

# @login_required
def dados_grafic(request, pk):
    campanha = Campanha.objects.get(pk=pk)
    lista_csv = Dados.objects.all().filter(campanha=campanha)
    saida = []
    for x in lista_csv:
        data = (datetime.strptime(x.date, '%Y-%m-%d %H:%M:%S')).timestamp() * 1000
        ws = str(x.ws)
        wd = str(x.wd)
        tsup = str(x.tsup)
        ate = str(x.ate)
        rh = str(x.rh)
        bp = str(x.bp)
        hs = str(x.hs)
        tp = str(x.tp)
        mag1 = str(x.mag1)
        dir1 = str(x.dir1)
        tsbe10 = str(x.tsbe10)
        tsbe100 =str(x.tsbe100)
        tsbe20 = str(x.tsbe20)
        tsbe30 = str(x.tsbe30)
        tsbe40 = str(x.tsbe40)
        tsbe50 = str(x.tsbe50)
        tsbe60 = str(x.tsbe60)
        tsbe70 = str(x.tsbe70)
        tsbe80 = str(x.tsbe80)
        tsbe90 = str(x.tsbe90)
        saida.append({"data":"{:.0f}".format(data),
                      "ws":ws.replace('None', 'null'),
                      "wd":wd.replace('None', 'null'),
                      "tsup":tsup.replace('None', 'null'),
                      "ate":ate.replace('None', 'null'),
                      "rh":rh.replace('None', 'null'),
                      "bp":bp.replace('None', 'null'),
                      "hs":hs.replace('None', 'null'),
                      "tp":tp.replace('None', 'null'),
                      "mag1":mag1.replace('None', 'null'),
                      "dir1":dir1.replace('None', 'null'),
                      "tsbe10":tsbe10.replace('None', 'null'),
                      "tsbe100":tsbe100.replace('None', 'null'),
                      "tsbe20":tsbe20.replace('None', 'null'),
                      "tsbe30":tsbe30.replace('None', 'null'),
                      "tsbe40":tsbe40.replace('None', 'null'),
                      "tsbe50":tsbe50.replace('None', 'null'),
                      "tsbe60":tsbe60.replace('None', 'null'),
                      "tsbe70":tsbe70.replace('None', 'null'),
                      "tsbe80":tsbe80.replace('None', 'null'),
                      "tsbe90":tsbe90.replace('None', 'null')})
    return render(request, 'dados_grafic.html', {'lista_csv': saida})

# @login_required
def dados_grafic_en(request, pk):
    campanha = Campanha.objects.get(pk=pk)
    lista_csv = Dados.objects.all().filter(campanha=campanha)
    saida = []
    for x in lista_csv:
        data = (datetime.strptime(x.date, '%Y-%m-%d %H:%M:%S')).timestamp() * 1000
        ws = str(x.ws)
        wd = str(x.wd)
        tsup = str(x.tsup)
        ate = str(x.ate)
        rh = str(x.rh)
        bp = str(x.bp)
        hs = str(x.hs)
        tp = str(x.tp)
        mag1 = str(x.mag1)
        dir1 = str(x.dir1)
        tsbe10 = str(x.tsbe10)
        tsbe100 =str(x.tsbe100)
        tsbe20 = str(x.tsbe20)
        tsbe30 = str(x.tsbe30)
        tsbe40 = str(x.tsbe40)
        tsbe50 = str(x.tsbe50)
        tsbe60 = str(x.tsbe60)
        tsbe70 = str(x.tsbe70)
        tsbe80 = str(x.tsbe80)
        tsbe90 = str(x.tsbe90)
        saida.append({"data":"{:.0f}".format(data),
                      "ws":ws.replace('None', 'null'),
                      "wd":wd.replace('None', 'null'),
                      "tsup":tsup.replace('None', 'null'),
                      "ate":ate.replace('None', 'null'),
                      "rh":rh.replace('None', 'null'),
                      "bp":bp.replace('None', 'null'),
                      "hs":hs.replace('None', 'null'),
                      "tp":tp.replace('None', 'null'),
                      "mag1":mag1.replace('None', 'null'),
                      "dir1":dir1.replace('None', 'null'),
                      "tsbe10":tsbe10.replace('None', 'null'),
                      "tsbe100":tsbe100.replace('None', 'null'),
                      "tsbe20":tsbe20.replace('None', 'null'),
                      "tsbe30":tsbe30.replace('None', 'null'),
                      "tsbe40":tsbe40.replace('None', 'null'),
                      "tsbe50":tsbe50.replace('None', 'null'),
                      "tsbe60":tsbe60.replace('None', 'null'),
                      "tsbe70":tsbe70.replace('None', 'null'),
                      "tsbe80":tsbe80.replace('None', 'null'),
                      "tsbe90":tsbe90.replace('None', 'null')})
    return render(request, 'dados_grafic_en.html', {'lista_csv': saida})

def contatos(request):
    contatos = Contacts.objects.all()
    return render(request, 'contatos.html', {"contatos": contatos})

def contatos_en(request):
    contatos = Contacts.objects.all()
    return render(request, 'contatos_en.html', {"contatos": contatos})

@login_required
def documentos(request):
    return render(request, 'documentos.html')

@login_required
def documentos1(request, path):
    extensions = ['html', 'htm', 'zip', 'py', 'css', 'js', 'jpeg', 'jpg', 'png', 'pdf', 'docx']
    fm = FileManager(settings.MEDIA_ROOT + '/docs/', extensions=extensions)
    return fm.render(request, path)
