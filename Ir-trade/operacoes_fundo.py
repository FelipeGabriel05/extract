import pdfplumber

with pdfplumber.open('48976_informe_para_imposto_renda_ano_calendario_2021.pdf') as pdf:
    page = pdf.pages[15]
    operations = page.crop((20, 275, page.width, 500))
    
    operation_settings = {
        "vertical_strategy": "explicit",
        "horizontal_strategy": "text",
        "explicit_vertical_lines": [75, 110, 165, 228, 285, 345, 410, 468, 525, 588, 654, 710, 766],
        "explicit_horizontal_lines": [
            280, 290, 310, 330, 340, 360, 380, 400, 410, 430, 450, 460, 480
        ]
    }
    table_operation = operations.extract_table(operation_settings)
    
    i = 0
    lista_meses = []
    while i <= len(table_operation) - 1:
        if len(table_operation[i][0]) == 3:
            lista_meses.append(table_operation[i])
        i += 1
    
    
    total_operacoes = 0
    meses_operacoes = {}
    while total_operacoes <= len(lista_meses) - 1:
        obj = {
            "Resultado Líquido do Mês": lista_meses[total_operacoes][1],
            "Resultado Negativo Mês Anterior": lista_meses[total_operacoes][2],
            "Base Cálculo Imposto": lista_meses[total_operacoes][3],
            "Prejuízo Compensar": lista_meses[total_operacoes][4],
            "Alíquota do Imposto": lista_meses[total_operacoes][5],
            "Imposto Devido": lista_meses[total_operacoes][6],
            "Saldo do imposto retido nos meses anteriores": lista_meses[total_operacoes][7],
            "Imposto retido no mês": lista_meses[total_operacoes][8],
            "Imposto a compensar": lista_meses[total_operacoes][9],
            "imposto a pagar": lista_meses[total_operacoes][10],
            "Imposto pago": lista_meses[total_operacoes][11],
        }
        meses_operacoes[f"{lista_meses[total_operacoes][0]}"] = obj
        total_operacoes += 1
        
    print(meses_operacoes)