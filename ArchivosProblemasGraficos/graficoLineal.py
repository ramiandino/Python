import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ArchivosProblemasGraficos\\pedos.csv")

#Creando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)

#Creando un punto en el momento de mas pedos.
plt.plot("01-09",17,"o")

#Mostrando el grafico.
plt.show()