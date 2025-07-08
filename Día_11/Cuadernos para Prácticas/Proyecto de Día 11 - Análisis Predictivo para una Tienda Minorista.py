import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

ruta = 'Ventas.csv'
df_ventas = pd.read_csv(ruta)
df_ventas

df_ventas.info()

df_ventas.describe()

fig, ax = plt.subplots()
ax.scatter(df_ventas['DíaDeLaSemana'], df_ventas['Ventas'])
ax.set_title('Ventas por dia de la semana')
ax.set_xlabel('Dia de la semana')
ax.set_ylabel('Cantidad de ventas del dia');

dias_festivos = df_ventas.drop(['Promociones', 'Ventas'], axis=1)
dias_festivos

X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(dias_festivos, df_ventas['Ventas'], train_size=0.9, random_state=42)

modelo = LogisticRegression()

modelo.fit(X_entrena, y_entrena)

modelo.score(X_prueba, y_prueba)
modelo.score(X_prueba, y_prueba)