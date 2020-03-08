import os

file_path = []

if not os.path.exists('code_file'):
	os.make_dirs('code_file')
for dir in os.listdir('code_file'):
	file = './code_file/' + dir
	file_path.append(file)


for files in file_path: 
    prg_file = open(files)
    for f in prg_file:
        if f[0] == "#":
            print("Its comment          ",f)
        else:
            print("Its code             ",f)
        
    