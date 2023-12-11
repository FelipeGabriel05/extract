import colunaTitulo
import negociacao
import resumo
import negocios

def main():
    templateSantander = {
        "Nota": colunaTitulo.Nota(),
        "Titulo": colunaTitulo.ColunaTitulo(),
        "Total_Negocios": negocios.Negocio(),
        "Página_2": {
            "Informações": negociacao.Num_page(),
            "Negociação": negociacao.Negociacao(),
            "Observação": negociacao.Observacao(),
            "Resumo": resumo.Resumo()
        }
    }
    print(templateSantander)
    return templateSantander

if __name__ == '__main__':
    main()