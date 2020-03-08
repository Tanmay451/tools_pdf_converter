import os
from fpdf import FPDF
# https://pyfpdf.readthedocs.io/en/latest/reference/set_link/index.html
# https://pyfpdf.readthedocs.io/en/latest/reference/header/index.html
# fpdf.add_link()
pdf = FPDF()

# This is for header and footer
class PDF(FPDF):
    def header(self):
        # Select black for header
        pdf.set_text_color(100,0,0)
        # Select Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Framed title
        self.cell(30, 10, f[1:], 'C')
        # Line break
        self.ln(20)

pdf = PDF()

file_path = []

for root, dirs, files in os.walk("./code_file"):
    for file in files:
        if file.endswith(""):
             file_path.append(os.path.join(root, file))
             print(os.path.join(root, file))



for files in file_path: 
    prg_file = open(files)
    for f in prg_file:
        pdf.add_page()
        break
    
    
    for f in prg_file:
        if f[0] == "#":
            f = f[1:]
            if ("http" in f):
                print( pdf.set_link(f, y = -1, page = -1))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",f)
                pdf.cell(200, 8,txt=f, ln=1)
            else:
                pdf.set_text_color(0,70,0)
                pdf.set_font("Arial", size=8)
                pdf.cell(200, 8,txt=f, ln=1)
                print("Its comment          ",f)
        else:
            if (len(f) != 1):
                f = ">>>    "+f
                pdf.set_text_color(0,0,0)
                pdf.set_font("Arial", size=8)
                pdf.cell(200, 6, txt=f, ln=1)
                print("Its code             ",f)

pdf.output("simple_demo.pdf")      
    