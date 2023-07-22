#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Electric_Vehicle_Population_Data.csv', encoding='latin-1')


# In[27]:


marcas = df['Make'].value_counts()


# In[ ]:





# In[28]:


print(marcas)


# In[29]:


plt.figure(figsize=(10, 6))  # Tamaño de la figura
marcas.plot(kind='bar')  # Tipo de gráfica de barras
plt.xlabel('Make')  # Etiqueta del eje x
plt.ylabel('marcas')  # Etiqueta del eje y
plt.title('Frecuencia de valores en mi_columna')  # Título del gráfico
plt.xticks(rotation=90)  # Rotar las etiquetas del eje x para mayor legibilidad


# In[30]:


df.loc[df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'Clean Alternative Fuel Vehicle Eligible', 'Clean Alternative Fuel Vehicle (CAFV) Eligibility',] = 0 

df.loc[df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'Not eligible due to low battery range', 'Clean Alternative Fuel Vehicle (CAFV) Eligibility',] = 1 
12


# In[33]:


print(df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].head(12))

clean = df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].value_counts()


# In[42]:


plt.figure(figsize=(12, 6))  # Tamaño de la figura
sns.countplot(x='Make', hue='Clean Alternative Fuel Vehicle (CAFV) Eligibility', data=df)  # Gráfico de barras apiladas
plt.xlabel('Fabricante')  # Etiqueta del eje x
plt.ylabel('Cantidad')  # Etiqueta del eje y
plt.title('Elegibilidad de CAFV por Fabricante')  # Título del gráfico
plt.xticks(rotation=90)  # Rotar las etiquetas del eje x para mayor legibilidad
plt.legend(title='CAFV Eligibility', labels=['Clean Eligible', 'Not Eligible', "Unkown"])


# In[37]:


plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.boxplot(x='Make', y='Electric Range', data=df)  # Gráfico de cajas
plt.xlabel('Fabricante')  # Etiqueta del eje x
plt.ylabel('Rango Eléctrico')  # Etiqueta del eje y
plt.title('Distribución del Rango Eléctrico por Fabricante')  # Título del gráfico
plt.xticks(rotation=90)  # Rotar las etiquetas del eje x para mayor legibilidad

# Mostrar la gráfica
plt.tight_layout()  # Ajustar el diseño para evitar recortes de etiquetas
plt.show()


# In[43]:


plt.figure(figsize=(10, 8))  # Tamaño de la figura
sns.heatmap(df[['Electric Range', 'Base MSRP']].corr(), annot=True, cmap="coolwarm", center=0, fmt=".2f")  # Heatmap
plt.title('Matriz de Correlación entre Electric Range y Base MSRP')  # Título del gráfico

plt.show()


# In[ ]:




