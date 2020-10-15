# Aula 002 - Material de apoio ao notebook

### 1. Introdução

As **Séries Temporais** são séries em que a variável importante é o **tempo**. Uma definição mais formal, de acordo com o [Portal Action](http://www.portalaction.com.br/series-temporais/introducao) é:

> Uma série temporal é um conjunto de observações ordenadas no tempo. Alguns exemplos de séries temporais são:
> - Valores diários de poulição em uma cidade;
> - Valores mensais de temperaturas registradas em uma cidade;
> - Índices diários da Bolsa de Valores de São Paulo;
> - Acidentes ocorridos nas rodovias da cidade de São Paulo durante um mês.

> Os modelos utilizados para descrever séries temporais são processos estocásticos, ou seja, processos **controlados por leis probabilísticas**.

É importante dizer que quanto mais longe tentar prever algo, maior será o grau de incerteza associado.

### 2. Naive Approach
O modelo **Naive Approach** ou modelo "ingênuo" é um modelo baseado no evento imediatamente anterior. Ele parte da premissa de que "o futuro repetirá o passado" servindo como uma *baseline* inicial. **Baselines** são métricas comparativas.

Na prática, o método Naive projeta o último valor para o futuro. Também existe o **Naive Sazonal** que projeta o último **período**.

Vamos utilizar o exemplo do professor Carlos. Considere uma **fatura de luz** em que os últimos valores foram:

- Março: R\$ 500,00
- Abril: R\$ 800,00
- Maio: R\$ 2.000,00

Seguindo o método Naive teríamos que a previsão para o valor da fatura de luz do mês de junho seria de R\$ 2.000,00.

O dataset utilizado na aula foi o `Electric_Production.csv`.

#### 2.1 Explicando as células

```
train = df[df.index <= '2012-8-1']
valid = df[df.index > '2012-8-1']
y_hat = valid.copy()
 ```

Na célula acima, dividimos o dataset em duas partes: uma **antes** de 01/08/2012 e outro **depois** de 01/08/2012. Esta separação, de acordo com o professor Carlos, foi para fins didáticos. A variável `y_hat = valid.copy()` armazena uma cópia da variável valid.

Vejamos a próxima célula:

```
y_hat['naive'] = train.iloc[-1].values[0]
plotar train e valid
fig, ax = plt.subplots(figsize=(8,4))
train.plot(ax=ax)
valid.plot(ax=ax)
y_hat['naive'].plot(ax=ax)
plt.show()
```

- `y_hat['naive'] = train.iloc[-1].values[0]` -> cria uma coluna chamada 'naive' e recebe o último valor do conjunto de treino. Para não retornar array, coloca índice 0 em `values`. O `y_hat` é um **df** que **armazena as previsões**.

- `fig, ax = plt.subplots(figsize=(8,4))` -> é um método OOI (Object-Oriented Interface) de plotar gráficos no formato de orientação a objetos.

- `train.plot(ax=ax)` -> vai criar um subgráfico com o conj. treino

- `valid.plot(ax=ax)` -> vai cirar outro subgráfico com o conj. validaçao

- `y_hat['naive'].plot(ax=ax)` -> cria outro subgráfico com a coluna `naive` do `y_hat`.

O resultado do gráfico plotado acima será uma reta localizada no mesmo $ y_{n-1} $ até que uma nova amostra seja inserida.

### 3. Média Móvel
As médias móveis são muito utilizadas no cotidiano. Os jornais televisivos costumam usá-la quando se referem aos números de mortalidade ou infectados pela Covid-19. No mercado financeiro, ela é muito utilizada pelos adeptos a análise gráfica, técnica e/ou *price action*. 
A média móvel é um indicador móvel que reflete a média em um determinado período `N`. Ou seja, uma média móvel de `N` períodos calcula a média aos `N` períodos anteriores.

**Considere o exemplo da fatura de energia:** suponhamos que queiramos estimar a próxima fatura com base nas sete últimas. Vejamos o código.

#### 3.1 Explicando as células

```
train.Value.rolling(7).mean()
```
A célula acima pega o conjunto de trein e calcula a média (`mean()`) e plota uma média móvel (`rolling`) de sete períodos (`(7)`).

```
y_hat['m7'] = train.Value.rolling(7).mean().iloc[-1]

fig, ax = plt.subplots(figsize=(8,4))
train.plot(ax=ax)
valid.plot(ax=ax)
y_hat['m7'].plot(ax=ax)
plt.show()
```

No nosso dataframe `y_hat` criamos uma nova coluna chamada `m7` que irá receber justamente o valor da média móvel em 7 períodos contando a partir do último no conjunto de treino. Em seguida, com a mesma técnica de OOI é plotado utilizando a média móvel de 7 períodos.

No gráfico, o que você terá é o seguinte: a 'reta' iniciará a partir do valor calculado pela média dos últimos 7 períodos e se deslocará iterando sobre estes valores. Porém, no gráfico a inclinação é muito pequena.