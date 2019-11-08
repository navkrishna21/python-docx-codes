from docx import Document


document = Document('/home/navkrishna/Downloads/demo.docx') #document location

flag=True
for (table_no,table) in enumerate(document.tables):
	empty_rows=[]
	empty_cols=[]

	for (i,row) in enumerate(table.rows):
		for cell in row.cells:
			if cell.text:
				break
		else:
			empty_rows.append(i)
				
	
	for (i,col) in enumerate(table.columns):
		for cell in col.cells:
			if cell.text:
				break
		else:
			empty_cols.append(i)			

	if empty_rows:
		flag=False
		print("Empty rows in table {}  are: ".format(table_no+1) + ','.join( map(str,empty_rows)) )



	if empty_cols:
		flag=False
		print("Empty columns in table {}  are: ".format(table_no+1) + ','.join( map(str,empty_cols) ))

if flag:
	print("No issues in the document file")
