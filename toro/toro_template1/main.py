import detalhes
import observacoes
import resumo
import titulo

def main():
    TemplateToro_1 = {
        "Titulo_da_nota": titulo.Titulo(),
        "Comprovante_BM&F_Resumo": resumo.Resumo(),
        "Detalhes": detalhes.Detalhes(),
        "Observações": observacoes.Observacoes() 
    }
    print(TemplateToro_1)
    return TemplateToro_1

if __name__ == '__main__':
    main()