from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv") # переменная возращает весь csv файл вместе с индексами


for index, row in df.iterrows():
    y1 = 20
    y2 = 20
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size= 16)
    pdf.set_text_color(100, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    for i in range(1, 30):
        pdf.line(10, y1, 200, y2)
        y1 += 20
        y2 += 20

    pdf.ln(252)

    pdf.set_font(family="Times", style="B", size=14)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=0, txt=str(row["Order"]), align="R")



pdf.output('output.pdf', 'F')