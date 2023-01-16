# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 17:37:38 2022

@author: Felipe Henao
"""

import requests
import xml.etree.ElementTree as ET
import pandas as pd

#non_connected.csv
#IP_Estaciones.csv
df_ips = pd.read_csv(r"IP_Estaciones.csv",
                     delimiter = ';', index_col=0)
output_dataframe = pd.DataFrame()
non_connected = pd.DataFrame()
tp = pd.Timestamp.now()  # Marca de tiempo

for EMRI in df_ips.index:
    EMRI_df = pd.DataFrame(index=[tp],
                           columns=pd.MultiIndex.from_product([[EMRI],
                                                               ['Battery', 
                                                                'Signal', 
                                                                'Storage', 
                                                                'historial datos',
                                                                'Observ']]))
    try:
        xml_str = requests.get('http://'+ df_ips.at[EMRI, 'IP'] +'/pub/GetStatus.asp',
                               timeout=4).text
        xml_tree = ET.fromstring(xml_str)
        if xml_tree[3].text == '0':
            print(f'La estacion {EMRI} conecto.')
        else:
            print(f'La estacion {EMRI} conecto pero no esta midiendo')
        EMRI_df.loc[tp, (EMRI, 'Battery')] = xml_tree[4].text + '%'
        EMRI_df.loc[tp, (EMRI, 'Signal')] = int(xml_tree[13].text)
        EMRI_df.loc[tp, (EMRI, 'Storage')] = round(int(xml_tree[9].text)/1000-0.6,1)
        if xml_tree[7].text == '0':
            EMRI_df.loc[tp, (EMRI, 'Observ')] = 'ninguna'
        else:
            EMRI_df.loc[tp, (EMRI, 'Observ')] = 'error por chequeo electrico'
        output_dataframe = pd.concat([output_dataframe, EMRI_df], axis=1)
    except:
        print(f'La estacion {EMRI} no conecto.')
        EMRI_df.loc[tp, (EMRI, 'Battery')] = ''
        EMRI_df.loc[tp, (EMRI, 'Signal')] = ''
        EMRI_df.loc[tp, (EMRI, 'Storage')] = ''
        EMRI_df.loc[tp, (EMRI, 'Observ')] = ''
        output_dataframe = pd.concat([output_dataframe, EMRI_df], axis=1)
        non_connected.loc[EMRI, 'IP'] = df_ips.at[EMRI, 'IP']

output_dataframe.to_excel('revision_estaciones.xlsx')
non_connected.to_csv('non_connected.csv', sep=';')