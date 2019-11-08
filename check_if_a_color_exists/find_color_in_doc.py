from docx import Document
from docx.shared import RGBColor

document =  Document('/home/navkrishna/Downloads/demo.docx')

color_to_check=RGBColor(0x4F, 0x81, 0xBD) #add the hex code of the color to find

color_found=False

for para in document.paragraphs:
		
	para_color=None
	if para.style.font.color.rgb:
			para_color=para.style.font.color.rgb
	
	for run in para.runs:
			
		final_color=None
		if run.style.font.color.rgb:
			final_color=run.style.font.color.rgb

		if run.font.color.rgb:
			final_color=run.font.color.rgb

		if not final_color:
			final_color=para_color

		if final_color:
			if final_color==color_to_check:
				color_found=True 
			#print(run.text + " "+ str(final_color))


if color_found:
	print("the color " + str(color_to_check) + " is found in your document")
else:
	print("the color " + str(color_to_check) + " is not found")
#document.save()

