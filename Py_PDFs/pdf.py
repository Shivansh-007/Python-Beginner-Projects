import PyPDF2

# rb: reading binary files
with open("dummy.pdf", "rb") as file:
	#print(file)
	reader = PyPDF2.PdfFileReader(file)
	#print(reader.numPages)
	#print(reader.getPage(0))
	page = reader.getPage(0)
	page.rotateCounterClockwise(90) #won't work until the above command is added since it should be a page object.
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)