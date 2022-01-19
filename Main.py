import sys, os

from pandas import *
import pandas as pd
from numpy import *
import random
import re
from sys import *

# ubicacion = input(str("Hola para leer tu archivo indicame la direccion y el archivo como tal y su extension: "))

df = pd.read_excel("C:/Users/vdgp_/OneDrive/Escritorio/dataframe.xlsx", sheet_name=0)


def ZeroR():
    iter = int(input("Numero de iteraciones: "))
    CountTest = 0                           #CONTADOR DE FILAS DE PRUEBA
    CountTrainer = 0                        #CONTADOR DE FILAS DE ENTRENAMIENTO
    ListTrainer = []                        #FILAS QUE SERAN DE ENTRENAMIENTO
    NumIteraciones = 0                      #CANTIDAD DE VECES QUE SE VA ITERAR LA FUNCION ZERO-R
    MaxRows = df.shape[0]                   #CANTIDAD MAXIMA DE FILAS DEL DATA FRAME
    CountTrainer = MaxRows * 0.7            #CANTIDAD DE FILAS DE ENTRENAMIENTO 70%
    CountTest = MaxRows - int(CountTrainer) #CANTIDAD DE FILAS DE PRUEBAS
    print("La cantidad de Filas del Dataframe es: ", df.shape[0])
    print("Cantidad de filas para Entrenamiento:  ", int(CountTrainer))
    print("Cantidad de filas para Pruebas:  ", int(CountTest))

    # CANTIDAD DE VECES QUE SE VA ITERAR EL ZERO-R
    for a in range(iter):

        print("\n \n \n _____________________Iteración numero ", str(a + 1), "_____________________")
        #SE CREA LA LISTA DE ENTRENAMIENTO CON NUMEROS RANDOM
        ListTrainer = random.sample(range(int(MaxRows)), int(CountTrainer))
        ListTest = range(int(MaxRows))
        ListTest = list(ListTest)

        # SE CREA UNA LISTA CON TODOS LOS VALORES Y SE ELIMINAN LOS DE LISTA DE ENTRENAMIENTO
        for x in ListTrainer:
            ListTest.remove(x)

        #CREAMOS DATAFRAME EN BASE EL INDICE DE LISTA DE ENTRENAMIENTO
        DataFrameTrainer = df.loc[ListTrainer]
        #CREAMOS DATAFRAME EN BASE EL INDICE DE LA LISTA DE PRUEBAS
        DataFrameTest = df.loc[ListTest]
        print("\n---Datos de Entrenamiento---")
        print(DataFrameTrainer)
        print("\n---Datos de Prueba---")
        print(DataFrameTest)
        #OBTENEMOS LOS NOMBRES DE LAS COLUMNAS
        columns_names = list(DataFrameTrainer.columns.values)
        #OBTENEMOS LA COLUMNA CLASE
        ClassName = columns_names.pop()
        #EN ESTE APARTADO IMPRIMIMOS LA CLASE QUE MAS SE REPITE LA CANTIDAD DE VECES QUE SE ENCUENTRA TANTO EN EL DATAFRAME DE PRUEBA Y ENTRENAMIENTO
        print("La Clase del DataFrame Entranamiento que mas se Repite Es: ",
              DataFrameTrainer[ClassName].value_counts().idxmax(),
              " numero de veces ", DataFrameTrainer[ClassName].value_counts().nlargest(n=1).values[0])
        print("La Clase ", DataFrameTrainer[ClassName].value_counts().idxmax(), " del DataFrame Pruebas se repite: ",
              len(DataFrameTest[DataFrameTest[ClassName] == DataFrameTrainer[ClassName].value_counts().idxmax()]),
              "  veces ")
        porcent = (int(len(
            DataFrameTest[
                DataFrameTest[ClassName] == DataFrameTrainer[ClassName].value_counts().idxmax()])) * 100) / int(
            len(ListTest))
        print("Porcentaje de Acierto: ", porcent, "%")
        print("Porcentaje de Errores: ", 100 - porcent, "%")
    os.system("PAUSE")
    print ("\n" * 100)

