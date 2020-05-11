import pdfplumber

with pdfplumber.open("2020.pdf") as pdf, open('out.txt', 'w', encoding='utf-8') as f:
    for page in pdf.pages:
        for row in page.extract_table():
            f.write('|'.join([r.replace('\n', '') for r in row]) + '\n')