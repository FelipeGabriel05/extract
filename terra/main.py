import titulo
import banco
import negocio
import resumo

def main():
    templateTerra = {
        "Nota": titulo.Nota(),
        "Corretora": titulo.Corretora(),
        "Cliente": titulo.Cliente(),
        "Banco": banco.Banco(),
        "Total Negocios": negocio.Negocios(),
        "Dados da Nota": resumo.Dados(),
        "Obsevações": resumo.Resumo()
    }
    print(templateTerra)
    return templateTerra

if __name__ == '__main__':
    main()