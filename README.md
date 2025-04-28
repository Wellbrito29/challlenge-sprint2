# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%"></a>
</p>

<br>

# 🌾 Challenge Ingredion - Sprint 2

## 📚 Nome do Grupo
Inova Fusca

## 👨‍🎓 Integrantes:
- [WELLIGTON NASCIMENTO DE BRITO - RM 552157](https://www.linkedin.com/company/inova-fusca)
- [CELESTE LEITE DOS SANTOS - RM 559312](https://www.linkedin.com/company/inova-fusca)
- [EDUARDO CARVALHO - RM 95585](https://www.linkedin.com/company/inova-fusca)
- [LUMA SANTOS DE OLIVEIRA - RM 560146](https://www.linkedin.com/company/inova-fusca)
- [RICARDO ARAÚJO DE OLIVEIRA - RM 561182](https://www.linkedin.com/company/inova-fusca)

## 👩‍🏫 Professores:
### Tutor(a)
- Nome do Tutor
### Coordenador(a)
- Nome do Coordenador

---

## 📜 Descrição do Projeto

Desenvolvimento de um modelo de Inteligência Artificial para **previsão de produtividade agrícola** utilizando dados históricos de imagens de satélite (NDVI) e bandas espectrais.

O projeto visa transformar dados brutos em **insights preditivos** e identificar padrões críticos para tomada de decisão no contexto do agronegócio.

---

## 🛠️ 1. Como a Solução Resolve o Problema

O projeto foi dividido nas seguintes etapas:

### a) Pré-processamento dos Dados
- Leitura dos arquivos brutos (`NDVI7.csv`, `B3_7.csv`, `B4_7.csv`).
- Limpeza dos dados: tratamento de valores nulos.
- Estruturação do dataset final (`dataset_final.csv`) para entrada no modelo de IA.

### b) Análise Exploratória
- Visualização temporal da variação do NDVI.
- Análise de correlação entre variáveis espectrais (NDVI, B3, B4) e produtividade.

### c) Modelagem Preditiva
- Treinamento do modelo **Random Forest Regressor**.
- Avaliação utilizando métricas **RMSE** e **R²** para validar a capacidade de previsão.

### d) Visualização de Resultados
- Gráficos gerados para demonstrar:
  - Evolução do NDVI.
  - Matriz de correlação entre variáveis.
  - Comparação entre produtividade real e prevista.

---

## 📂 2. Estrutura de Pastas

```
Challenge-Ingredion-Sprint2/
├── README.md
├── requirements.txt
├── Challenge_Ingredion_Sprint2.ipynb
├── monta_dataset.py
├── dataset_final.csv
├── dados_brutos/
│   ├── NDVI7.csv
│   ├── B3_7.csv
│   ├── B4_7.csv
├── images/
│   ├── ndvi_time_series.png
│   ├── correlation_matrix.png
│   ├── real_vs_predicted.png
└── src/
    ├── data_processing.py
    ├── model_training.py
    ├── model_evaluation.py
```

---

## 🔧 3. Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior
- Instalação das bibliotecas:

```bash
pip install -r requirements.txt
```

### Execução
1. Gerar o dataset final:
   ```bash
   python monta_dataset.py
   ```
2. Rodar o notebook:
   - `Challenge_Ingredion_Sprint2.ipynb`
   - Executar todas as células em sequência para gerar análises, treinar o modelo e salvar os gráficos.

---

## 📈 4. Resultados e Métricas

Após a construção do modelo e sua validação, foram obtidos os seguintes resultados:

| Métrica | Resultado |
|:---|:---|
| **RMSE (Root Mean Squared Error)** | **0.05** |
| **R² (Coeficiente de Determinação)** | **0.92** |

As métricas demonstram **alto desempenho preditivo**, com baixa margem de erro e alta capacidade de explicação da variabilidade da produtividade.

---

## 🧠 5. Análise dos Resultados

- **Random Forest** foi o modelo escolhido por ser robusto, lidar bem com variáveis correlacionadas e evitar overfitting.
- A variável **NDVI** apresentou forte correlação com a produtividade, reforçando seu valor como indicador agrícola.
- A análise gráfica Real vs Previsto evidenciou uma forte aderência entre as previsões e os valores reais.

---

## 🌱 6. Conclusão

O modelo de Inteligência Artificial desenvolvido foi **efetivo** em prever a produtividade agrícola com base em índices de vegetação e bandas espectrais:

- A acurácia alcançada indica que o modelo é confiável para aplicações práticas no agronegócio.
- **O R² de 0.92** mostra que o modelo é capaz de explicar 92% da variabilidade na produtividade.
- **O RMSE de 0.05** confirma a baixa margem de erro do modelo.

### 🔥 Melhorias Futuras
- Adicionar novas variáveis climáticas (precipitação, temperatura, umidade do solo).
- Implementar algoritmos mais avançados como **XGBoost** e **LightGBM**.
- Realizar validações cruzadas e tuning de hiperparâmetros para ganho adicional de performance.

---

## 🗃 7. Histórico de Lançamentos

| Versão | Data | Alterações |
|:---|:---|:---|
| 0.1.0 | 04/2025 | Versão inicial da Sprint 2 - Challenge Ingredion. |

---

## 📋 8. Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>