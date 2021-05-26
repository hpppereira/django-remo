"""
pip install crossrefapi
"""

# import requests
from crossref.restful import Works
# from doi2bib import crossref
# from refextract import extract_references_from_url



works = Works()
a = works.doi('10.1007/s10236-017-1113-9')

for k in a.keys():
    print ('============================================ \n')
    print (k)
    print (a[k])

n = []
nn = []
for i in range(len(a['author'])):
    names = a['author'][i]['given'].split()
    n.append(a['author'][i]['family'] + ', ')
    for ii in range(len(names)):
        n[-1] = n[-1] + names[ii][0] + '. '
c = str(n)[1:-1].replace("'","").replace(". ,", ".;")

# coloca et al se tiver mais que 2 autores
if len(c.split(';')) > 2:
    c = c.split(';')[0].split(',')[0] + ' et al.'

title = a['title'][0]
ano = int(a['issued']['date-parts'][0][0])
url = a['URL']


# # iln = [last_names[i][0] for i in range(len(last_names))]
# c = str(['{}, {}.'.format(a['author'][i]['family'], 
#                           a['author'][i]['given'][0]) for i in range(len(a['author']))]).replace("'", "")[1:-1]


# a = crossref.get_bib_from_doi('https://doi.org/10.1080/1755876X.2019.1606880')
# a = crossref.get_bib('https://doi.org/10.1080/1755876X.2019.1606880')

# b = requests.get('https://doi.org/10.1080/1755876X.2019.1606880')
# a = requests.get("https://api.altmetric.com/v1/doi/"+str(self.doi))

# title = a.json()['title']
# url = a.json()['url']
# ano = datetime.utcfromtimestamp(a.json()['published_on']).strftime('%Y')
# authors = str(a.json()['authors']).replace("[","").replace("]","").replace("'","")

