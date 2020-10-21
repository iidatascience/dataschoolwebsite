#!/usr/bin/env python3
import http.server
from tjgwebservices.controllers.datasciencecontroller import DataScienceController
from tjgwebservices.views.tjgtemplate.datasciencesheets import TemplateSheets
from tjgwebservices.views.tjgtemplate.datasciencesheets import PostSheets
from tjgwebservices.controllers.utils.loggerinitializer import *
from io import BytesIO
from io import StringIO
import cgi
import psycopg2
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from xml.dom import minidom
import cgitb
from tjgwebservices.models.sqlmodel import SQLDoc
cgitb.enable(display=0, logdir="/var/log/pythoncgi/")

class WebHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
    def do_GET(self):
        ts = TemplateSheets()
        self.csspaths = ts.csspaths
        self.jspaths = ts.jspaths
        self.pagpaths = ts.pagpaths
        self.fullpath = self.path
        pathurl = self.path.split('?')[0]
        pathprefix = "tjgwebservices/views"
        if pathurl in ts.paths:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            ds = DataScienceController(self.path, self)
            ds.drawTemplate()
            del ds
            del ts
        elif pathurl in self.csspaths:
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            filepath = pathprefix +self.path
            filepath = filepath.split('?')[0]
            self.wfile.write(bytes(str(
                "".join(open(filepath,'r').readlines())
                ), "utf-8")) 
        elif pathurl in self.jspaths:
            self.send_response(200)
            self.send_header("Content-type", "text/js")
            self.end_headers()
            filepath = pathprefix +self.path
            filepath = filepath.split('?')[0]
            self.wfile.write(bytes(str(
                "".join(open(filepath,'r').readlines())
                ), "utf-8")) 
        elif pathurl in self.pagpaths:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            #filepath = pathprefix +self.path
            basepath = self.path.split('?')[0]
            filepath = 'tjgwebservices/views'+basepath+'.tpl'
            self.wfile.write(bytes(str(
                "".join(open(filepath,'r').readlines())
                #"".join(open(filepath,'r').readlines())
                ), "utf-8")) 
        elif pathurl[:3] == "img" or pathurl[:4] == "/img":
            imageprefix = "tjgwebservices/views/static"
            filepath = imageprefix +self.path
            filepath = filepath.split('?')[0]
            f = open(filepath, 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        else:
            pass
    
    def do_POST(self):
        ts = PostSheets()
        #self.send_response(200)
        #self.send_header("Content-type", "text/html;charset=utf-8")
        #self.end_headers()
        self.fullpath = self.path
        pathurl = self.path.split('?')[0]
        if pathurl in ts.postpaths:
            doc = minidom.parse('tjgwebservices/views/static/xml/sqlconfig.xml')
            self.s = SQLDoc(doc)
            dsdb = self.s.retrieveDatabase()
            #self.form = cgi.FieldStorage()
            self.db = psycopg2.connect(host=dsdb['hostname'],dbname=dsdb['dbname'], user=dsdb['dbuser'], password=dsdb['dbpassword'], port=dsdb['dbport'])
            db =self.db
            cur = db.cursor()
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            fields = parse_qsl(body)[1]
            elements = fields[1][1]
            #self.wfile.write(str(fields))
            self.send_response(200)
            self.end_headers()
            response = BytesIO()
            #response.write(b'This is POST request. ')
            #response.write(b'Received: ')
            conversationid = str(elements)
            if pathurl == '/chat/getconversation':
                sqlquery = "SELECT date_time,message,user_id_to FROM ds_user_conversations WHERE user_id_from = %s OR user_id_to = %s ORDER BY date_time ASC"
                sqlvalues = (conversationid,conversationid)
                cur.execute(sqlquery,sqlvalues)
                db.commit();
                if cursor.rowcount > 0:
                    jsonstring = '['
                    for row in cur:
                        dt = row[0]
                        me = row[1]
                        ut = row[2]
                        jsonstring = jsonstring+' {"to":"'+ut+'","time":"'+dt+'","message":"'+me+'"},'
                    jsonstring = jsonstring[0:-1]
                    response.write(jsonstring)
                else:
                    response.write(b'[]')
                self.wfile.write(response.getvalue())
            elif pathurl == '/chat/checkconversation':
                sqlquery = "SELECT date_time, message, user_id_to FROM ds_user_conversations WHERE user_id_from = %s OR user_id_to = %s ORDER BY date_time ASC"
                sqlvalues = (conversationid,conversationid)
                cur.execute(sqlquery,sqlvalues)
                db.commit();
                if cur.rowcount > 0:
                    jsonstring = '['
                    for row in cur:
                        dt = row[0]
                        me = row[1]
                        ut = row[2]
                        jsonstring = jsonstring+' {"to":"'+ut+'","time":"'+dt+'","message":"'+me+'"},'
                    jsonstring = jsonstring[0:-1]
                    response.write(jsonstring)
                else:
                    response.write(b'[]')
                self.wfile.write(response.getvalue())
