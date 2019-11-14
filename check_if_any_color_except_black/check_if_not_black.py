from docx import Document
from docx.shared import RGBColor
from colorsys import rgb_to_hsv 
from docx.enum.dml import MSO_COLOR_TYPE

def is_black(color):
	r=int( color[:2],16 )
	g=int( color[2:4],16 )
	b=int( color[4:6],16 )

	r, g, b = [x/255.0 for x in [r, g, b]]
	h,s,v=rgb_to_hsv(r,g,b)
	if v < 0.3:
		return True
	
def is_color_found(document):
	
	color_found=False

	for para in document.paragraphs:
			
		para_color=None
		
		if para.style.font.color.rgb:
			para_color=para.style.font.color.rgb
		
		for run in para.runs:

			if run.text.isspace():
				continue	
			
			final_color=None  
  
			if run.font.color.rgb or run.font.color.type:

				if run.font.color.type == MSO_COLOR_TYPE.AUTO:
					final_color=RGBColor(0x00, 0x00, 0x00)
				else:
					final_color=run.font.color.rgb
			
			if run.style.font.color.rgb or run.style.font.color.type:

				if run.style.font.color.type == MSO_COLOR_TYPE.AUTO:
					final_color=RGBColor(0x00, 0x00, 0x00)
				else:	
					final_color=run.style.font.color.rgb

			if not final_color:
				final_color=para_color  

			if final_color and not is_black( str( final_color) ) :
				color_found=True
				#print(run.text + " " + str(final_color))
				break
		if color_found:
			break
	return color_found


document =  Document("/home/navkrishna/Downloads/Summer Internship Report.docx")

if is_color_found(document):
	print("your Doc may contain blue/red text")
else:
	print("no color exists in your document")
#document.save()
