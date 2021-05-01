from django.db import models
from django.utils import timezone
# import requests
from crossref.restful import Works
from datetime import datetime
import pandas as pd
import os

class Index(models.Model):
    POSITION = (('L', 'O que é'),
                ('C', 'Objetivos'),
                ('O', 'Dados'))

    position = models.CharField(max_length=1, choices=POSITION,verbose_name="Tipo de Publicação")
    title_pt = models.CharField(verbose_name="Titulo em Português",max_length=200)
    title_en = models.CharField(verbose_name="Titulo em Inglês",max_length=200)
    text_pt = models.TextField(verbose_name="Texto em Português")
    text_en = models.TextField(verbose_name="Texto em Inglês")
    
    def __str__(self):
        return self.title_pt

    class Meta:
        verbose_name = 'Index'
        verbose_name_plural = 'Index'

class Institution(models.Model):
    name = models.CharField(max_length=60,verbose_name="Nome")
    initials = models.CharField(max_length=8,verbose_name="Sigla")
    country = models.CharField(max_length=30,verbose_name="Pais")
    city = models.CharField(max_length=30,verbose_name="Cidade")
    estado = models.CharField(max_length=2,verbose_name="UF")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Instituições'
        verbose_name_plural = 'Instituições'

class Person(models.Model):
    POSITION = (
        ('A', 'Coordenador'),
        ('B', 'Pesquisador'),
        ('C', 'Aluno Pós-Graduação'),
        ('D', 'Aluno Graduação'),
        ('E', 'Técnico'),
        ('F', 'Pesquisador Egresso'),
        ('G', 'Colaborador Externo'),
    )

    name = models.CharField(max_length=60,verbose_name="Nome")
    email = models.EmailField(max_length=60,verbose_name="E-mail", blank=True)
    institution = models.ForeignKey(Institution,verbose_name="Instituição", on_delete=models.CASCADE)
    lattes = models.CharField(max_length=100,verbose_name="Link para o Lattes", blank=True)
    position = models.CharField(max_length=2, choices=POSITION,verbose_name="Cargo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipe'

class Noticia(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title_pt = models.CharField(verbose_name="Titulo em Português",max_length=200)
    title_en = models.CharField(verbose_name="Titulo em Inglês",max_length=200)
    text_pt = models.TextField(verbose_name="Texto em Português")
    text_en = models.TextField(verbose_name="Texto em Inglês")
    image = models.FileField(verbose_name="Imagem",upload_to='imagens/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title_pt

    class Meta:
        verbose_name = 'Notícias'
        verbose_name_plural = 'Notícias'

class Destaque(models.Model):
    title_pt = models.CharField(verbose_name="Titulo em Português",max_length=200)
    title_en = models.CharField(verbose_name="Titulo em Inglês",max_length=200)
    text_pt = models.TextField(verbose_name="Texto em Português")
    text_en = models.TextField(verbose_name="Texto em Inglês")
    image = models.FileField(verbose_name="Imagem",upload_to='imagens/', blank=True, null=True)
    url = models.CharField(verbose_name="URL",max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title_pt

    class Meta:
        verbose_name = 'Destaques'
        verbose_name_plural = 'Destaques'

class Publicacao(models.Model):
    POSITION = (
        ('A', 'Artigos'),
        ('B', 'Livros'),
        ('C', 'Congressos'),
        ('D', 'Monografia'),
        ('E', 'Mestrado'),
        ('F', 'Doutorado'),
    )

    doi = models.CharField("DOI",max_length=200, unique=True, blank=True, null=True, 
                           help_text="Ex: 10.1007/s10236-017-1113-9. Caso a publicação não tenha DOI, preencher os outros campos manualmente")
    title = models.CharField("Titulo",max_length=500,blank=True, null=True, default='#')
    ano = models.CharField("Ano",max_length=4,blank=True, null=True, default='#')
    authors = models.CharField("Autores",max_length=200,blank=True, null=True, default='#')
    url = models.CharField("URL",max_length=200,blank=True, null=True, default='#')
    position = models.CharField(max_length=1, choices=POSITION,verbose_name="Tipo de Publicação")

    def save(self, *args, **kwargs):
        if self.doi != None:
            # a = requests.get("https://api.altmetric.com/v1/doi/"+str(self.doi))
            # self.title = a.json()['title']
            # self.url = a.json()['url']
            # self.ano = datetime.utcfromtimestamp(a.json()['published_on']).strftime('%Y')
            # self.authors = str(a.json()['authors']).replace("[","").replace("]","").replace("'","")
            # print (str(a.json()['authors']).replace("[","").replace("]","").replace("'",""))

            works = Works()
            a = works.doi(str(self.doi))
            self.title = a['title'][0]
            self.ano = int(a['issued']['date-parts'][0][0])
            self.url = a['URL']
            n = []
            nn = []
            for i in range(len(a['author'])):
                names = a['author'][i]['given'].split()
                n.append(a['author'][i]['family'] + ', ')
                for ii in range(len(names)):
                    n[-1] = n[-1] + names[ii][0] + '. '
            self.authors = str(n)[1:-1].replace("'","").replace(". ,", ".;")
            # coloca et al se tiver mais que 2 autores
            if len(self.authors.split(';')) > 2:
                self.authors = self.authors.split(';')[0].split(',')[0] + ' et al.'

        super(Publicacao, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Publicações'
        verbose_name_plural = 'Publicações'   

class Estacao(models.Model):
    nome = models.CharField("Nome da Estação",max_length=200)
    lat = models.FloatField("Latitude")
    lon = models.FloatField("Longitude")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Estações'
        verbose_name_plural = 'Estações' 

class Campanha(models.Model):
    estacao = models.ForeignKey(Estacao,verbose_name='Estação',on_delete=models.CASCADE)
    csv = models.FileField(verbose_name="csv", upload_to='data/', blank=True, null=True)
    prof = models.CharField(max_length=60,verbose_name="Profundidade")
    data_i = models.DateField(verbose_name="Data inicial",blank=True, null=True)
    data_f = models.DateField(verbose_name="Data final",blank=True, null=True)
    # infos = models.TextField("Informações",blank=True, null=True)

    def __str__(self):
        return self.estacao.nome

    def save(self, *args, **kwargs):
        super(Campanha, self).save(*args, **kwargs)

        df = pd.read_csv(os.environ['HOME'] + '/media/' + self.csv.name, parse_dates=True, index_col='date')
        df.replace({pd.np.nan: None}, inplace=True)

        campanha = self

        for i in range(len(df)):
            dados = Dados(
                campanha = campanha,
                date = str(df.index[i]),
                ate = df['ate'][i],
                bat = df['bat'][i],
                bp = df['bp'][i],
                con = df['con'][i],
                dir1 = df['dir1'][i],
                dir2 = df['dir2'][i],
                dir3 = df['dir3'][i],
                dp = df['dp'][i],
                hs = df['hs'][i],
                lat = df['lat'][i],
                lon = df['lon'][i],
                mag1 = df['mag1'][i],
                mag2 = df['mag2'][i],
                mag3 = df['mag3'][i],
                psbe10 = df['psbe10'][i],
                psbe100 = df['psbe100'][i],
                rh = df['rh'][i],
                tdl = df['tdl'][i],
                tp = df['tp'][i],
                tsbe10 = df['tsbe10'][i],
                tsbe100 = df['tsbe100'][i],
                tsbe20 = df['tsbe20'][i],
                tsbe30 = df['tsbe30'][i],
                tsbe40 = df['tsbe40'][i],
                tsbe50 = df['tsbe50'][i],
                tsbe60 = df['tsbe60'][i],
                tsbe70 = df['tsbe70'][i],
                tsbe80 = df['tsbe80'][i],
                tsbe90 = df['tsbe90'][i],
                tsup = df['tsup'][i],
                wd = df['wd'][i],
                ws = df['ws'][i])
            dados.save(force_insert=True)
                
    class Meta:
        verbose_name = 'Campanhas'
        verbose_name_plural =  'Campanhas'  

class Dados(models.Model):
    campanha = models.ForeignKey(Campanha, verbose_name='Estação',on_delete=models.CASCADE)
    date = models.CharField('Data', blank=True, null=True, max_length=60)
    ate = models.FloatField('ate', blank=True, null=True)
    bat = models.FloatField('bat', blank=True, null=True)
    bp = models.FloatField('bp', blank=True, null=True)
    con = models.FloatField('con', blank=True, null=True)
    dir1 = models.FloatField('dir1', blank=True, null=True)
    dir2 = models.FloatField('dir2', blank=True, null=True)
    dir3 = models.FloatField('dir3', blank=True, null=True)
    dp = models.FloatField('dp', blank=True, null=True)
    hs = models.FloatField('hs', blank=True, null=True)
    lat = models.FloatField('lat', blank=True, null=True)
    lon = models.FloatField('lon', blank=True, null=True)
    mag1 = models.FloatField('mag1', blank=True, null=True)
    mag2 = models.FloatField('mag2', blank=True, null=True)
    mag3 = models.FloatField('mag3', blank=True, null=True)
    psbe10 = models.FloatField('psbe10', blank=True, null=True)
    psbe100 = models.FloatField('psbe100', blank=True, null=True)
    rh = models.FloatField('rh', blank=True, null=True)
    tdl = models.FloatField('tdl', blank=True, null=True)
    tp = models.FloatField('tp', blank=True, null=True)
    tsbe10 = models.FloatField('tsbe10', blank=True, null=True)
    tsbe100 = models.FloatField('tsbe100', blank=True, null=True)
    tsbe20 = models.FloatField('tsbe20', blank=True, null=True)
    tsbe30 = models.FloatField('tsbe30', blank=True, null=True)
    tsbe40 = models.FloatField('tsbe40', blank=True, null=True)
    tsbe50 = models.FloatField('tsbe50', blank=True, null=True)
    tsbe60 = models.FloatField('tsbe60', blank=True, null=True)
    tsbe70 = models.FloatField('tsbe70', blank=True, null=True)
    tsbe80 = models.FloatField('tsbe80', blank=True, null=True)
    tsbe90 = models.FloatField('tsbe90', blank=True, null=True)
    tsup = models.FloatField('tsup', blank=True, null=True)
    wd = models.FloatField('wd', blank=True, null=True)
    ws = models.FloatField('ws', blank=True, null=True)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'Dados de Campanhas'
        verbose_name_plural =  'Dados de Campanhas' 

class Contacts(models.Model):
    name = models.CharField(max_length=60,verbose_name="Nome")
    email = models.CharField(max_length=30,verbose_name="Email")
    tel = models.CharField(max_length=30,verbose_name="Tel")

    def __str__(self):
        return self.name

    class Meta:
        # verbose_name = 'Contatos'
        verbose_name_plural = 'Contatos'

# class Diretorios(models.Model):
#     title = models.CharField(verbose_name="Nome do diretório",max_length=200)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = 'Diretório'
#         verbose_name_plural = 'Diretórios'

# class Documentos(models.Model):
#     title = models.CharField(verbose_name="Titulo em Português",max_length=200)
#     docs = models.FileField(verbose_name="Documento",upload_to='docs/', blank=True, null=True)
#     dire = models.ForeignKey(Diretorios,verbose_name='Diretório',on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = 'Documento'
#         verbose_name_plural = 'Documentos'
