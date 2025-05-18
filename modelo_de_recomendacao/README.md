# Modelo de Recomendação de Produtos
**O que você vai encontrar nessa pasta?** \
Uma aplicação de machine learning para recomendar novos produtos para clientes de um e-commerce. Esses clientes já estão sem fazer uma nova compra a mais de 30 dias, mas ainda estão na janela de clientes que poderiam voltar para realizar uma nova compra - abaixo de 90 dias desde a última compra realizada. \
O modelo de machine learning será aplicado para entender as caracterísitcas dos usuários e dos produtos disponíveis nas bases desse e-commerce para gerar novas recomendações de produtos para esses clientes que serão impactados nas ações de marketing, aumentando a possibildiade desses clientes impactados de converterem com essas recomendações.

  ## Resumo do Material
A base de dados utilizada nessa pasta é originária do [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), que contém datasets sobre dados de um e-commerce brasileiro que utiliza soluções de e-commmerce da **Olist**, nesses datasets é possível encontrar informações relacionadas aos pedidos feitos, carecterísticas dos clientes, carecterísticas dos produtos, avaliação dos pedidos e outras informações relevantes.\
A intenção inicial do material era desenvolver um modelo de recomendação com base no histórico de pedidos e avaliações, mas como foi encontrado na parte 01 da análise exploratória, essas bases não há tantos clientes que realizaram várias compras. Por conta disso, foi necessário alterar o tipo de modelo para um com base em caracterísiticas de usuários e produtos para gerar recomendações.

**Etapas Aplicadas**
- Análise exploratória dos dados
- Geração de um dataset com características de usuários e produtos de compras realizadas
- Geração de uma amostra negativa por similaridade
- Aplicação de tratamentos de pré-processamento
- Treino de modelos de Random Forest, XGB, LGBM e CatBoost
- Avaliação de desempenho dos modelos
- Seleção dos clientes a serem impactados
- Aplicação do melhor modelo para recomendação
- Exportação da base de clientes e produtos recomendados

**Insights da Análise Exploratória**
- 90% dos pedidos tem um único produto e 96% possuem um único produto ou mais de um produto igual.
- Como 96% da base consiste em pedidos com o mesmo produto, será possível utilizar o order_id como uma proxy para o produto, já que as bases da Olist não possuem a avalição feita por produto, mas apenas por pedido.
- Aproximadamente 97% dos usuários fizeram um único pedido.
- Numa escala de nota de 1 a 5: aproximadamente 12% dos usuários deram uma nota baixa para o produto (1 ou 2), 8% deram uma nota mediana (3) e 80% deram uma nota alta (4 ou 5).
- Mesmo com 97% dos usuários tendo um pedido, vamos no modelo testar tanto o valor absoluto da média de notas quanto os valores normalizado.

**Desempenho de Cada Modelo**
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Modelo</th>
      <th>AUC-ROC</th>
      <th>LogLoss</th>
      <th>F1-Score</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>Average Precision</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>RandomForest</th>
      <td>0.701796</td>
      <td>0.649723</td>
      <td>0.640039</td>
      <td>0.682282</td>
      <td>0.602721</td>
      <td>0.748785</td>
    </tr>
    <tr>
      <th>XGBoost</th>
      <td>0.718397</td>
      <td>0.609830</td>
      <td>0.642172</td>
      <td>0.678783</td>
      <td>0.609308</td>
      <td>0.750327</td>
    </tr>
    <tr>
      <th>LightGBM</th>
      <td>0.701869</td>
      <td>0.627845</td>
      <td>0.617522</td>
      <td>0.681597</td>
      <td>0.564458</td>
      <td>0.736580</td>
    </tr>
    <tr>
      <th>CatBoost</th>
      <td>0.724814</td>
      <td>0.607961</td>
      <td>0.650163</td>
      <td>0.681721</td>
      <td>0.621398</td>
      <td>0.754333</td>
    </tr>
  </tbody>
</table>
</div>
