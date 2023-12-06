import pdfplumber

with pdfplumber.open('Toro.pdf') as pdf:
    page = pdf.pages[0]
    all_text = ''
    text = page.extract_text()
    for row in text:
        all_text += text
    row = all_text.split("\n")
    coluna_resumo = page.crop((20, 155, page.width, 270))
    resumo_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "text",
        "explicit_vertical_lines": [35, 120, 158, 170, 250, 294, 304, 370, 430, 442, 500, 566],
        "explicit_horizontal_lines": [160, 170, 190, 210, 220, 240, 255]
    }
    table_resumo = coluna_resumo.extract_table(resumo_settings)
    
    coluna_detalhes = page.crop((20, 430, page.width, 480))
    detalhes_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [35, 90, 140, 210, 260, 340, 400, 480, 518, 567]
    }
    tabela_detalhes = coluna_detalhes.extract_table(detalhes_settings)
    
    i = 0
    resumo_list = []
    while i <= len(table_resumo) - 1:
        if table_resumo[i][4] != '':
            resumo_list.append(table_resumo[i])
        i += 1
    
    titulo = row[2].split()
    linha14 = row[14].split()
    
    obj_detalhes = {
        "Titulo": row[13],
        "Preco de Exercício": linha14[3],
        "Quantidade_total_de_compra": linha14[8],
        "Preço_médio_compra": f"{linha14[12]} {row[15]}",
        "Quantidade_total_de_venda": linha14[17],
        "Preço_médio_venda": f"{linha14[21]}{linha14[22]}",
        "detalhes": {
            "CV": tabela_detalhes[0][0],
            "Mercado": tabela_detalhes[0][1],
            "Quantidade": tabela_detalhes[0][2],
            "Preço": tabela_detalhes[0][3],
            "Valor_Operação": tabela_detalhes[0][4],
            "Vencimento": tabela_detalhes[0][5],
            "Tipo_Mercado": tabela_detalhes[0][6],
            "Envio": tabela_detalhes[0][7],
            "OBS": tabela_detalhes[0][8]
        }
    }
    
    coluna_legenda = page.crop((20, 496, page.width, 650))
    legenda_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [30, 220, 450],
        "explicit_horizontal_lines": [500, 515, 525, 535, 545, 555, 565, 575, 585]
    }
    tabela_legenda = coluna_legenda.extract_table(legenda_settings)
    
    obs = {
        "titulo": "Legenda",
        "dados_2": tabela_legenda[0][0],
        "dados_P": tabela_legenda[0][1],
        "dados_negocio": tabela_legenda[1][0],
        "dados_H": tabela_legenda[1][1],
        "dados_8": tabela_legenda[2][0],
        "dados_X": tabela_legenda[2][1],
        "dados_D": tabela_legenda[3][0],
        "dados_Y": tabela_legenda[3][1],
        "dados_F": tabela_legenda[4][0],
        "dados_L": tabela_legenda[4][1],
        "dados_B": tabela_legenda[5][0],
        "dados_T": tabela_legenda[5][1],
        "dados_A": tabela_legenda[6][0],
        "dados_I": tabela_legenda[6][1],
        "dados_C": tabela_legenda[7][0]
    }
    
    linha_dt = row[-11].split()
    dt_obs = row[-11].split('Especificações diversas: IRRF Day Trade: Base R$0,00 Projeção R$0,00')
    linha_oc = row[-10].split()
    obj_adicional = {
        "Especificações diversas": {
            "IRRF_Day_Trade": {
                "Base": linha_dt[6],
                "Projeção": linha_dt[8],
                "obs": dt_obs[-1]
            },
            "IRRF_Operação_Comum": {
                "Base": linha_oc[4],
                "Projeção": linha_oc[6],
                "obs": row[-9]
            },
            "informação_adicional": f"{row[-8]} {row[-7]} {row[-6]} {row[-5]} {row[-4]} {row[-3]} {row[-2]}"
        }
    }
    
    
    
    obj_nota = {
        "Nome Completo": row[0],
        "Conta": titulo[1],
        "Data_de_referencia": titulo[2],
        "Comprovante": titulo[3],
        "Titulo_da_nota": row[3],
        "Numero_da_pagina": row[-1],
        "Resumo": {
             "RESUMO DOS NEGÓCIOS": {
                resumo_list[0][0]: resumo_list[0][1],
                resumo_list[1][0]: resumo_list[1][1],
                resumo_list[2][0]: resumo_list[2][1],
                resumo_list[3][0]: resumo_list[3][1]
            },
            "Tributos": {
                resumo_list[0][3]: resumo_list[0][4],
                resumo_list[1][3]: resumo_list[1][4],
                resumo_list[2][3]: resumo_list[2][4],
                resumo_list[3][3]: resumo_list[3][4],
                resumo_list[-3][3]: resumo_list[-3][4],
                resumo_list[-2][3]: resumo_list[-2][4],
                resumo_list[-1][3]: resumo_list[-1][4]
            },
            "CUSTOS": {
                resumo_list[0][6]: resumo_list[0][7],
                resumo_list[1][6]: resumo_list[1][7],
                resumo_list[2][6]: resumo_list[2][7],
                resumo_list[3][6]: resumo_list[3][7],
                resumo_list[-2][6]: resumo_list[-2][7],
                resumo_list[-1][6]: resumo_list[-1][7],
            },
            "RESULTADO": {
                resumo_list[0][9]: resumo_list[0][10],
                resumo_list[1][9]: resumo_list[1][10],
                resumo_list[2][9]: resumo_list[2][10],
                resumo_list[3][9]: resumo_list[3][10],
                resumo_list[-2][-2]: resumo_list[-2][-1],
            }
        },
        "Detalhes": obj_detalhes,
        "Observações": obs,
        "Adicional": obj_adicional
    }