def OneR():
    iter = int(input("Numero de iteraciones: "))

    for a in range(int(iter)):
        TotalAciertos = 0                                   #TOTAL DE ACIERTOS
        Aciertos = 0                                        #OBTENER EL MAYOR DE ACIERTOS
        CountTest = 0                                       #CONTADOR DE FILAS DE PRUEBA
        CountTrainer = 0                                    #CONTADOR DE FILAS DE ENTRENAMIENTO
        ListTrainer = []                                    #LISTA DE INDICE DE ENTRENAMIENTO
        NumIteraciones = 0                                  #CANTIDAD DE ITERACIONES QUE HARA EL ONE-R
        ListAttribute = []                                  #TABLAS DE
        count = 0                                           #INDICE DE LA COLUMNA DE TABLA FRECUENCIA
        count2 = 0                                          #UBICAR EL NOMBRE DE LA TABLA DE ATRIBUTO
        TableFrecuency = []                                 #LISTA DE DATAFRAMES TABLAS DE FRECUENCIA
        columns_names = []                                  #OBTENER LOS NOMBRE DE LAS COLUMNAS
        BestTable = pd.DataFrame                            #MEJOR TABLA DE FRECUENCIa
        MaxRows = df.shape[0]                               #CANTIDAD MAXIMA DE FILAS DEL DATA FRAME
        BestTableName = []                                  #OBTENER EL NOMBRE DE LA TABLA
        CountTrainer = MaxRows * 0.7                        #CANTIDAD DE FILAS DE ENTRENAMIENTO 70%
        CountTest = MaxRows - int(CountTrainer)             #CANTIDAD DE FILAS DE PRUEBAS

        print("\n \n \n _____________________Iteración numero ", str(a + 1), "_____________________")
        print("La cantidad de Filas del Dataframe es: ", df.shape[0])
        print("Cantidad de filas para Entrenamiento:  ", int(CountTrainer))
        print("Cantidad de filas para Pruebas:  ", int(CountTest))

        #SE CREA LA LISTA DE ENTRENAMIENTO CON NUMEROS RANDOM
        ListTrainer = random.sample(range(int(MaxRows)), int(CountTrainer))
        ListTest = range(int(MaxRows))
        ListTest = list(ListTest)

        #SE CREA UNA LISTA CON TODOS LOS VALORES Y SE ELIMINAN LOS DE LISTA DE ENTRENAMIENTO
        for x in ListTrainer:
            ListTest.remove(x)

        #CREAMOS DATAFRAME EN BASE EL INDICE DE LISTA DE ENTRENAMIENTO
        DataFrameTrainer = df.loc[ListTrainer]
        #CREAMOS DATAFRAME EN BASE EL INDICE DE LA LISTA DE PRUEBAS
        DataFrameTest = df.loc[ListTest]
        print("\n---Datos de entrenamiento---")
        print(DataFrameTrainer.to_string())
        print("\n---Datos de prueba---")
        print(DataFrameTest.to_string())
        #TABLAS DE FRECUENCIA
        columns_names = list(DataFrameTrainer.columns.values)
        Clase = columns_names.pop()
        ClassName = Clase

        #AGREGANDO ETIQUETAS DE LOS ATRIBUTOS
        for a in columns_names:
            ListAttribute.append(DataFrameTrainer[a].unique().tolist())

        #SE CONSTRUYE LAS TABLAS DE FRECUENCIA
        for y in ListAttribute:
            TableFrecuency.append(pd.crosstab(index=DataFrameTrainer[columns_names[count]], columns=DataFrameTrainer[ClassName]))
            count += 1

        print("----------------TABLAS DE FRECUENCIA-------------------------")
        for x in range(0, len(TableFrecuency)):
            print("_____________________________________________________________")
            print("Tabla de Frecuencia #", str(x + 1), "\n", TableFrecuency[x])
            dftmp = pd.DataFrame(TableFrecuency[x])
            # SE IMPRIMEN LAS REGLAS DE CADA TABLA DE FRECUENCIA
            print("\n--Reglas-- \n", dftmp.idxmax(axis=1))
            # SE MUESTRAN LOS ACIERTOS DE CADA TABLA
            print("\nAciertos\n", dftmp.max(axis=1).sum())
            # SE SACA EL CONJUNTO CON MAS ACIERTOS
            if dftmp.max(axis=1).sum() > Aciertos:
                Aciertos = dftmp.max(axis=1).sum()
                BestTable = dftmp.idxmax(axis=1)
                BestTableName = columns_names[count2]
            count2 += 1

        print("La Mejor tabla es: \n", BestTable)
        print("\n____________Resultado_______________")

        #CALCULA EL TOTAL DE ACIERTOS CON DATAFRAME DE PRUEBA
        for a, b in BestTable.items():
            TotalAciertos += len(DataFrameTest[(DataFrameTest[BestTableName] == a) & (DataFrameTest[ClassName] == b)])
            print(a, "->", b, "Aciertos: ",
                  len(DataFrameTest[(DataFrameTest[BestTableName] == a) & (DataFrameTest[ClassName] == b)]))
        print("\nTotal de aciertos: ", TotalAciertos, " de ", len(DataFrameTest), "datos de prueba")
        porcent = (TotalAciertos * 100) / len(DataFrameTest)
        print("Porcentaje de aciertos: ", porcent, "%")
        print("Porcentaje de errores: ", 100 - porcent, "%")
    os.system("PAUSE")
    print("\n" * 100)


while True:
    print("1) Zero-R")
    print("2) One-R")
    print("0) Salir")
    op = input()

    if op == "1":
        ZeroR()

    elif op == "2":
        OneR()

    elif op == "0":
        break
