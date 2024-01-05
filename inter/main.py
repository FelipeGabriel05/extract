import titulo
import text
import negocios
import resumo
import observacoes

def Main():
    i = 0
    total_paginas = text.Total_page()
    num_page = 1
    extract = {}
    while i <= total_paginas -1:
        Template_Inter = {
            "Titulo": titulo.Titulo(i),
            "Corretora": titulo.Corretora(i),
            "Cliente": titulo.Cliente(i),
            "Banco": titulo.Banco(i),
            "Negocios Realizados": negocios.Negocios(i),
            "Resumo": resumo.Resumo(i),
            "Observações": observacoes.Observacoes(i),
            "Final_Pagina": observacoes.Final_pagina(i)
        }
        extract[f"Pagina_{num_page}"] = Template_Inter
        num_page += 1
        i += 1
    return extract

if __name__ == '__main__':
    Main()
