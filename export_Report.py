import json
import http.server
import socketserver
import webbrowser
import os
import argparse

def exportCSV(images,dupImages):
    print("What would you like the file name to be?\nPlease keep in mind that any existing CSV files under the same name will be overwritten.\n\n")
    fileName = input()+".csv" #adds the appropriate suffix to a file name
    #print(fileName)
    file = open(fileName, mode='w')
    
    file.write("Unique Images:\n")
    if images:  #error handling, checks if there's any unique images at all
        for key in images:
            file.write(f"{images[key]}: {key}\n")
    else:
        file.write("No unique images detected.\n")
    file.write("\n")
    file.write("Duplicate Images:\n")
    if dupImages:
        for key in dupImages:
            file.write(f"{key}: {dupImages[key]}\n")
    else:
        file.write("No duplicates detected.\n")
    file.close()
    print("\n||- Report complete -||")
    input("\n[Press ENTER to return]")
    
def exportHTML(images,dupImages,port,path):
    data = {
        "images": images,
        "dupImages": dupImages,
        "path": path
    }
    print(data)
    
    with open("report.json",'w') as file:
        json.dump(data,file)
    
    class MyHandler(http.server.SimpleHTTPRequestHandler):
        def endHeaders(self):
            self.send_header('Access-Control-Allow-Origin','*')
            super().end_headers()
    Handler = MyHandler
    
    with socketserver.TCPServer(("",port), Handler) as httpd:
        print(f"Serving with port: {port}")
        webbrowser.open(f'http://localhost:{port}/index.html')
        httpd.serve_forever()