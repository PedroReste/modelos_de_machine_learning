# Feature Selection para dezenas de Features

## **O que você vai encontrar aqui?**

Nessa pasta é apresentado algumas formas de realizar *feature selection* para momentos que um dataset é vasto, se tornando inviável realizar análises exploratórias e verificar variável por variável. Em um post no [Medium]() é explicando o conceito de cada técnica de forma mais aprofundada enquanto aqui é apresentado todo o processo dentro de um script.

**Quais métodos foram abordados?**
- Filtro por quantidade de missing data
- Variância mínima
- Correlação Alta entre Features
- Recursive Feature Elimination

## **Qual foi resultado encontrado?**

A princípio para esse dataset não houve um ganho consideravél aplicando essas técnicas quando observados os resultados do erro quadrado médio e o R². Talvez em outros dataset seja mais efetivo, dependedo do contexto dos dados aonde essas ténicas forem aplicadas.

**Erro quadrado médio**
- **Sem nenhum tratamento adicional:** 842632962.4154353
- **Variância mínima:** 833833587.0615345
- **Correlação alta entre features:** 882726593.6872934
- **Variância e Correlação:** 834004939.0052686
- **RFE:** 957543952.2998086

**R²**
- **Sem nenhum tratamento adicional:** 0.8901
- **Variância mínima:** 0.8912
- **Correlação alta entre features:** 0.8849
- **Variância e Correlação:** 0.8912
- **RFE:** 0.8751