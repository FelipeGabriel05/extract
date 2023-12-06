import pdfplumber

with pdfplumber.open("CM Capital.pdf") as pdf:
    page = pdf.pages[0]
    all_text = ''
    texto = page.extract_text()
    for row in texto:
        all_text += texto
    row = all_text.split('\n')
    
    coluna_nota = page.crop((400, 65, page.width, 75))
    titulos_settings = {
        "vertical_strategy": "explicit",
        "explicit_vertical_lines": [440, 490, 526, 590]
    }
    titulos = coluna_nota.extract_table(titulos_settings)
    
    obj_titulo = {
        "tipo_nota": row[0],
        "Nr_nota": titulos[0][0],
        "Folha": titulos[0][1],
        "Data_pregao": titulos[0][2]    
    }
    
    linha_corretora1 = row[6].split()
    linha_corretora2 = row[8].split()
    coluna_corretora = page.crop((10, 100, 180, 120))
    corretora_settings = {
        "horizontal_strategy": "explicit",
        "explicit_horizontal_lines": [101, 110, 119]
    }
    corretora = coluna_corretora.extract_table(corretora_settings)
    
    obj_corretora = {
        "Corretora": row[5],
        "Backoffice_email": linha_corretora1[-4],
        "Ouvidoria_telefone": linha_corretora2[-4],
        "Ouvidoria_email": linha_corretora2[-1],
        "endereco_corretora": f"{corretora[0][0]} {corretora[1][0]}",
        "CNPJ_corretora": row[4],
        "Numero_da_corretora": row[7]
    }
    
    linha_cliente1 = row[12].split()
    linha_cliente2 = row[14]
    endereco_cliente = ''
    total = 0
    while total <= len(linha_cliente1) - 4:
        endereco_cliente += f" {linha_cliente1[total]}"
        total += 1

    obj_cliente = {
        "Cliente": row[11],
        "Endereco_cliente": f"{endereco_cliente} {linha_cliente2}",
        "numero_do_cliente": row[13],
        "CNPJ_ou_CPF": row[10]
    }
    
    coluna_negocios = page.crop((10, 190, page.width, 628))
    negocios_settings = {
        "vertical_strategy": "explicit",
        "explicit_vertical_lines": [18, 30, 125, 220, 240, 315, 430, 510, 595]
    }
    negocios = coluna_negocios.extract_table(negocios_settings)
    i = 0
    total_negocios = {}
    while i <= len(negocios) - 1:
        obj_negocios = {
            "C_V": negocios[i][0],
            "Mercadoria": negocios[i][1],
            "Vencimento": negocios[i][2],
            "Quantidade": negocios[i][3],
            "Preco_Ajuste": negocios[i][4],
            "Tipo_do_negocio": negocios[i][5],
            "Vlr_de_operacao_ajuste_DC": negocios[i][6],
            "Taxa_operacional": negocios[i][7]
        }
        total_negocios[f"negocio_{i}"] = obj_negocios
        i += 1
        
    coluna_inferior = page.crop((10, 628, page.width, 710))
    inferior_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "text",
        "explicit_vertical_lines": [ 39, 57, 110, 128, 180, 196, 201, 244, 250, 360,
    370, 479, 482, 594],
        "explicit_horizontal_lines": [635, 648, 654, 668, 675, 686, 696, 705]
    }
    
    dados = coluna_inferior.extract_table(inferior_settings)
    if len(dados) == 9:
        obj_resumo = {
            "Vendas_disponivel": dados[1][2],
            "Compra_disponivel": dados[1][6],
            "Vendas_opcoes": dados[1][8],
            "Compras_opcoes": dados[1][10],
            "Valor_dos_negocios": dados[1][11],
            "IRRF": dados[4][2],
            "Taxa_Corretora_Intermediacao": dados[4][6],
            "Taxa_Corretora_IMPLANT": dados[4][8],
            "Taxa_registro_BMeF": dados[4][10],
            "Taxa_registro_BMeF_emol": dados[4][11],
            "IRRF_day_Trade_projecao": dados[7][2],
            "Outros_custos": dados[7][4],
            "ISS": dados[7][6],
            "Ajuste_de_posicao": dados[7][8],
            "Ajuste_day_trade": dados[7][10],
            "Total_das_despesas": dados[7][11],
            "Outros": '',
            "IRRF_corretagem": '',
            "Total_Conta_Investimento": '',
            "Total_Conta_Normal": '',
            "Total_liquido": '',
            "Total_liquido_da_nota": ''
        }
    else:
        obj_resumo = {
            "Vendas_disponivel": dados[1][2],
            "Compra_disponivel": dados[1][6],
            "Vendas_opcoes": dados[1][8],
            "Compras_opcoes": dados[1][10],
            "Valor_dos_negocios": dados[1][11],
            "IRRF": dados[4][2],
            "Taxa_Corretora_Intermediacao": dados[4][6],
            "Taxa_Corretora_IMPLANT": dados[4][8],
            "Taxa_registro_BMeF": dados[4][10],
            "Taxa_registro_BMeF_emol": dados[4][11],
            "IRRF_day_Trade_projecao": dados[7][2],
            "Outros_custos": dados[7][4],
            "ISS": dados[7][6],
            "Ajuste_de_posicao": dados[7][8],
            "Ajuste_day_trade": dados[7][10],
            "Total_das_despesas": dados[7][11],
            "Outros": dados[10][0],
            "IRRF_corretagem": dados[10][2],
            "Total_Conta_Investimento": dados[10][6],
            "Total_Conta_Normal": dados[10][8],
            "Total_liquido": dados[10][10],
            "Total_liquido_da_nota": dados[10][11]
        }
    
    informacoes_corretagem = {
        "info1": row[-10],
        "info2": row[-9],
        "info3": row[-8],
        "info4": row[-7],
        "info5": row[-6],
        "info6": f"{row[-5]} {row[-4]} {row[-3]}",
        "info7": f"{row[-2]} {row[-1]}"
    }
    
    templateCapital = {
        "Titulo": obj_titulo,
        "Corretora": obj_corretora,
        "Cliente": obj_cliente,
        "Negocios": total_negocios,
        "Resumos_dos_negocios": obj_resumo,
        "Informacao_corretagem": informacoes_corretagem
    }
    print(templateCapital)