import pdfplumber

data = {}
with pdfplumber.open("test.pdf") as pdf:
    for i, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        data[f"Page {i}"] = text
        

print(data)
