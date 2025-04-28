
import pandas as pd
import glob
import os

caminho = './dados_brutos/'
arquivos_csv = glob.glob(os.path.join(caminho, '*.csv'))
bandas = {}

for arquivo in arquivos_csv:
    nome_banda = os.path.basename(arquivo).replace('.csv', '')
    bandas[nome_banda] = pd.read_csv(arquivo)
    print(f'Arquivo {nome_banda} carregado com shape {bandas[nome_banda].shape}')

bandas_necessarias = ['NDVI7', 'B3_7', 'B4_7']
for banda in bandas_necessarias:
    if banda not in bandas:
        raise Exception(f"Banda necessária {banda} não encontrada nos dados!")

dataset = bandas['NDVI7'].copy()
dataset = dataset.rename(columns={'valor': 'NDVI'})

dataset['B3'] = bandas['B3_7']['valor']
dataset['B4'] = bandas['B4_7']['valor']

dataset = dataset.dropna()

saida = './dataset_final.csv'
dataset.to_csv(saida, index=False)
print(f'Dataset final salvo em {saida}')
