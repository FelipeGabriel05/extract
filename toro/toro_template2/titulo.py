import pdfplumber
import nome_arquivo

def Titulo():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        titulo = row[2].split()
        
        obj_nota = {
            "Nome Completo": row[0],
            "Conta": titulo[1],
            "Data_de_referencia": titulo[2],
            "Comprovante": titulo[3],
            "Titulo_da_nota": row[3],
            "Numero_da_pagina": row[-1]
        }
        return obj_nota
        