import pdfplumber
import nome_arquivo

def Dados():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
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
        return obj_dados
    
def Resumo():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        obj_resumo = {
            "Dados_1": row[-11],
            "Dados_2": row[-10],
            "Dados_3": row[-9],
            "Dados_4": row[-8],
            "Dados_5": row[-7],
            "Dados_6": row[-6],
            "informacao_1": f"{row[-5]} {row[-4]} {row[-3]}",
            "informacao_2": f"{row[-2]} {row[-1]}"
        }
        return obj_resumo
        