from docx import Document


document = Document('/home/navkrishna/Downloads/demo.docx') #document location

flag = True

for (table_no,table) in enumerate(document.tables):
	empty_cells=[]
	for (i,row) in enumerate(table.rows):
		for (j,cell) in enumerate(row.cells):
			if not cell.text:
				empty_cells.append((i,j))

	if empty_cells:
		flag = False
		print("empty cells in table {}  are: ".format(table_no+1))

		for row,col in empty_cells:
			print("row : {} , column : {}".format(row,col)  )
		print()

if flag:
	print("No issues in the document file")
