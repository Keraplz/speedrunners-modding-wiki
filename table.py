# Creates HTML tables.
# each line of s should be in the following format:
# key | value

s = ""

properties = []
for line in s.split("\n"):
  name, default_value = line.split(" | ")
  properties.append((name, default_value))

html = ""
html += "<table width=100%>"
html += "<tr>"
html += "<th>Property name</th>"
html += "<th>Default value</th>"
html += "</tr>"

for key, value in properties:
  html += "<tr>"
  html += f"<td>{key}</td>"
  html += f"<td>{value}</td>"
  html += "</tr>"

html += "</table>"

print(html)
