from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
from filemanager import path_end
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('index_en/', views.index_en, name='index_en'),
    path('equipe/', views.equipe, name='equipe'),
    path('equipe_en/', views.equipe_en, name='equipe_en'),
    path('publicacoes/', views.publicacoes, name='publicacoes'), 
    path('publicacoes_en/', views.publicacoes_en, name='publicacoes_en'), 
    path('noticias/', views.noticias_list, name='noticias_list'),
    path('noticias_en/', views.noticias_list_en, name='noticias_list_en'),
    path('noticias/post/<int:pk>', views.noticias_detail, name='noticias_detail'),
    path('noticias_en/post/<int:pk>', views.noticias_detail_en, name='noticias_detail_en'),
    path('modelagem/', views.modelagem, name='modelagem'), 
    path('modelagem_en/', views.modelagem_en, name='modelagem_en'),
    path('dados/', views.dados, name='dados'),
    path('dados_en/', views.dados_en, name='dados_en'), 
    path('dados/grafic/<int:pk>', views.dados_grafic, name="dados_grafic"),
    path('dados_en/grafic/<int:pk>', views.dados_grafic_en, name="dados_grafic_en"),
    path('contatos/', views.contatos, name='contatos'),
    path('contatos_en/', views.contatos_en, name='contatos_en'),
    path('documentos/', views.documentos, name='documentos'),
    url(r'^documentos1/' + path_end, views.documentos1, name='documentos1'),
]