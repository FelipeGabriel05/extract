import titulo
import cliente
import negocios
import resumo
import resumo_financeiro

def main():
    TemplateBradesco = {
        "Nota": titulo.Nota(),
        "Corretora": titulo.Corretora(),
        "Cliente": cliente.Cliente(),
        "Banco": cliente.Banco(),
        "Total_Negocios": negocios.Negocios(),
        "Resumo dos Negocios": resumo.Resumo(),
        "Observação": resumo.Observacao(),
        "Resumo Financeiro": resumo_financeiro.Resumo_Financeiro()
    }
    print(TemplateBradesco)
    return TemplateBradesco

if __name__ == '__main__':
    main()