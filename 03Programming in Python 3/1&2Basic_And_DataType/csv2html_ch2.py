# coding:utf-8
#实用方法: csv2html_ch2.py <test.csv >test.html
#实用方法: python3 csv2html_ch2.py maxwidth=3 format=0.2f  <test.csv >test.html
def extract_fields(line):
	fields =[]
	field =""
	quote = None
	for c in line:
		if c in "\"":
			if quote is None: #start of quoted string
				quote = c
			elif quote == c : # end of quoted string
				quote = None
			else:
				field += c #other quote inside quoted string
			continue
		if quote is None and c == ",": #end of field
			fields.append(field)
			field = ""
		else:
			field += c
	if field:
			fields.append(field)
	# print("fields =*{0}".format(fields))
	return fields

import xml.sax.saxutils
def escape_html(text):
	return xml.sax.saxutils.escape(text)
	# text = text.replace("&","&amp;")
	# text = text.replace("<","&lt;")
	# text = text.replace(">","&gt;")
	# return text

def print_start():
	print("<table border='1'>")
def print_end():
	print("</table>")

def print_line(line,color,maxwidth,myformat):
	print("<tr bgcolor='{0}'>".format(color))
	fields = extract_fields(line)
	# print("fields={0}".format( fields))				
	for field in fields:
		# print("field=", field)
		if not field:
			print("<td></td>")
		else:
			number = field.replace(",", "")
			try:
				x = float(number)
				# print("<td align='right'>{0:d}</td>".format(round(x)))
				y=myformat
				print("<td align='right'>{0:{1}}</td>".format(x,y))
			except ValueError:
				field = field.title()
				# t = escape_html("<")
				# print("field here=",t )
				field = field.replace(" And ", " and ")
				if len(field) <= maxwidth:
					field = escape_html(field)
				else:
					field = "{0}..".format(
						escape_html(field[:maxwidth]))
				print("<td>{0}</td>".format(field))
	print("</tr>")

def main():
	maxwidth = 100
	print_start()
	count = 0

	myformat = '.0f'
#处理输入新加的参数
	inputs = sys.argv[1:]
	if 'maxwidth=' in inputs[0]:
		maxwidth = int(inputs[0].replace("maxwidth=",""))
		print("maxwidth={0}".format(maxwidth))
	if 'format=' in inputs[1]:
		myformat = inputs[1].replace("format=","")
	while True:
		try:
			line = input()
			if count == 0:
				color = "lightgreen"
			elif count %2 :
				color = "white"
			else:
				color = "lightyellow"
			print_line(line, color, maxwidth,myformat)
		except EOFError:
			break
	print_end()


import sys
main()


