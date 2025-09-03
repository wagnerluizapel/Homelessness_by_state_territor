#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 09:14:50 2025

@author: wagnerapel
"""

import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import warnings
from warnings import filterwarnings

# Desativar cache para forçar recriação
@st.cache_data(ttl=0)  # ttl=0 desativa o cache
def load_data():
    return None  # Placeholder, pois não estamos carregando dados externos agora

# Configurar o backend do Matplotlib para ser compatível com Streamlit
import matplotlib
matplotlib.use('Agg')  # Usar backend 'Agg' para renderização não interativa

filterwarnings('ignore')
st.title("Homelessness Rates in Australia by State/Territory")

data = pd.read_csv(r'/Users/wagnerapel/teste/clean_csv.csv')


st.subheader("Homelessness Rates Table (per 10,000 residents)")
st.dataframe(data.reset_index(drop=True))


# ---- 2) Carregar dados geográficos ----
gdf = gpd.read_file("https://raw.githubusercontent.com/rowanhogan/australian-states/master/states.geojson")

# ---- 3) Mapping e criação da coluna State ----
mapping = {
    "New South Wales": "NSW",
    "Victoria": "Vic.",
    "Queensland": "Qld",
    "South Australia": "SA",
    "Western Australia": "WA",
    "Tasmania": "Tas.",
    "Northern Territory": "NT",
    "Australian Capital Territory": "ACT"
}


# Criar a coluna State ANTES do merge
gdf["State"] = gdf["STATE_NAME"].map(mapping)

# Agora fazer merge na coluna State que foi criada
gdf_merged = gdf.merge(data, on="State", how="left")

# SelectBox:
#st.sidebar.title("Choose an Year")
year = st.selectbox("Select the year", ['2006', '2011', '2016', '2021'], index=3)  # Default 2021


# Plotar o mapa
#st.subheader(f"Mapa de Taxas de Desabrigados - {year}")
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Verificar se a coluna do ano existe
if year in gdf_merged.columns:
    gdf_merged.plot(
        column=year,
        cmap="GnBu", alpha=0.7,
        linewidth=0.8,
        edgecolor="black",
        legend=True,
        ax=ax,
        missing_kwds={"color": "lightgrey", "label": "No data"}
    )

    # Adicionar rótulos dos nomes dos estados
    for idx, row in gdf_merged.iterrows():
        centroid = row['geometry'].centroid
        ax.annotate(text=row['STATE_NAME'], xy=(centroid.x, centroid.y),
                    xytext=(0, 0), textcoords='offset points', ha='center', va='center',
                    fontsize=8, color='black', fontweight='bold')

    plt.title(f"Map of homelessness rate per 10,000 people ({year})", fontsize=16, pad=20)
    plt.axis("off")

    # Exibir a figura no Streamlit
    st.pyplot(fig)
else:
    st.error(f"Coluna '{year}' não encontrada no DataFrame. Colunas disponíveis: {gdf_merged.columns.tolist()}")
