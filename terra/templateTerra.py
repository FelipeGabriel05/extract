import pdfplumber

with pdfplumber.open('Terra.pdf') as pdf:
    page = pdf.pages[0]
    all_text = ''
    text = page.extract_text()
    for row in text:
        all_text += text
    row = all_text.split('\n')
    
    tipo_nota = row[1].split()
    obj_nota = {
        "Nr_da_Nota": tipo_nota[0],
        "Data_pregao": tipo_nota[1]
    }
    
    telefones = row[4].split()
    internet = row[5].split()
    cnpj = row[6].split()
    carta = cnpj[-1]
    
    obj_corretora = {
        "Corretora": row[2],
        "Endereco": row[3],
        "Telefone": f"{telefones[1]} {telefones[2]} {telefones[3]}",
        "FAX": f"{telefones[-3]} {telefones[-2]} {telefones[-1]}",
        "Website": internet[-1],
        "CNPJ": cnpj[1],
        "Carta_Patente": carta 
    }
    
    linha8 = row[8].split()
    total = 0
    cliente = ''
    while total < len(linha8) - 1:
        cliente += f" {linha8[total]}"
        total += 1
    
    linha11 = row[11].split()
    
    coluna_cliente = page.crop((20, 160, page.width, 185))
    cliente_settings = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "explicit",
        "explicit_horizontal_lines": [170, 180]
    }
    table_cliente = page.extract_table(cliente_settings)
    obj_cliente = {
        "Nome_cliente": cliente,
        "CPF_CNPJ_CVM_COB": linha8[-1],
        "Endereco": row[9],
        "Codigo_cliente": linha11[-2],
        "Acessor": linha11[-1],
        "Agente_da_Compensacao": table_cliente[0][0],
        "Cliente": table_cliente[0][1],
        "Valor": table_cliente[0][2],
        "Custodiante": table_cliente[0][3],
        "C_I": table_cliente[0][4]
    }
    
    
    coluna_banco1 = page.crop((20, 185, page.width, 203))
    banco1_settings = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "explicit",
        "explicit_horizontal_lines": [195, 202]
    }
    table_banco1 = page.extract_table(banco1_settings)
    
    coluna_banco2 = page.crop((20, 204, page.width, 225))
    banco2_settings = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "explicit",
        "explicit_horizontal_lines": [215, 220]
    }
    table_banco2 = page.extract_table(banco2_settings)
    
    obj_banco = {
        "Banco": table_banco1[0][0],
        "Agencia": table_banco1[0][1],
        "Conta_Corrente": table_banco1[0][2],
        "Acionista": table_banco2[0][0],
        "Administrador": table_banco2[0][1],
        "Complemento_nome": table_banco2[0][2],
        "P_Vinc": table_banco2[0][3]
    }
    
    coluna_negocios = page.crop((20, 245, page.width, 290))
    negocios_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [30, 50, 102, 165, 220, 280, 360, 460, 480, 555],
        "explicit_horizontal_lines": [245, 285]
    }
    table_negocios = coluna_negocios.extract_table(negocios_settings)
    total_negocios = {}
    i = 0
    while i <= len(table_negocios) - 1:
        negocio = {
            "CV": table_negocios[i][0],
            "Mercadoria": table_negocios[i][1],
            "Vencimento": table_negocios[i][2],
            "Quantidade": table_negocios[i][3],
            "Preco_Ajuste": table_negocios[i][4],
            "Tipo_Do_Negocio": table_negocios[i][5],
            "Vlr_de_Operacao_Ajuste_DC": table_negocios[i][6],
            "Taxa_Operacional": table_negocios[i][7]
        }
        total_negocios[f"negocio{i}"] = negocio
        i += 1
    
    coluna_inferior = page.crop((20, 290, page.width, 385))
    inferior_settings = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "explicit",
        "explicit_horizontal_lines": [302, 312, 325, 335, 345, 355, 373, 378]
    }
    table_inferior = coluna_inferior.extract_table(inferior_settings)
    
    coluna_inferior2 = page.crop((20, 370, page.width, 385))
    inferior2_settings = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "explicit",
        "explicit_horizontal_lines": [302, 312, 325, 335, 345, 355, 373, 378]
    }
    table_inferior2 = coluna_inferior2.extract_table(inferior2_settings)
    
    obj_dados = {
        "Vendas_Disponivel": table_inferior[0][0],
        "Compras_Disponivel": table_inferior[0][2],
        "Vendas_Opcoes": table_inferior[0][4],
        "Compras_Opcoes": table_inferior[0][6],
        "Valor_dos_Negocios": table_inferior[0][8],
        "IRRF": table_inferior[2][0],
        "IRRF_DayTrade": table_inferior[2][2],
        "Taxa_Operacional": table_inferior[2][4],
        "Taxa_Registro_BMeF": table_inferior[2][6],
        "Taxa_BMeF_emol_gar": table_inferior[2][8],
        "Outros_Custos": table_inferior[4][0],
        "ISS": table_inferior[4][2],
        "Ajuste_de_posicao": table_inferior[4][4],
        "Ajuste_day_Trade": table_inferior[4][6],
        "Total_de_despesas": table_inferior[4][8],
        "IRRF_Corretagem": table_inferior2[0][0],
        "Total_Conta_Investimento": table_inferior2[0][2],
        "Total_Conta_Normal": table_inferior2[0][4],
        "Total_liquido": table_inferior2[0][6],
        "Total_liquido_da_nota": table_inferior2[0][8] 
    }

    obj_resumo = {
        "Corretora": obj_corretora,
        "Cliente": obj_cliente,
        "info_banco": obj_banco,
        "Negocios_realizados": total_negocios,
        "Tabela_inferior": obj_dados,
        "Dados_1": row[-11],
        "Dados_2": row[-10],
        "Dados_3": row[-9],
        "Dados_4": row[-8],
        "Dados_5": row[-7],
        "Dados_6": row[-6],
        "informacao_1": f"{row[-5]} {row[-4]} {row[-3]}",
        "informacao_2": f"{row[-2]} {row[-1]}"
    }
    
    print(obj_resumo)