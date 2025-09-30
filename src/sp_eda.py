# Tratamiento de datos
import pandas as pd

def eda_preliminar(df):
    """
    Realiza un análisis exploratorio preliminar de un DataFrame de pandas.

    Este análisis incluye:
    - Muestra 5 filas aleatorias del DataFrame.
    - Información general del DataFrame (número de filas, columnas, tipos de datos).
    - Porcentaje de valores nulos por columna.
    - Número de filas duplicadas.
    - Distribución de valores para columnas categóricas (tipo 'object').

    Parameters:
    df (pd.DataFrame): El DataFrame a analizar.

    Returns:
    None: La función imprime los resultados directamente.
    """

    display(df.sample(5))

    print('--------')
    print(f'Shape: {df.shape}')

    print('--------')
    print('\nInfo:')
    display(df.info())

    print('--------')
    print('Nulls (%):')
    display(df.isnull().mean()*100)

    print('--------')
    print(f'Duplicated rows: {df.duplicated().sum()}')

    print('--------')
    print('Categorical freq:')
    for col in df.select_dtypes(include='object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('***')

    print('--------')
    print('Numeric Statistics:')
    display(df.describe().T)

