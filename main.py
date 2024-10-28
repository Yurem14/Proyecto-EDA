# %% [markdown]
# # Notebook de desarrollo API juegos olimpicos 
# + Importando librerias

# %%
import pandas as pd
import numpy as np
from fastapi import FastAPI

# %% [markdown]
# + Instanciando FastAPI

# %%
app=FastAPI()

# %% [markdown]
# + Cargar Datasets

# %%
df=pd.read_parquet('Data/Dataset.parquet') 

# %% [markdown]
# + Funciones

# %% [markdown]
# + Funcion inicio

# %%

@app.get("/")
def index():
    return{"API:online"}

# %% [markdown]
# + Funcion medals

# %%
@app.get("/medals")
def medals():
    medals=df['Medal'].value_counts()
    return{medals.index[0]:medals.values[0], medals.index[1]:medals.values[1],medals.index[2]:medals.values[2]}

# %%
medals()

# %% [markdown]
# + Funcion medal_country

# %%
@app.get("/medal_country/{Pais}")
def medal_country(Pais:str):
    filtro=df[df['Team']==Pais]
    medallas=filtro['Medal'].value_counts()
    dic={}
    for i in range(len(medallas)):
        dic[medallas.index[i]]=int(medallas.values[i])
    return dic     

# %%
medal_country('Mexico')

# %%
@app.get("/medal_year/{Anio}") 
def medal_year(Anio:int):
    filtro=df[df['Year']==Anio]
    medallas=filtro['Medal'].value_counts()
    dic={}
    for i in range(len(medallas)):
        dic[medallas.index[i]]=int(medallas.values[i])
    return dic     

# %%
medal_year(2016)

# %%
@app.get("/athletes/{nombre}")
def athletes(nombre:str):
    filtro=df[df['Name']==nombre]
    dic={}
    if filtro==0:
        return {'Error':'Revise los datos ingresados'}
    dic['Nombre']=nombre
    dic['Sexo']=filtro['sex'].values[0]
    dic['Edad']=filtro['Age'].values[0]
    dic['Pais']=list(filtro['Team'].value_counts().index)
    dic['Juegos']=list(filtro['Games'].value_counts().index)
    dic['Evento']=list(filtro['Event'].value_counts().index)
    Medallas={}
    for i in range(len(filtro['Medal'].value_counts())):
        Medallas[filtro['Medal'].value_counts().index[i]]=filtro['Medal'].value_counts().values[i]
    dic['Medallas']=Medallas    
    return dic


