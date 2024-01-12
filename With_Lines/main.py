from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation = "P", unit = "mm", format = "A4")

pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    #set Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1)
    
    #For creating Lines
    for i in range(20, 298, 10):
        pdf.line(10, i, 200, i)

    #set Footer
    pdf.ln(250)
    pdf.set_font(family='Times', style='I', size=9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R",
             ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        #For creating Lines
        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)
            
        #set Footer
        pdf.ln(250)
        pdf.set_font(family='Times', style='I', size=9)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R",
                ln=1)

pdf.output("output1.pdf")