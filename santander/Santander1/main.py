import corretora
import cliente
import negocio
import negociacao
import resumo

def main():
    templateSantander = {
        "Titulo": corretora.Titulo(),
        "Corretora": corretora.Corretora(),
        "Cliente": cliente.Cliente(),
        "Banco": cliente.Banco(),
        "Total_Negocios": negocio.Negocios(),
        "Negociação": negociacao.Negociacao(),
        "Observação": negociacao.Observacoes(),
        "Resumo": resumo.Resumo()
    }
    print(templateSantander)
    return templateSantander

if __name__ == '__main__':
    main()