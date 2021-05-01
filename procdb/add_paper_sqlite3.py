# -*- coding: utf-8 -*-
"""
Ferramentas para popular o banco de dados da página da REMO

**Funções**

>> :func:`funcao` <<
    Popular BD.

**Instituições**
1 - UFRJ
2 - UFBA
3 - Petrobras

**Cargos Pesquisador**
A - Coordenador
B - Pesquisador
C - Aluno Pós-Graduação
D - Aluno Graduação
E - Técnico
----------

"""

import numpy as np
import pandas as pd
import sqlite3
from sqlite3 import Error


# read csv with data.
df = pd.read_excel('data/tabela_paper_REMO.xlsx')

# subsitui palavras por indices do banco

# list of tuples
data = [tuple([int(df.ano[i]), df.autor[i], df.tipo[i],
               df.doi[i], df.url[i], df.titulo[i]])
               for i in range(len(df))]

try:
    conn = sqlite3.connect('../db.sqlite3')
    conn.text_factory = str
except Error as e:
    print(e)

cur = conn.cursor()

# delete from your_table;
# delete from sqlite_sequence where name='your_table';
    
sql = ''' INSERT INTO remo_publicacao(ano,authors,position,doi,url,title)
          VALUES (?,?,?,?,?,?)'''

with conn:
    # cur.execute(sql, ('teste', 'teste@teste', 1, 'teste.com', 'A'))
    cur.executemany(sql, data)

conn.close()
 
