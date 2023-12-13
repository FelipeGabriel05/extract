import pdfplumber
import text
import nome_arquivo

def Titulo(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_texto(num_page)
        tipo_nota = row[5].split()
        
        obj = {
            "Data_pregao": tipo_nota[2],
            "N_Nota": tipo_nota[5],
            "Folha": tipo_nota[7]
        }
        return obj
        
    
def Corretora(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_texto(num_page)
        
        total = 0
        endereco = ''
        text_address = row[1].split()
        while total <= len(text_address) - 2:
            endereco += f" {text_address[total]}"
            total += 1
        
        telefones = row[2].split()
        internet = row[3].split()
        campo_cnpj = row[4].split(":")
        obj_corretagem = {
            "Nome_da_corretora": row[0],
            "Endereco": endereco,
            "Telefone": f"{telefones[0]} {telefones[1]}",
            "Ouvidoria": f"{telefones[-3]} {telefones[-2]} {telefones[-1]}",
            "Internet": internet[1],
            "CNPJ": campo_cnpj[1] 
        }
        return obj_corretagem

def Cliente(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_texto(num_page)
        
        cliente = row[7].split()
        nome_total = 1
        nome_cliente = ''
        while nome_total <= len(cliente) - 2:
            nome_cliente += f"{cliente[nome_total]} "
            nome_total += 1

        obj_cliente = {
            "Numero_do_Cliente": cliente[0],
            "Nome_do_Cliente": nome_cliente,
            "CPF_CNPJ_CVM_COB": cliente[-1],
            "Endereco_Cliente": f"{row[8]} {row[9]}"
        }
        return obj_cliente
    
def Banco(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_texto(num_page)
        
        banco = row[11].split()
        obj_banco = {
            "Banco": banco[0],
            "Agencia": banco[1],
            "Conta_Corrente": banco[2]
        }
        return obj_banco
