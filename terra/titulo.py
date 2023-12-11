import pdfplumber
import nome_arquivo

def Nota():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
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
        return obj_nota
    
def Corretora():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
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
        return obj_corretora
    
def Cliente():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
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
        table_cliente = coluna_cliente.extract_table(cliente_settings)
        
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
        return obj_cliente