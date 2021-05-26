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
df = pd.read_excel('data/tabela_equipe_REMO.xlsx', sep=',')

# subsitui palavras por indices do banco (verificar no sqlite browser o ID)
df.replace(to_replace='UFRJ', value=1, inplace=True)
df.replace(to_replace='UFBA', value=2, inplace=True)
df.replace(to_replace='Petrobras', value=3, inplace=True)
df.replace(to_replace='CHM', value=5, inplace=True)
df.replace(to_replace='ATLANTIS', value=6, inplace=True)
df.replace(to_replace='IEAPM', value=7, inplace=True)
df.replace(to_replace='University of Reading', value=8, inplace=True)
df.replace(to_replace='Mercator Ocean', value=9, inplace=True)
df.replace(to_replace='CMCC', value=10, inplace=True)
df.replace(to_replace='NERSC', value=11, inplace=True)
df.replace(to_replace='IAP/CAS', value=12, inplace=True)
df.replace(to_replace='USP', value=13, inplace=True)
df.replace(to_replace='TENDRAL', value=14, inplace=True)

df.replace(to_replace='Coordenador', value=u'A', inplace=True)
df.replace(to_replace='Pesquisador', value=u'B', inplace=True)
df.replace(to_replace='Aluno Pós-Graduação', value=u'C', inplace=True)
df.replace(to_replace='Aluno Graduação', value=u'D', inplace=True)
df.replace(to_replace='Técnico', value=u'E', inplace=True)
df.replace(to_replace='Pesquisador Egresso', value=u'F', inplace=True)
df.replace(to_replace='Colaborador Externo', value=u'G', inplace=True)

# list of tuples
data = [tuple([df.iloc[i][0], df.iloc[i][1], int(df.iloc[i][2]),
        df.iloc[i][3], df.iloc[i][4]]) for i in range(len(df))]

try:
    conn = sqlite3.connect('../db.sqlite3')
    conn.text_factory = str
except Error as e:
    print(e)

cur = conn.cursor()

# delete from your_table;
# delete from sqlite_sequence where name='your_table';
    
sql = ''' INSERT INTO remo_person(name,email,institution_id,lattes,position)
          VALUES (?,?,?,?,?)'''

with conn:
    # cur.execute(sql, ('teste', 'teste@teste', 1, 'teste.com', 'A'))
    cur.executemany(sql, data)

conn.close()
 
