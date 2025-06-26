# Desempenho do Pysentimiento em Português

**O que você vai encontrar nessa pasta?**

Uma investigação para comprender a qualidade dos modelos de classificação de sentimento, emoções, ironia e discurso de ódio em português do Pysentimiento tem para tipos distintos de textos.

## **Passo a Passo Aplicado**


## **Como Funciona o Pysentimiento?**

**(REESTRUTURAR TEXTO DEPOIS)**

Os modelos utilizados para extrair sentimentos e emoções são originados da biblioteca **[Pysentimiento](https://github.com/pysentimiento/pysentimiento)**. Essa lib é baseada em modelos transformer **BERT** (Bidirectional Encoder Representations from Transformers) da Google que são estruturados em três pontos principais:
- **Bidirecional**: entende uma palavra com base nas palavras à esquerda e à direita ao mesmo tempo.
- **Pré-treinado**: treinado em tarefas como preencher palavras e prever se uma frase segue logicamente a outra.
- **Fine-tunável**: pode ser adaptado a tarefas específicas como análise de sentimento, classificação, etc.

No caso específico do Pysentimiento, é utilizado modelos BERT adptados que foram pré-treinados com bases textuais específicas (como tweets ou comentários curtos) em diversos idiomas (incluindo o português) e ajustados para ações específicas, como a classificação de sentimentos e emoções, e detecção de ironia e discurso de ódio.

## **Resultados Encontrados**


## **Considerações Finais**