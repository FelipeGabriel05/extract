import pdfplumber
import nome_arquivo

def Nota():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        all_text = ''
        for row in text:
            all_text += text
        row = all_text.split('\n')
        coluna_titulo = page.crop((455, 20, page.width, 65))
        titulos_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [50, 57],
            "explicit_vertical_lines": [458, 490, 523, 578]
        }
        titulos = coluna_titulo.extract_table(titulos_settings)
        obj_nota = {
            "Tipo_de_Nota": row[0],
            "Nr_Nota": titulos[0][0],
            "Foha": titulos[0][2],
            "Data_pregao": titulos[0][3]
        }
        return obj_nota
    
def Corretora():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        all_text = ''
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        telefone = row[5].split()
        internet = row[6].split()
        cnpj = row[7].split()
        ouvidoria = row[8].split()
        
        coluna_corretora = page.crop((389, 90, page.width, 100))
        corretora_settings1 = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [390, 560],
            "explicit_horizontal_lines": [90, 99]
        }
        email_corretora = coluna_corretora.extract_table(corretora_settings1)
        
        coluna_corretora2 = page.crop((409, 100, page.width, 110))
        corretora_settings2 = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [103, 109],
            "explicit_vertical_lines": [410, 550]
        }
        carta = coluna_corretora2.extract_table(corretora_settings2)
        
        coluna_corretora3 = page.crop((419, 110, 581, 120))
        corretora_settings3 = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [420, 580],
            "explicit_horizontal_lines": [110, 119]
        }
        email_ouvidoria = coluna_corretora3.extract_table(corretora_settings3)
    
        obj_corretora = {
            "Tipo_corretora": row[3],
            "Endereco": row[4],
            "Telefone": telefone[1],
            "Internet": internet[2],
            "CNPJ": cnpj[1],
            "Telefone_Ouvidoria": ouvidoria[3],
            "Email": email_corretora[0][0],
            "Carta Patente": carta[0][0],
            "Email_Ouvidoria": email_ouvidoria
        }
        return obj_corretora