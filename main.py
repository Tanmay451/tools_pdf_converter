# Python program to convert 
# text file to pdf file 


from fpdf import FPDF 
import glob

# file name in array
file_path = glob.glob("./code_file/*")

# save FPDF() class into 
# a variable pdf 
pdf = FPDF() 
 

# set style and size of font 
# that you want in the pdf 
pdf.set_font("Arial", size = 15) 

# open the text file in read mode 
for f in file_path:
	# Add a page 
	pdf.add_page()
	
	f = open(f, "r") 

	# insert the texts in pdf 
	for x in f: 
		pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 

	# save the pdf with name .pdf 
pdf.output("tanmay.pdf") 
