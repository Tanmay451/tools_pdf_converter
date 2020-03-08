import os
from fpdf import FPDF

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

if not os.path.exists('code_file'):
	os.make_dirs('code_file')
for dir in os.listdir('code_file'):
	file = './code_file/' + dir
	file_path.append(file)


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
    