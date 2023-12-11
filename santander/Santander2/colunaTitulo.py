import nome_arquivo
import pdfplumber

def ColunaCliente():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_cliente = page.crop((20, 200, page.width, 243))
        cliente_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [201, 211, 221, 231, 241]
        }
        table_cliente = coluna_cliente.extract_table(cliente_settings)
        num_cliente = table_cliente[0][1].split('Cliente:')
        info_cliente = table_cliente[3][2].split()
        
        
        obj_cliente = {
            "Número do Cliente": num_cliente[-1],
            "Nome": table_cliente[1][1],
            "Endereço": f"{table_cliente[2][1]} {table_cliente[3][1]}",
            "CPF_CNPJ_CVM_COB": table_cliente[1][2],
            "Codigo Cliente": info_cliente[0],
            "Assessor": info_cliente[1]
        }
        return obj_cliente

def Coluna_banco():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_banco = page.crop((20, 244, page.width, 286))
        banco_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_horizontal_lines": [255, 260, 277, 285],
            "explicit_vertical_lines": [54, 98, 152, 258, 341, 403, 540]
        }
        table_banco = coluna_banco.extract_table(banco_settings)

        obj_banco = {
            "Agente_de_compensação": table_banco[1][2],
            "Cliente": table_banco[1][3],
            "Valor": table_banco[1][4],
            "Custodiante": table_banco[1][5],
            "Banco": table_banco[4][0],
            "Agencia": table_banco[4][1],
            "Conta_Corrente": table_banco[4][2],
            "Acionista": table_banco[4][3],
            "Administrador": table_banco[4][4],
            "Complemento_Nome": table_banco[4][5]
        }
        return obj_banco

def Nota():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        nota = row[3].split()
        obj_nota = {
            "Numero da Pagina": row[0],
            "Data Pregão": nota[0],
            "N_Nota": nota[1]
        }
        return obj_nota


def ColunaTitulo():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        linha5 = row[5].split()
        num_endereco = 0
        endereco = ''
        while num_endereco <= len(linha5) - 3:
            endereco += f"{linha5[num_endereco]} "
            num_endereco += 1
        telefone = row[6].split()
    
        obj_corretora = {
            "Nome da Corretora": row[4],
            "Endereco": endereco,
            "CEP": linha5[-1],
            "Telefone_Capitais_e_regições_metropolitanas": f"{telefone[0]} {telefone[1][0]}{telefone[1][1]}{telefone[1][2]}{telefone[1][3]}",
            "Telefone_Demais_Localidades": f"{telefone[5]} {telefone[6]} {telefone[7][0]}{telefone[7][1]}{telefone[7][2]}{telefone[7][3]}",
            "Telefone_Pessoas_com_deficiencia": f"{telefone[-3]} {telefone[-2]} {telefone[-1][0]}{telefone[-1][1]}{telefone[-1][2]}{telefone[-1][3]}",
            "Site": row[8],
            "CNPJ": row[9]
        }
        
        obj_titulo = {
            "Corretora": obj_corretora,
            "Cliente": ColunaCliente(),
            "banco": Coluna_banco()
        }
        return obj_titulo
