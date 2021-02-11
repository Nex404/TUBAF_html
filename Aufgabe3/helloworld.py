import webbrowser

#Textdatei erstellen

zahl = 12
f = open("helloworld.html", "w")

message = f"<html> \
<head>\
    <title>HelloWorld</title>\
</head>\
<body>\
<p>Hello World!{zahl}</p>\
</body>\
</html>"

f.write(message)
f.close()

webbrowser.open_new_tab("helloworld.html")