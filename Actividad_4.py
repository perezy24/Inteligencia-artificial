import pandas as pd

#Creamos el Dataframe, con las dos variables "PUNTO_A" y "PUNTO_B"
#_________________________
recorrido = pd.DataFrame({'PUNTO_A':[16, 8, 12],
                               'PUNTO_B':[8, 4, 8],
                               })

#Creamos nuestra formula manhattan y la aplicamos a nuestros dos puntos
#_________________________
def distancia(a, b):
    return sum(abs(a - b))
  
print(distancia(recorrido.iloc[0], recorrido.iloc[1])) # Distancia de 12
print(distancia(recorrido.iloc[0], recorrido.iloc[2])) # Distancia de 4
