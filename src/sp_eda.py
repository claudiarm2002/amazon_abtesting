import pandas as pd

def eda_preliminar(df):
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
