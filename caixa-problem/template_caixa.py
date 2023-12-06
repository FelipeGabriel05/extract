import pdfplumber

with pdfplumber.open('Caixa.pdf') as pdf:
    page = pdf.pages[0]
    texto = page.extract_text()
    all_text = ""
    for row in texto:
        all_text += texto
    row = all_text.split("\n")
    print(row[1])