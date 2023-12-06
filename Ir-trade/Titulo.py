import pdfplumber

def Titulo_template(num_page):
    with pdfplumber.open('48976_informe_para_imposto_renda_ano_calendario_2021.pdf') as pdf:
        page = pdf.pages[num_page]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        nome = row[3].split('Nome: ')
        cpf_cnpj = row[4].split('CPF/CNPJ: ')
        dado_inferior = row[-1].split()
        titulo = {
            "Calendario": row[0],
            "Informe_de_rendimentos": f"{row[1]} {row[2]}",
            "Nome_Cliente": nome[-1],
            "CPF_CNPJ": cpf_cnpj[-1],
            "titulo_de_operacao": f"{row[5]} {row[6]} ",
            "Internet": dado_inferior[0],
            "Numero_da_pagina": dado_inferior[-1]
        }
        return titulo
    
# Titulo_template(1)