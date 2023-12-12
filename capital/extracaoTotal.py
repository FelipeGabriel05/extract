import titulo
import resumo
import negocios
import text

def Extract():
    total_paginas = text.Total_Paginas()
    pagina = 1
    i = 0
    extract = {}
    while i <= total_paginas - 1:
        obj = {
            "Titulo_da_Nota": titulo.Titulo(0),
            "Corretora": titulo.Corretora(0),
            "Cliente": titulo.Cliente(0),
            "Negocios": negocios.Negocios(0),
            "Resumo_dos_Negocios": resumo.Resumo(0),
            "Observações": negocios.Observacoes(0)    
        }
        extract[f"Page_{pagina}"] = obj
        pagina += 1
        i += 1
    return extract
