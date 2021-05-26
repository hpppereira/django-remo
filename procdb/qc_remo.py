"""
Qualificação dos dados da REMO
Henrique Pereira
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')


# filename = 'CF01_201602_BMOP05_REMO'
# filename = 'CF01_201611_BMOP05_REMO'
filename = 'CF03_201606_BMOP06_REMO'


def uv2id(ndr_ucomp, ndr_vcomp, str_conv='cart'):

    # Intensidade vetorial.
    icomp = np.sqrt(ndr_ucomp ** 2 + ndr_vcomp ** 2)

    if str_conv == 'cart':
        # Direção vetorial na convenção CARTESIANA.
        dcomp = np.rad2deg(np.arctan2(ndr_vcomp, ndr_ucomp)) % 360.
    elif str_conv == 'meteo':
        # Direção vetorial na convenção METEOROLÓGICA.
        dcomp = (np.rad2deg(np.arctan2(ndr_ucomp, ndr_vcomp)) - 180.) % 360.
    elif str_conv == 'ocean':
        # Direção vetorial na convenção OCEANOGRÁFICA.
        dcomp = np.rad2deg(np.arctan2(ndr_ucomp, ndr_vcomp)) % 360.

    return icomp, dcomp


df = pd.read_table('data/' + filename + '.csv', sep=',',
    index_col='date', parse_dates=True)

if filename == 'CF01_201602_BMOP05_REMO':
    df = df['2016-02-23 17:00':'2016-06-21 18:00']

elif filename == 'CF03_201606_BMOP06_REMO':
    df = df['2016-06-24 00:00':'2016-10-01 23:00']

# subtitui dados e intensidade e direcao das
# correntes pelos dados brutos
elif filename == 'CF01_201611_BMOP05_REMO':
    df = df['2016-11-06':'2016-12-31']

    df.drop(labels=['dp_ax', 'err', 'hs_ax', 'tp_ax'], axis=1, inplace=True)

    df[['mag1','dir1']] = np.nan

    raw = pd.read_csv('data/dataframe_CF01_201611_ADCP_DPL1_003_1.csv',
                             index_col='date', parse_dates=True)

    u = raw['Eas1'].values
    v = raw['Nor1'].values

    i, d =  uv2id(u, v, str_conv='ocean')

    adcp = pd.DataFrame(index=raw.index)
    adcp['mag1'] = i
    adcp['dir1'] = d

    df['2016-11-05 17:00:00':adcp.index[-1]][['mag1', 'dir1']] = adcp[['mag1','dir1']]

    df['mag2'] = 0
    df['mag3'] = 0
    df['dir2'] = 0
    df['dir3'] = 0

df['ate'].loc[df.ate < 0] = np.nan
df['rh'].loc[df.rh < 0] = np.nan
df['bp'].loc[df.ate > 1030] = np.nan
df['tp'].loc[df.tp < 4] = np.nan

sbe = ['tsbe10', 'tsbe100', 'tsbe20', 'tsbe30', 'tsbe40', 'tsbe50', 'tsbe60',
       'tsbe70', 'tsbe80', 'tsbe90', 'tsup']

for m in ['mag1']:
    df[m].loc[df[m] > 1000] = np.nan
    df[m].loc[df[m] <= 0] = np.nan

for d in ['dir1']:
    df[d].loc[df[d] > 360] = np.nan
    df[d].loc[df[d] < 0] = np.nan

for s in sbe:
    df[s].loc[df[s] > 30] = np.nan
    df[s].loc[df[s] < 15] = np.nan

for c in df.columns:
    plt.figure()
    df[c].plot(title=c)
plt.show()

df.to_csv('data/' + filename + '_qc.csv', sep=',', na_rep='NaN', float_format='%.2f')