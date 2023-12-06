import pdfplumber

with pdfplumber.open("Toro - Futuro.pdf") as pdf:
    page = pdf.pages[0]
    coluna_resumo = page.crop((20, 155, page.width, 270))
    all_text = ""
    text = page.extract_text()
    for row in text:
        all_text += text
    row = all_text.split('\n')
    resumo_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "text",
        "explicit_horizontal_lines": [160, 170, 190, 210, 220, 240, 255, 265],
        "explicit_vertical_lines": [35, 120, 158, 170, 250, 294, 304, 370, 430, 442, 500, 566]
    }
    table_resumo = coluna_resumo.extract_table(resumo_settings)
    
    i = 0
    lista_resumo = []
    while i <= len(table_resumo) - 1:
        if table_resumo[i][0] != '':
            lista_resumo.append(table_resumo[i])
        i += 1
    titulo = row[2].split()
    obj_nota = {
        "Nome Completo": row[0],
        "Conta": titulo[1],
        "Data_de_referencia": titulo[2],
        "Comprovante": titulo[3],
        "Titulo_da_nota": row[3],
        "Resumo": {
            "VOLUME FINANCEIRO E AJUSTES": {
                lista_resumo[0][0]: lista_resumo[0][1],
                lista_resumo[1][0]: lista_resumo[1][1],
                lista_resumo[2][0]: lista_resumo[2][1],
                lista_resumo[3][0]: lista_resumo[3][1],
                lista_resumo[4][0]: lista_resumo[4][1],
                lista_resumo[5][0]: lista_resumo[5][1],
                lista_resumo[6][0]: lista_resumo[6][1]
            },
            "TRIBUTOS": {
                lista_resumo[0][3]: lista_resumo[0][4],
                lista_resumo[1][3]: lista_resumo[1][4],
                lista_resumo[2][3]: lista_resumo[2][4],
                lista_resumo[3][3]: lista_resumo[3][4],
                lista_resumo[4][3]: lista_resumo[4][4],
                lista_resumo[5][3]: lista_resumo[5][4]
            },
            "CUSTOS": {
                lista_resumo[0][6]: lista_resumo[0][7],
                lista_resumo[1][6]: lista_resumo[1][7],
                lista_resumo[2][6]: lista_resumo[2][7],
                lista_resumo[3][6]: lista_resumo[3][7],
            },
            "RESULTADO": {
                lista_resumo[0][9]: lista_resumo[0][10],
                lista_resumo[1][9]: lista_resumo[1][10],
                lista_resumo[2][9]: lista_resumo[2][10],
                lista_resumo[3][9]: lista_resumo[3][10],
            }
        }
    }
    
    coluna_detalhes = page.crop((20, 430, page.width, 500))
    detalhes_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [40, 106, 170, 230, 318, 413, 496, 566]
    }
    table_detalhes = coluna_detalhes.extract_table(detalhes_settings)
    linha14 = row[14].split()
    linha15 = row[15].split()
    total_detalhes = {
        "Título": linha14[0],
        "Quantidade_total_de_compra": linha14[5],
        "Preço médio compra": f"{linha14[9]} {linha15[0]}",
        "Quantidade_total_de_venda": {linha14[14]},
        "Preço médio venda": f"{linha14[-1]} {linha15[-1]}"
    }
    
    total_negocios = 0
    while total_negocios <= len(table_detalhes) - 1:
        soma = total_negocios + 1
        negocio = {
            "CV": table_detalhes[total_negocios][0],
            "Vencimento": table_detalhes[total_negocios][1],
            "Quantidade": table_detalhes[total_negocios][2],
            "Preco_Ajuste": table_detalhes[total_negocios][3],
            "Tipo_de_negocio": table_detalhes[total_negocios][4],
            "Valor_Operacao": table_detalhes[total_negocios][5],
            "Taxa_Operacao": table_detalhes[total_negocios][6],
        }
        total_detalhes[f"negocio_{soma}"] = negocio 
        total_negocios += 1
        
    linha19 = row[19].split()
    linha20 = row[20].split()
    
    total_increment = 12
    nome = ''
    while total_increment <= 26:
        nome += f" {linha19[total_increment]}"
        total_increment += 1
    ouvidoria = row[-3].split('Ouvidoria:')
    obj_especificacoes = {
        "IRRF_Day_Trade": {
            "Base": f"{linha19[7]} {linha19[8]}",
            "Projeção": f"{linha19[10]} {linha19[11]}",
            "obs": nome
        },
        "IRRF_Operacao_Comum": {
            "Base": linha20[4],
            "Projeção": linha20[6],
            "obs": row[21],
        },
        "informação adicional": f"{row[22]} {row[23]} {row[24]} {row[25]} {row[26]} {row[27]} {row[28]}",
        "Ouvidoria": ouvidoria[-1],
        "Dias_uteis": row[-2],
        "Página": row[-1]
    }
    