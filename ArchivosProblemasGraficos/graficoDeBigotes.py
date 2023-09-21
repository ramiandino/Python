import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ArchivosProblemasGraficos\\bigotes.csv")

#Creando el grafico
sns.boxplot(x="categoria",y="valor",data=df)

#Mostrando el grafico.
plt.show()