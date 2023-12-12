import titulo
import resumo
import detalhes
import observacoes

def Main():
    TemplateToro2 = {
        "Titulo_Nota": titulo.Titulo(),
        "Resumo_Nota": resumo.Resumo(),
        "Detalhes": detalhes.Detalhes(),
        "Observações": {
            "Legenda": observacoes.Legenda(),
            "Obs_adicionais": observacoes.Adicional()
        }
    }
    print(TemplateToro2)
    return TemplateToro2

if __name__ == '__main__':
    Main()