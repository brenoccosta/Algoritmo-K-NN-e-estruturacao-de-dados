# # Algoritmo K-NN e estruturação de dados
# ## Limpeza e processamento dos dados

import pandas as pd

# ###### Importação do dataset teste de 15.120 amostras

treino = pd.read_csv(filepath_or_buffer='C:/.../train.csv')

# ###### Adição da categoria "Área"

treinoarea = treino
treinoarea = treinoarea.assign(Area=0)

for i in range(1, 5):
    treinoarea['Area'].loc[treinoarea[f'Wilderness_Area{i}'] == 1] = i

# ###### Adição da categoria "Solo"

treinosolo = treinoarea
treinosolo = treinosolo.assign(Solo=0)

for i in range(1, 41):
    treinosolo['Solo'].loc[treinosolo[f'Soil_Type{i}'] == 1] = i

# ###### Remoção das colunas excessivas

treinofinal = treinosolo
treinofinal = treinofinal.drop(columns=treinofinal.columns[11:55])
treinofinal = treinofinal.drop(columns=treinofinal.columns[2])
treinofinal = treinofinal.drop(columns=treinofinal.columns[0])

# ###### Normalização dos dados

tabelanormal = treinofinal

colunas = []
for coluna in tabelanormal.columns:
    colunas.append(coluna)

colunas.pop()
colunas.pop()
colunas.pop()

for coluna in colunas:
    tabelanormal[coluna] = (tabelanormal[coluna] - tabelanormal[coluna].min()) / (tabelanormal[coluna].max() - tabelanormal[coluna].min())

# ## Aplicação do algoritmo e geração das matrizes de confusão

import matplotlib.pyplot as plt

import sklearn as skl

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

# ###### Aplicação imediata do K-NN

especies = treino["Cover_Type"]

dados_train, dados_test, classes_train, classes_test = train_test_split(treino, especies, test_size= 0.2,
                                                                        stratify= treino["Cover_Type"])
model = KNeighborsClassifier(n_neighbors= i)
model.fit(dados_train, classes_train)
cm = confusion_matrix(classes_test, model.predict(dados_test))
plot_confusion_matrix(model, dados_test, classes_test)
plt.show()

# ###### Matriz de confusão após eliminação das colunas redundantes e da adição das colunas categóricas

dados_train, dados_test, classes_train, classes_test = train_test_split(treinofinal, treinofinal["Cover_Type"],
                                                                        test_size= 0.2, stratify = treinofinal["Cover_Type"])
model = KNeighborsClassifier(n_neighbors= i)
model.fit(dados_train, classes_train)
cm = confusion_matrix(classes_test, model.predict(dados_test))
plot_confusion_matrix(model, dados_test, classes_test)
plt.show()

# ###### Matriz de confusão após normalização

dados_train, dados_test, classes_train, classes_test = train_test_split(tabelanormal, tabelanormal["Cover_Type"], 
                                                                        test_size= 0.2, stratify = tabelanormal["Cover_Type"])
model = KNeighborsClassifier(n_neighbors= i)
model.fit(dados_train, classes_train)
cm = confusion_matrix(classes_test, model.predict(dados_test))
plot_confusion_matrix(model, dados_test, classes_test)
plt.show()
