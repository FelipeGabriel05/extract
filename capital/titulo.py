import pdfplumber
import text
import nome_arquivo

def Titulo(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        row = text.Pegar_texto(num_page)
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
        return obj_titulo

def Corretora(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        row = text.Pegar_texto(num_page)
        
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
        return obj_corretora
    
def Cliente(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_texto(num_page)
        
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
        return obj_cliente