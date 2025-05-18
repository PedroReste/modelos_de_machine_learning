# first line: 1
@memory.cache  # Cache para evitar recomputações
def gerar_recomendacoes_para_um_cliente(cliente_id, modelo, cliente_features, produto_features,
                                        todos_produtos_set, clientes_info, produtos_info, produtos_comprados_dict, top_n):
    cliente_info = clientes_info.get(cliente_id)
    if cliente_info is None:
        return None

    produtos_comprados = produtos_comprados_dict.get(cliente_id, set())
    produtos_nao_comprados = todos_produtos_set - produtos_comprados
    if not produtos_nao_comprados:
        return None

    produtos_df = produtos_info.loc[produtos_info.index.intersection(produtos_nao_comprados)]
    if produtos_df.empty:
        return None

    # Adiciona dados do cliente
    df_recomendacoes = produtos_df.copy()
    df_recomendacoes.loc[:, 'customer_unique_id'] = cliente_id
    df_recomendacoes.loc[:, 'customer_state'] = cliente_info['customer_state']
    df_recomendacoes.loc[:, 'customer_city'] = cliente_info['customer_city']

    df_recomendacoes = df_recomendacoes.reset_index()

    # Converte para numpy para previsão mais rápida
    X_recomendacao = df_recomendacoes[cliente_features + produto_features].to_numpy()
    scores = modelo.predict_proba(X_recomendacao)[:, 1]
    df_recomendacoes['score'] = scores

    return df_recomendacoes.nlargest(top_n, 'score')
