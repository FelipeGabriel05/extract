import pdfplumber

with pdfplumber.open('48976_informe_para_imposto_renda_ano_calendario_2021.pdf') as pdf:
    page = pdf.pages[1]
    all_text = ''
    text = page.extract_text()
    for row in text:
        all_text += text
    row = all_text.split('\n')
        
    coluna_table = page.crop((20, 190, page.width, 415))
    table_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "lines",
        "explicit_vertical_lines": [105, 310, 410, 498],
        "explicit_horizontal_lines": [190, 204, 215, 230, 245, 260, 275, 290, 305, 320, 335, 350,
    365, 380, 395, 406]
    }
    tabela_meses = coluna_table.extract_table(table_settings)
    
    i = 3
    meses_lista = []
    while i <= len(tabela_meses) - 2:
        mes = {
            "Mes": tabela_meses[i][0],
            "Total_no_mes": tabela_meses[i][2]
        }
        meses_lista.append(mes) 
        i += 1
    
    obj_vendas_isentas = {
        "titulo_vendas": tabela_meses[0][0],
        "Cod_Lancamento": tabela_meses[1][1],
        "Total": tabela_meses[1][2],
        "total_mes" : {
            "mes1": meses_lista[0],
            "mes2": meses_lista[1],
            "mes3": meses_lista[2],
            "mes4": meses_lista[3],
            "mes5": meses_lista[4],
            "mes6": meses_lista[5],
            "mes7": meses_lista[6],
            "mes8": meses_lista[7],
            "mes9": meses_lista[8],
            "mes10": meses_lista[9],
            "mes11": meses_lista[10],
            "mes12": meses_lista[11]
        }
    }
       
    obj_adicional = {
        row[-6]: f"{row[-4]} {row[-3]} {row[-2]}"
    }
    
    