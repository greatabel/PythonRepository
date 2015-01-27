# coding:utf-8
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

def escape_html(text):
	text = text.replace("&","&amp;")
	text = text.replace("<","&lt;")
	text = text.replace(">","&gt;")
	return text

def print_start():
	print("<table border='1'>")
def print_end():
	print("</table>")

def print_line(line,color,maxwidth):
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
				print("<td align='right'>{0:d}</td>".format(round(x)))
			except ValueError:
				field = field.title()
				print("field here=", field)
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
	while True:
		try:
			line = input()
			if count == 0:
				color = "lightgreen"
			elif count %2 :
				color = "white"
			else:
				color = "lightyellow"
			print_line(line, color, maxwidth)
		except EOFError:
			break
	print_end()


import sys
main()


