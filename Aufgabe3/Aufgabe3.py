import webbrowser

name = input("Wie ist dein Name? : ")

# html message
message = f"\
    <html>\
        <head>\
            <title>Website von {name}</title>\
        </head>\
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8'/>\
        <body>\
            <h1>Willkommen auf meiner Seite!</h1>\
            Dies ist meine Seite <br>\
            Mein Name ist {name}.\
        </body>\
    </html>"

f = open("meine_website.html", "w")

f.write(message)
f.close()

webbrowser.open_new_tab("meine_website.html")