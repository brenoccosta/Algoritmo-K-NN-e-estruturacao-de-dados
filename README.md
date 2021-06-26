# Algoritmo K-NN e estruturação de dados

O *dataset* [Forest Cover Type Prediction | Kaggle](https://www.kaggle.com/c/forest-cover-type-prediction) foi objeto de uma competição em 2015 cujo objetivo era desenvolver o melhor algoritmo que aplicasse a tarefa de classificação no banco de dados da **Floresta Nacional Roosevelt**, no estado do Colorado - EUA. Tal banco de dados é composto por 15.120 entradas, cada uma com cinquenta e seis atributos, sendo vencedor aquele que melhor classificasse as outras 565.892 entradas, indisponíveis aos internautas mesmo após o encerramento.
Ele consiste em recortes de 30mx30m da floresta cujo intuito é automatizar a identificação da espécie predominante naquele terreno, trazendo informações tais como elevação/altitude, inclinação, distância da fonte de água mais próxima, região, tipo de solo, dentre outros. São sete espécies no total e cada uma possui o mesmo número de entradas, *i.e.*, 2.160.

## Aplicação imediata do K-NN

O *dataset* disponibilizado carece de uma estruturação inteligente das informações embutidas. Quase que por curiosidade, a aplicação imediata do K-NN fornece uma boa pista do quanto deve ser reprocessado o banco de dados antes de se prosseguir com o trabalho (**Figura 1**).

###### Figura 1
![Matriz de confusão do algoritmo K-NN aplicado ao *dataset* sem qualquer manuseio.](https://github.com/brenoccosta/Algoritmo-K-NN-e-estruturacao-de-dados/blob/afda61b6b3263e82db425c3d59a1d834a746d21d/%5BGit%5D%20K-NN%20Treino.png?raw=True)

> Observação: aplicou-se um teste de 20% da amostra e usou-se o método `stratify`, da função `train_test_split` da biblioteca `sklearn.model_selection`, para garantir que uma mesma quantidade amostral fosse retirada de cada categoria (espécie), uma vez que estão igualmente presentes no banco de dados.

Apenas as classes sete e quatro foram bem classificadas pelo algoritmo, com a cinco logo atrás, por tais espécies serem muito particulares, conforme pode ser visto [aqui](https://github.com/brenoccosta/Visualizacao-exemplo-de-analise-de-dados). Porém, quaisquer espécimes com características próximas às particularidades dessas três espécies foram enquadradas nessas classes, que apresentam mais de cem indivíduos erroneamente atribuídos. A exceção são as espécies um e dois que se confundem entre si devido a grandes semelhanças.

## Limpeza e processamento dos dados
### Limpeza

Apesar de composto por cinquenta e seis colunas, quarenta e quatro das mesmas são binárias, indicando a presença ou ausência de determinada característica, quatro reportando às regiões e quarenta, ao solo. Enquanto as regiões levantam poucas dúvidas quanto ao caráter categórico da informação, o solo pode ser menos intuitivo. Contudo, verificar-se-á que sempre em trinta e nove colunas constará 0, enquanto que em uma, 1, pelo tipo de solo ser sua composição, não seus componentes.

Procedeu-se à adição de duas novas colunas categóricas, variando de 1 a 4 e de 1 a 40, para a região e solo da amostra, e excluiu-se os valores binários, a inclinação em azimute -- redundante da inclinação em graus -- e o "identificador" da amostra. Este correspondia a uma série uniforme de números naturais cuja função era indexar o dado: exatamente o número de linha de uma tabela.

Após essa etapa, a nova tabela contava tão somente com doze colunas, das quais três eram categóricas (lembrando que a primeira categoria era de espécie), e o novo K-NN apresentou melhoras significativas (**Figura 2**):

###### Figura 2
![Matriz de confusão após a limpeza de dados.](https://github.com/brenoccosta/Algoritmo-K-NN-e-estruturacao-de-dados/blob/afda61b6b3263e82db425c3d59a1d834a746d21d/%5BGit%5D%20K-NN%20Treino%20Final.png?raw=True)

A reorganização dos dados, da supressão de ruídos (como angulação em azimute e em graus) e de dados que não eram informação (como a coluna identificadora) levou o algoritmo K-NN a uma melhora chocante de se ver, tanto pela simplicidade da reestruturação, quanto pela simplicidade do algoritmo, que com alta eficácia cumpre com o que lhe fora solicitado.

### Normalização

Visando uma performance ainda mais alavancada, as nove colunas não-categóricas foram normalizadas e uma nova matriz de confusão, gerada (**Figura 3**):

###### Figura 3
![Matriz de confusão com tabela normalizada](https://github.com/brenoccosta/Algoritmo-K-NN-e-estruturacao-de-dados/blob/ec02b2038d887a0fa1ff4fba173f88f2954855d8/Matrizes/%5BGit%5D%20K-NN%20Tabela%20Normal.png?raw=True "Tabela normalizada")

Devido à alta precisão, avanços milimétricos são mais difíceis de se alcançar. Por pequena que pareça a diferença, simplesmente haver basta para que seja preferível a normalização à não-normalização dos dados neste caso.

## Conclusão

Um algoritmo simples como o K-NN foi, em dois passos, eficiente na classificação de, pelo menos, 99% dos exemplares de seis das sete classes, e ao menos 98% eficiente na uma restante. Tendo em vista o caráter competitivo internacional do *dataset*, a rapidez e a simplicidade das etapas percorridas para alcançar-se tamanha precisão evidencia como, mais do que uma inteligência artificial poderosa, vale uma pessoa inteligente por detrás da inteligência artificial.
