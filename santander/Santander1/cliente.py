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
        
        num_cliente = row[9].split()
        num_letra = 8
        cliente = ''
        while num_letra <= len(num_cliente[0]) - 1:
            cliente += f"{num_cliente[0][num_letra]}"
            num_letra += 1
        
        cliente_nome = ''
        num_total_nome = 1
        while num_total_nome <= len(num_cliente) - 1:
            cliente_nome += f"{num_cliente[num_total_nome]} "
            num_total_nome += 1
        
        complemento_nome = row[10].split('CPF/CNPJ/CVM/COB CÓDIGO CLIENTE')
        
        total_increment = 0
        dados_cliente = row[12].split()
        complemento_endereco_cliente = ''
        while total_increment <= len(dados_cliente) -3:
            complemento_endereco_cliente += f"{dados_cliente[total_increment]} "
            total_increment += 1

        cep = row[13].split('CEP:')
        cidade = row[14].split('CIDADE:')
        
        obj_cliente = {
            "Numero do Cliente": cliente,
            "Nome do Cliente": f"{cliente_nome}{complemento_nome[0]}",
            "Endereço": f"{row[11]} {complemento_endereco_cliente}",
            "CEP": cep[-1],
            "CIDADE": cidade[-1],
            "CPF_CNPJ_CVM_COB": dados_cliente[-2],
            "Código Cliente": dados_cliente[-1]
        }
        return obj_cliente
    
def Banco():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_banco = page.crop((20, 210, page.width, 270))
        
        banco_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [220, 230, 253, 265]
        }
        table_banco = coluna_banco.extract_table(banco_settings)
        
        obj_banco = {
            "Agente_de_Compensação": table_banco[0][0],
            "CLIENTE": table_banco[0][1],
            "Valor": table_banco[0][2],
            "Custodiante": table_banco[0][3],
            "Banco_Agencia_Conta corrente": table_banco[2][0],
            "Acionista": table_banco[2][1],
            "Administrador": table_banco[2][2],
            "Complemento_Nome": table_banco[2][3]
        }
        return obj_banco