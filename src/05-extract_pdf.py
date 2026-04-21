import fitz  
import os

def pdf_to_text(pdf_path, output_txt):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Extraction réussie : {output_txt}")

# Utilisation
pdf_to_text("../Documents/Document5.pdf", "../Data/Document5.txt")
