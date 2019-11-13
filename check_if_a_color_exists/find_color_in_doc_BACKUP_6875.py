from docx import Document
from docx.shared import RGBColor

def is_color_found(document):
	
<<<<<<< HEAD
	color_found=False

	for para in document.paragraphs:
			
		para_color=None
		if para.style.font.color.rgb:
				para_color=para.style.font.color.rgb
		
		for run in para.runs:
				
			final_color=None

			if run.font.color.rgb:
				final_color=run.font.color.rgb
			
			if run.style.font.color.rgb:
				final_color=run.style.font.color.rgb
			
			if not final_color:
				final_color=para_color

			if final_color:
				color_found=True
				print(run.text + " " + str(final_color))
				#break 
		
		#if color_found:
		#	break
	return color_found

document =  Document('/home/navkrishna/Downloads/demo.docx')

if is_color_found(document):
	print("your color may contain blue/red text")
else:
	print("no color exists in your document")
#document.save()
