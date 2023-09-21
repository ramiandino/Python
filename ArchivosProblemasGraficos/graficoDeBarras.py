import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ArchivosProblemasGraficos\\coflaIngresos.csv")

#Creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

totalIngresos = df['ingresos'].sum()  #Nos suma todos los datos del valor de ingresos.

#Mostrando el total
print(f'El total de ingresos es de: ${totalIngresos} USD')

#Mostrando el grafico.
plt.show()