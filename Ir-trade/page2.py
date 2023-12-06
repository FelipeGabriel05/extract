import pdfplumber

with pdfplumber.open('48976_informe_para_imposto_renda_ano_calendario_2021.pdf') as pdf:
    page = pdf.pages[2]
    coluna_bovespa = page.crop((20, 250, page.width, 320))
    bovespa_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [40, 130, 160, 200, 250, 390, 480, 540, 610, 638, 730, 800],
        "explicit_horizontal_lines": [258, 268, 285, 305, 315]
    }
    tabela_bovespa = coluna_bovespa.extract_table(bovespa_settings)
    
    total_negocios = {}
    total_increment = 0
    while total_increment <= len(tabela_bovespa) - 2:
        negocio = {
            "Corretora": tabela_bovespa[total_increment][0],
            "CV": tabela_bovespa[total_increment][1],
            "Grupo": tabela_bovespa[total_increment][2],
            "Codigo": tabela_bovespa[total_increment][3],
            "Empresa": tabela_bovespa[total_increment][4],
            "CNPJ": tabela_bovespa[total_increment][5],
            "Ativo": tabela_bovespa[total_increment][6],
            "Vencimento": tabela_bovespa[total_increment][7],
            "Qtd": tabela_bovespa[total_increment][8],
            "Custo_medio": tabela_bovespa[total_increment][9],
            "Total_cTaxas": tabela_bovespa[total_increment][10],
        }
        total_negocios[f"negocio_{total_increment}"] = negocio
        total_increment += 1
    
    obj_bovespa = {
        "Total_negocios": total_negocios,
        "Total_de_posicao": tabela_bovespa[-1][-1]
    }
    print(obj_bovespa)