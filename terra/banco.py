import pdfplumber
import nome_arquivo

def Banco():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]

        coluna_banco1 = page.crop((20, 185, page.width, 203))
        banco1_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [195, 202]
        }
        table_banco1 = coluna_banco1.extract_table(banco1_settings)
        
        coluna_banco2 = page.crop((20, 204, page.width, 225))
        banco2_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [215, 220]
        }
        table_banco2 = coluna_banco2.extract_table(banco2_settings)
        
        obj_banco = {
            "Banco": table_banco1[0][0],
            "Agencia": table_banco1[0][1],
            "Conta_Corrente": table_banco1[0][2],
            "Acionista": table_banco2[0][0],
            "Administrador": table_banco2[0][1],
            "Complemento_nome": table_banco2[0][2],
            "P_Vinc": table_banco2[0][3]
        }
        return obj_banco