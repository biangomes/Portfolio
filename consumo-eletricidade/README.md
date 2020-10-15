# consumo-eletricidade
- Este projeto foi baseado na aula do curso Escola de DataScience da Sigmoidal.



Temos um dataset intitulado `Electric_Production.csv` com 397 linhas. Este dataset possui duas colunas, `DATE` e `Value` e o seu delimitador é uma `,`.

Ao plotar o gráfico, percebemos que ele era crescente, pois os fundos e topos estavam cada vez mais altos; porém, aparentava ter muitos ruídos. Assim, optou-se por decompô-lo utilizando a biblioteca `statsmodels.tsa.seasonal` de `seasonal_decompose`. 

Foi possível ver o gráfico como uma combinação aditiva de outros três tipos de gráficos: `Trend`, `Seasonal` e `Resid`, sendo este os erros que a função não conseguiu extrair.

Ainda assim, não pareceu muito claro. Então foi utilizado outra técnica em que se melhorava a escala.