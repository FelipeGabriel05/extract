import pdfplumber
import text
import titulo
import nome_arquivo

def InfoComplementar():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        row = text.Pegar_Texto(17)
        whatsapp = row[-1].split('17/17')
        obj = {
            "Titulo_pagina": titulo,
            "observação1": f"{row[7]} {row[8]} {row[9]} {row[10]} {row[11]} {row[12]}",
            "observação2": f"{row[13]} {row[14]} {row[15]}",
            "telefone": row[-3],
            "email": row[-2],
            "whatsapp": whatsapp[0] 
        }
        return obj
