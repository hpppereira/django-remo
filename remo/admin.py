from django.contrib import admin
from .models import *

class IndexAdmin(admin.ModelAdmin):
    list_display = ('title_pt', 'title_en', 'text_pt', 'text_en', 'position')
    search_fields = ('title_pt', 'title_en', 'text_pt', 'text_en', 'position')
admin.site.register(Index, IndexAdmin)

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'initials', 'country', 'city')
    search_fields = ('name', 'initials', 'country', 'city')
admin.site.register(Institution, InstitutionAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'institution', 'position')
    list_filter = ('institution', 'position')
admin.site.register(Person, PersonAdmin)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('title_pt', 'published_date', 'author')
    list_filter = ('author',)
admin.site.register(Noticia, NoticiaAdmin)

class CampanhaAdmin(admin.ModelAdmin):
    list_display = ('estacao','prof', 'csv', 'data_i', 'data_f')
    list_filter = ('estacao',)
admin.site.register(Campanha,CampanhaAdmin)

class DestaqueAdmin(admin.ModelAdmin):
	list_display = ('title_pt','text_pt')
	search_fields = ('title_pt','text_pt')
admin.site.register(Destaque,DestaqueAdmin)

class EstacaoAdmin(admin.ModelAdmin):
	list_display = ('nome','lat','lon')
	search_fields = ('nome','lat','lon')
admin.site.register(Estacao,EstacaoAdmin)

class PublicacaoAdmin(admin.ModelAdmin):
	list_display = ('doi', 'title','ano','authors', 'url', 'position')
	search_fields = ('doi', 'title','ano','authors', 'url', 'position')
admin.site.register(Publicacao,PublicacaoAdmin)

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'tel')
admin.site.register(Contacts, ContactsAdmin)

# class DiretoriosAdmin(admin.ModelAdmin):
#     list_display = ('title',)
# admin.site.register(Diretorios,DiretoriosAdmin)

# class DocumentosAdmin(admin.ModelAdmin):
#     list_display = ('title',)
# admin.site.register(Documentos, DocumentosAdmin)
