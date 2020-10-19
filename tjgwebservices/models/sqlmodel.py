#!/usr/bin/env python3
""
import cgitb
cgitb.enable(display=0, logdir="/var/log/pythoncgi/")

class SQLDoc(object):
    def __init__(self, doc):
        self.doc = doc


    def retrieveDatabase(self):
        config = self.doc.getElementsByTagName('database')[0].getElementsByTagName('configuration')[0]
        hostname = config.getElementsByTagName('hostname')[0].firstChild.nodeValue
        dbname = config.getElementsByTagName('dbname')[0].firstChild.nodeValue
        dbuser = config.getElementsByTagName('dbuser')[0].firstChild.nodeValue
        dbpassword = config.getElementsByTagName('dbpassword')[0].firstChild.nodeValue
        d = {'hostname':hostname,'dbname':dbname,'dbuser':dbuser,'dbpassword':dbpassword}
        return d

    def retrievePreExecutions(self):
        p = []
        preexecutions = self.doc.getElementsByTagName('database')[0].getElementsByTagName('preexecutions')[0]
        for preexecution in preexecutions:
            p.append(preexecution.childNodes[0].nodeValue.strip())
        return p

    def retrieveQueries(self):
        queries = self.doc.getElementsByTagName('database')[0].getElementsByTagName('queries')[0]
        return queries

    def retrieveQuery(self,querytype):
        queries = self.doc.getElementsByTagName('database')[0].getElementsByTagName('queries')[0]
        for query in queries:
            if query.getAttribute("type") == querytype:
                return query.childNodes[0].nodeValue.strip()

