import pdfplumber
import nome_arquivo

def Pegar_Texto(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[num_page]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        return row