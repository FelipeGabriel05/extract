import pdfplumber
import nome_arquivo

def Cliente():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        documento = row[10].split()
        
        coluna_cliente = page.crop((20, 125, 457, 162))
        cliente_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [132, 142, 152, 159],
            "explicit_vertical_lines": [38, 100, 455]
        }
        tabela_cliente = coluna_cliente.extract_table(cliente_settings)
        
        coluna_cliente2 = page.crop((454, 140, page.width, 162))
        cliente_settings2 = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [150, 160],
            "explicit_vertical_lines": [458, 538, 580]
        }
        tabela_cliente2 = coluna_cliente2.extract_table(cliente_settings2)
        
        obj_cliente = {
            "CPF_CNPJ_CVM_COB": documento[-1],
            "Numero_do_Cliente": tabela_cliente[0][0],
            "Nome": tabela_cliente[0][1],
            "Endereco_cliente": f"{tabela_cliente[1][1]} {tabela_cliente[2][1]}",
            "Codigo_cliente": tabela_cliente2[0][0],
            "Acessor": tabela_cliente2[0][1]
        }    
        return obj_cliente
    
def Banco():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_banco = page.crop((20, 160, page.width, 180))
        banco_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [170, 178],
            "explicit_vertical_lines": [40, 250, 330, 456, 558, 578]
        }
        tabela_banco = coluna_banco.extract_table(banco_settings)
        coluna_banco2 = page.crop((20, 180, page.width, 200))
        banco_settings2 = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [188, 198],
            "explicit_vertical_lines": [38, 69, 169, 254, 333, 456, 558, 578]
        }
        tabela_banco2 = coluna_banco2.extract_table(banco_settings2)
        obj_banco = {
            "Participante_destino_do_repasse": tabela_banco[0][0],
            "Cliente": tabela_banco[0][2],
            "Valor": f"{tabela_banco[0][4]} {tabela_banco[0][5]}",
            "Custodiante": tabela_banco[0][6],
            "CI": tabela_banco[0][7],
            "Banco": tabela_banco2[0][0],
            "Agencia": tabela_banco2[0][1],
            "Conta_Corrente": tabela_banco2[0][2],
            "Acionista": tabela_banco2[0][3],
            "Administrador": tabela_banco2[0][4],
            "Complemento_nome": tabela_banco2[0][5],
            "P_Vinc": tabela_banco2[0][6]
        }
        return obj_banco