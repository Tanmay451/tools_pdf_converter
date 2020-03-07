# Python program to convert 
# text file to pdf file 


from fpdf import FPDF 
import os
"""import glob

# file name in array
file_path = glob.glob("./code_file/*")
"""
# save FPDF() class into 
# a variable pdf 
file_path = []
if not os.path.exists('code_file'):
	os.make_dirs('code_file')
for dir in os.listdir('code_file'):
	file = './code_file/' + dir
	file_path.append(file)
pdf = FPDF() 
#print(file_path)
# Add a page 
pdf.add_page() 

# set style and size of font 
# that you want in the pdf 
pdf.set_font("Arial", size = 15) 

# open the text file in read mode 
for f in file_path:
	f = open(f, "r") 

	# insert the texts in pdf 
	for x in f: 
		pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 

	# save the pdf with name .pdf 
	pdf.output("tanmay.pdf") 
