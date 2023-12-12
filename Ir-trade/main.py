import titulo
import negocios
import total_mercado
import operacao
import infoComplementar

def Main():
    TemplateIR = {
        "Rendimentos": titulo.Rendimentos(),
        "Negocios": negocios.Negocios(),
        "Mercado": total_mercado.Total_mercado(),
        "Operação": operacao.Operacao(),
        "Informações Complementares": infoComplementar.InfoComplementar()
    }
    print(TemplateIR)
    return TemplateIR

if __name__ == '__main__':
    Main()
