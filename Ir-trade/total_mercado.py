import pdfplumber
import text
import nome_arquivo

def Total_mercado():
    import mercado
    import mercado2
    import titulo
    
    total_meses = 3
    negocios_mercado = {}
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        while total_meses <= 14:
            row = text.Pegar_Texto(total_meses)
            mes = row[7].split()
            if total_meses == 14: 
                obj_mercado = {
                    "Titulo_pagina": titulo.Titulo(total_meses),
                    "Mercado à vista": mercado.Mercado_Vista(total_meses),
                    "Mercado Opções": mercado.Mercado_Opcoes(total_meses),
                    "Mercado Futuro": mercado.Mercado_Futuro(total_meses),
                    "Mercado Termo": mercado2.Mercado_Termo(total_meses),
                    "Resultados": mercado2.Resultados(total_meses),
                    "Consolidação do Mês": mercado2.Consolidacao(total_meses),
                    "informação1": row[-4],
                    "informação2": f"{row[-3]} {row[-2]}"
                }
            else:
                obj_mercado = {
                    "Titulo_pagina": titulo.Titulo(total_meses),
                    "Mercado à vista": mercado.Mercado_Vista(total_meses),
                    "Mercado Opções": mercado.Mercado_Opcoes(total_meses),
                    "Mercado Futuro": mercado.Mercado_Futuro(total_meses),
                    "Mercado Termo": mercado2.Mercado_Termo(total_meses),
                    "Resultados": mercado2.Resultados(total_meses),
                    "Consolidação do Mês": mercado2.Consolidacao(total_meses),
                }
            negocios_mercado[f"{mes[-1]}"] = obj_mercado
            total_meses += 1
    return negocios_mercado
