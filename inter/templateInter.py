import pdfplumber

with pdfplumber.open('notas 2020 janeiro a junho banco inter - OK.pdf') as pdf:
    page = pdf.pages[0]
    all_text = ''
    text = page.extract_text()
    for row in  text:
        all_text += text
    row = all_text.split('\n')
    
    total = 0
    endereco = ''
    text_address = row[1].split()
    while total <= len(text_address) - 2:
        endereco += f" {text_address[total]}"
        total += 1
    
    telefones = row[2].split()
    internet = row[3].split()
    campo_cnpj = row[4].split(":")
    obj_corretagem = {
        "Nome_da_corretora": row[0],
        "Endereco": endereco,
        "Telefone": f"{telefones[0]} {telefones[1]}",
        "Ouvidoria": f"{telefones[-3]} {telefones[-2]} {telefones[-1]}",
        "Internet": internet[1],
        "CNPJ": campo_cnpj[1] 
    }
    
    cliente = row[7].split()
    nome_total = 1
    nome_cliente = ''
    while nome_total <= len(cliente) - 2:
        nome_cliente += f"{cliente[nome_total]} "
        nome_total += 1
    obj_cliente = {
        "Numero_do_Cliente": cliente[0],
        "Nome_do_Cliente": nome_cliente,
        "CPF_CNPJ_CVM_COB": cliente[-1],
        "Endereco_Cliente": f"{row[8]} {row[9]}"
    }
    
    tipo_nota = row[5].split()
    
    banco = row[11].split()
    obj_banco = {
        "Banco": banco[0],
        "Agencia": banco[1],
        "Conta_Corrente": banco[2]
    }
    
    negocios_settings = {
        "vertical_strategy": "explicit",
        "explicit_vertical_lines": [44, 88, 102, 160, 265, 298, 358, 458, 540, 552]
    }
    coluna_negocios = page.crop((20, 185, page.width, 418))
    table_negocios = coluna_negocios.extract_table(negocios_settings)


    if table_negocios[0][0] == banco[0]:
        i = 2
        total = len(table_negocios) - 3
    else: 
        i = 0
        total = len(table_negocios) - 2
    lista_negocios = []
    while i <= total:
        negocio = {
            "Praca": table_negocios[i][0],
            "C_V": table_negocios[i][1],
            "Tipo_Mercado": table_negocios[i][2],
            "Especificacao_de_titulos": table_negocios[i][3],
            "OBS": table_negocios[i][4],
            "Quantidade": table_negocios[i][5],
            "Preco_liquidacao": table_negocios[i][6],
            "Compra_Venda": table_negocios[i][7],
            "D_C": table_negocios[i][8],
        }
        lista_negocios.append(negocio)
        i += 1
    
    a = 0
    total_negocios = {}
    while a <= len(lista_negocios) - 1:
        total_negocios[f"negocio_{a}"] = lista_negocios[a]
        a += 1
    
    
    lista_resumo = []
    total_linhas = -25
    while total_linhas <= -13:
        
        if row[total_linhas][-1] == 'C' or row[total_linhas][-1] == 'D':
            resumo = row[total_linhas].split()
        else:
            resumo = row[total_linhas].split()
            resumo.append('')
        
        lista_resumo.append(resumo)
        total_linhas += 1
    
    
    obj_resumo_negocios = {
        "Debentures": lista_resumo[0][1],
        "Vendas_a_vista": lista_resumo[1][3],
        "Compras_a_vista": lista_resumo[2][3],
        "Opcoes_Compras": lista_resumo[3][3],
        "Opcoes_Vendas": lista_resumo[4][3],
        "Operacoes_a_termo": lista_resumo[5][3],
        "Operacoes_a_Futuro": lista_resumo[6][3],
        "Valor_das_Oper_com_Til_Publ": lista_resumo[7][6],
        "Valor_das_Operacoes": lista_resumo[8][3],
        "Valor_do_Ajuste_pFuturo": lista_resumo[9][4],
        "IR_Sobre_Corretagem": lista_resumo[10][3],
        "IRRF_Sobre_Day_Trade": lista_resumo[11][4]
    }
    
    liquido =  f"{lista_resumo[12][0]} {lista_resumo[12][1]} {lista_resumo[12][2]}"
    obj_resumo_financeiro = {
        "Valor_Liquido_das_Operacoes_1": lista_resumo[0][-2],
        "Valor_Liquido_das_Operacoes_1_OBS": lista_resumo[0][-1],
        "Taxa_de_Liquidacao_2": lista_resumo[1][-2],
        "Taxa_de_Liquidacao_2_OBS": lista_resumo[1][-1],
        "Taxa_de_Registro": lista_resumo[2][-2],
        "Taxa_de_Registro_OBS": lista_resumo[2][-1],
        "Total_1_2_3_A": lista_resumo[3][-2],
        "Total_1_2_3_A_OBS": lista_resumo[3][-1],
        "Taxa_de_Termos_Opcoes_Futuro": lista_resumo[4][-2],
        "Taxa_de_Termos_Opcoes_Futuro_OBS": lista_resumo[4][-1],
        "Taxa_ANA": lista_resumo[5][-2],
        "Taxa_ANA_OBS": lista_resumo[5][-1],
        "Emolumentos": lista_resumo[6][-2],
        "Emolumentos_OBS": lista_resumo[6][-1],
        "Total_Bolsa_B": lista_resumo[7][-2],
        "Total_Bolsa_B_OBS": lista_resumo[7][-1],
        "Corretagem": lista_resumo[8][-2],
        "Corretagem_OBS": lista_resumo[8][-1],
        "ISS": lista_resumo[9][-2],
        "ISS_OBS": lista_resumo[9][-1],
        "IRRFs_operacoes_base": lista_resumo[10][-2],
        "IRRFs_operacoes_base_OBS": lista_resumo[10][-1],
        "Outras": lista_resumo[11][-2],
        "Outras_OBS": lista_resumo[11][-1],
        liquido: lista_resumo[12][-2],
        f"{liquido}_OBS": lista_resumo[12][-1],
    }
    
    dados1 = row[-11].split()
    dados2 = row[-10].split()
    dados3 = row[-9].split()
    dados4 = row[-8].split()
    dados5 = row[-7].split()
    obs_total = 0
    nome_obs = ''
    while obs_total <= len(dados1) - 7:
        nome_obs += f"{dados1[obs_total]} "
        obs_total += 1

    obj_OBS = {
        "Dados2": nome_obs,
        "DadosB": f"{dados1[-6]} {dados1[-5]} {dados1[-4]}",
        "DadosX": f"{dados1[-3]} {dados1[-2]} {dados1[-1]}",
        "Dados_Negocio": f"{dados2[0]} {dados2[1]} {dados2[2]} {dados2[3]}",
        "DadosA": f"{dados2[4]} {dados2[5]} {dados2[6]} {dados2[7]}",
        "DadosY": f"{dados2[8]} {dados2[9]} {dados2[10]} {dados2[11]} {dados2[12]}",
        "Dados8": f"{dados3[0]} {dados3[1]} {dados3[2]} {dados3[3]}",
        "DadosC": f"{dados3[4]} {dados3[5]} {dados3[6]} {dados3[7]} {dados3[8]} {dados3[9]} {dados3[10]} ",
        "DadosL": f"{dados3[11]} {dados3[12]} {dados3[13]}",
        "DadosD": f"{dados4[0]} {dados4[1]} {dados4[2]}",
        "DadosP": f"{dados4[3]} {dados4[4]} {dados4[5]} {dados4[6]}",
        "DadosT": f"{dados4[7]} {dados4[8]} {dados4[9]} {dados4[10]} {dados4[11]}",
        "DadosF": f"{dados5[0]} {dados5[1]} {dados5[2]}",
        "DadosH": f"{dados5[3]} {dados5[4]} {dados5[5]} {dados5[6]}",
        "Dados1": f"{dados5[7]} {dados5[8]} {dados5[9]}"
    }
    
    total_operacao = row[-6].split()
    total_i = 3
    observacao = ''
    while total_i <= len(total_operacao) - 1:
        observacao += f"{total_operacao[total_i]} "
        total_i += 1
    
    especificacao = row[-5].split('_')
    obj_info_inferior = {
        "Especificacoes_diversas": especificacao[0],
        "Observacao": observacao,
        "Informacoes_adicionais": f"{row[-3]} {row[-2]} {row[-1]}"
    }
    
    templateInter = {
        "Data_pregao": tipo_nota[2],
        "N_Nota": tipo_nota[5],
        "Folha": tipo_nota[7],
        "Corretora": obj_corretagem,
        "Cliente": obj_cliente,
        "Banco": obj_banco,
        "Negocios": total_negocios,
        "Resumo_dos_Negocios": obj_resumo_negocios,
        "Resumo_Financeiro": obj_resumo_financeiro,
        "Observacoes": obj_OBS,
        "Final_da_pagina": obj_info_inferior
    }
    print(templateInter)