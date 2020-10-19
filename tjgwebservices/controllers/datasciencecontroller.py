#!/usr/bin/env python3
""
import cgitb
from urllib.parse import urlparse
from urllib.parse import parse_qs
import cgi
import hashlib
import sys
import psycopg2
from xml.dom import minidom
from tjgwebservices.models.sqlmodel import SQLDoc
from tjgwebservices.models.xmlmodel import XMLDoc
from tjgwebservices.views.tjgtemplate.templatedatascience import *
from tjgwebservices.views.tjgtemplate.datasciencesheets import *
from tjgwebservices.controllers.utils.loggerinitializer import *

cgitb.enable(display=0, logdir="/var/log/pythoncgi/")

class DataScienceController():

    def drawTemplate(self):
        self.templatetext= ''.join(self.buildDSTemplate())
        self.writeToResponse(self.templatetext)
        self.writeToClose()
        self.templatetext = ""
        self.templatemodule = []

    def writeToResponse(self, text):
        self.handler.wfile.write(bytes(str(text), "utf-8")) 
     
    def writeToClose(self):
        if not self.handler.wfile.closed:
            #self.handler.wfile.closed = True
            self.handler.wfile.flush()
            #self.handler.wfile.detach()

    def buildDSTemplate(self):        
        loggedin = False
        lrobj = self.retrieveRedirect()
        if lrobj is not None:
            if (lrobj[0]=="register"):
                self.newRegister()
            else:
                cl = self.checkLogin(lrobj)
                ui = 0
                if (cl == True):
                    ui = self.checkUser()
                if (ui > 0):
                    loggedin = True
        if loggedin:
            if (lrobj[0]=="editprofile"):
                    self.editProfile()
            if (lrobj[0]=="goal"):	
                    self.submitGoal()
        doc = minidom.parse('tjgwebservices/views/static/xml/dscatalog.xml')
        x = XMLDoc(doc)
        #heading = x.retrieveValue('heading')
        headingtitle = x.retrieveValue('headingtitle')
        headingdescription = x.retrieveValue('headingdescription')
        hd = DSHead("/","GET")
        self.templatemodule.append(hd.templatetext)
        del hd
        self.templatemodule.append("<body>")
        lm = LoginModal("/","GET")
        self.templatemodule.append(lm.templatetext)
        del lm
        rm = RegisterModal("/","GET")
        self.templatemodule.append(rm.templatetext)
        del rm
        tn = DSTopNav("/","GET")
        self.templatemodule.append(tn.templatetext)
        del tn
        self.templatemodule.append("<main>")
        self.templatemodule.append("<aside>")
        obj = [x.retrieveLinks2('links'), 
                x.retrieveLinks2('additionallinks'), 
                x.retrieveLinks2('sitelinks')]
        sn = DSSideNav("/","GET",obj)
        self.templatemodule.append(sn.templatetext)
        del sn
        si = DSSideImg("/","GET",x.retrieveImages())
        self.templatemodule.append(si.templatetext)
        del si
        self.templatemodule.append(' <a href="//iidataschool.com/">')
        self.templatemodule.append('	<h1>'+headingtitle+'</h1>')
        self.templatemodule.append('	<img src="img/iidataschool0001.png" class="adbanner" style="margin: 0 auto;width: 100%;" />')
        self.templatemodule.append(" </a>\n")
        self.templatemodule.append(' <a href="//iidataschool.com/">')
        self.templatemodule.append('	<h1>'+headingtitle+'</h1>')
        self.templatemodule.append('	<img src="img/iidataschool0002.png" class="adbanner" style="margin: 0 auto;width: 100%;" />')
        self.templatemodule.append(" </a>\n")
        self.templatemodule.append(' <a href="//iidataschool.com/">')
        self.templatemodule.append('	<h1>'+headingtitle+'</h1>')
        self.templatemodule.append('	<img src="img/iidataschool0003.png" class="adbanner" style="margin: 0 auto;width: 100%;" />')
        self.templatemodule.append(" </a>\n")
        ca = DSCalendar("/","GET","")
        self.templatemodule.append(ca.templatetext)
        del ca
        self.templatemodule.append('</aside>')
        self.templatemodule.append('<div>')
        self.templatemodule.append('<header>')
        self.templatemodule.append('	<img src="img/AIMLBD_ad0001.png" class="adbanner" width="720" height="90" style="margin: 0 auto;width: 100%;">')
        self.templatemodule.append('	<h1>'+headingtitle+'</h1>')
        self.templatemodule.append('	<p>'+headingdescription+'</p>')
        self.templatemodule.append('	<p><a href="#">Learn more</a></p>')
        self.templatemodule.append(' <span>')
        fi = Figures("/","GET",x.retrieveFigures())
        self.templatemodule.append(fi.templatetext)
        del fi
        self.templatemodule.append(' </span>')
        self.templatemodule.append(' </header>')
        if loggedin:
            self.templatemodule.append('<p>Welcome '+self.username+"</p>")
        self.templatemodule.append('<p>'+self.message+'</p>')
        self.templatemodule.append(' <div id="pageElement">')
        self.templatemodule.append(' </div>')
        if loggedin:
            ar = Articles("/","GET",x.retrieveArticles())
            self.templatemodule.append(ar.templatetext)
            del ar
        self.templatemodule.append('</div>')
        self.templatemodule.append('<div class="datasciencebook">')
        nb = NavBook("/","GET","II Data School")
        self.templatemodule.append(nb.templatetext)
        del nb
        bo = Pages("/","GET",x.retrievePages())
        self.templatemodule.append(bo.templatetext)
        del bo
        self.templatemodule.append('</div>')
        self.templatemodule.append('</main>')
        fr = FooterObject("/","GET","II Data School of Science - II Data School","0.0.0.1")
        self.templatemodule.append(fr.templatetext)
        del fr
        return self.templatemodule
        
    def buildSheetsTemplate(self, arg1):
        self.writeToResponse(TemplateSheets(arg1).templatetext)
        self.writeToClose()

    def __init__(self,  arg1,  handler1):
        self.templatetext = ""
        self.templatemodule = []
        doc = minidom.parse('tjgwebservices/views/static/xml/sqlconfig.xml')
        self.s = SQLDoc(doc)
        dsdb = self.s.retrieveDatabase()
        self.form = cgi.FieldStorage()
        self.db = psycopg2.connect(host=dsdb['hostname'],dbname=dsdb['dbname'], user=dsdb['dbuser'], password=dsdb['dbpassword'], port=5432)
        self.message = ""
        self.username = ""
        self.argpath = arg1.split('?')[0]
        logging.info("Argument Path: "+self.argpath)
        self.handler = handler1


    def retrieveRedirect(self):
        self.form = cgi.FieldStorage()
        url = self.handler.fullpath
        parsed = urlparse(url) 
        sURL = parse_qs(parsed.query)
        loginredirect = sURL.get('loginredirect')
        return loginredirect


    def checkLogin(self,loginredirect):
        self.loginredirect = loginredirect
        form = self.form
        if not loginredirect:
            loginredirect = ""
            return False
        else:
            loginredirect = loginredirect[0]
            if (loginredirect=="login"):
                if not form["uname"]:
                    self.username = ""
                    return False
                else:
                    if not form["psw"]:
                        using_password = 0
                        password = ""
                        return False
                    else:
                        using_password = 1
                        return True

    def checkUser(self):
        form = self.form
        db = self.db
        cur = db.cursor()
        if not form["uname"]:
            return 0
        if not form["psw"]:
            return 0
        username = form.getvalue("uname")
        if (username == "1"):
            self.message="Invalid Password"
            return 0	        
        #password =  hashlib.md5(form.getvalue('psw')).hexdigest()
        password =  form.getvalue('psw')
        preexecutions = self.s.retrievePreExecutions()
        for preexecution in preexecutions:
            cur.execute(preexecution) 
        query = "SELECT COUNT(*) FROM  `ds_users` WHERE `username` = '"+str(username)+"' AND `password`= md5('"+str(password)+"')"
        cur.execute(query)
        result = cur.fetchone()
        number_of_rows = result[0]
        db.commit()
        if number_of_rows == 1:
            self.username = username
            query1 = "SELECT `id` FROM  `ds_users` WHERE `username` = '"+str(username)+"';"
            cur.execute(query1)
            result = cur.fetchone()
            userid = result[0]
            return userid
        else:
            self.message="Invalid Password"
            return 0


    def newRegister(self):
        form = self.form
        db = self.db
        cur = db.cursor()
        if ((form.getvalue('uname') == "1")  or (form.getvalue('psw') == "1")):
            self.message = "Invalid registration"
            return self.message
        username = form.getvalue('uname')
        useremail = form.getvalue('email')
        password =  hashlib.md5(form.getvalue('psw')).hexdigest()
        nameuser = form.getvalue('name')
        region = form.getvalue('region')
        profession = form.getvalue('profession')
        referred = form.getvalue('referred')
        sqlquery = """INSERT INTO `ds_users` (`name`,`username`,`email`,`password`,`params`) VALUES (%s,%s,%s,%s,%s)"""
        sqlvalues = (nameuser, username, useremail, password, 'new_user')
        try:
            cur.execute(sqlquery, sqlvalues)
            sqlquery2 = "SELECT `id` FROM  `ds_users` WHERE `username` = '%s'"
            sqlvalues2 = (username)
            cur.execute(sqlquery2,sqlvalues2)
            db.commit()
            for row in cur:				
                sqlquery3 = """INSERT INTO `ds_user_profiles`(`user_id`,`region`,`profession`,"
                "`referred`, `profile_status`,`last_visited`) VALUES (%s,%s,%s,%s,'active', NOW())"""
                sqlvalues3 = (region, profession, referred)
                cur.execute(sqlquery3, sqlvalues3)
                db.commit()
                if cur.rowcount:
                    self.message = str(cur.rowcount) + ' records inserted'
                else:
                    self.message = 'last insert id not found'
        finally:
            db.close()


    def editProfile(self):
        form = self.form
        db = self.db
        cur = db.cursor()
        userid = form.getvalue("userid")
        region = form.getvalue("region")
        profession = form.getvalue("profession")
        referred = form.getvalue("referred")
        sqlquery = "UPDATE `ds_user_profiles` SET `region`='%s',"
        "`profession`='%s', `referred`='%s'"
        " WHERE `user_id` = '%s'"
        sqlvalues = (region, profession, referred, userid)
        try:
            cur.execute(sqlquery, sqlvalues)
            db.commit()
            if cur.rowcount:
                self.message = str(cur.rowcount) + ' records inserted'
            else:
                self.message = 'last insert id not found'
        finally:
            db.close()


    def submitGoal(self):
        form = self.form
        db = self.db
        cur = db.cursor()
        userid = form.getvalue("userid")
        goal = form.getvalue("desc")
        sqlquery = """INSERT INTO `ds_goals`(`creator_id`, `goal`, `submissionDate`, `startDate`, `endDate`) VALUES (%s,%s, NOW(),NOW(),NOW())"""
        sqlvalues = (userid, goal)
        try:
            cur.execute(sqlquery, sqlvalues)
            db.commit()
            if cur.rowcount:
                self.message = str(cur.rowcount) + ' records inserted'
            else:
                self.message = 'last insert id not found'
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            sys.stderr.write(e)
            return None
        finally:
            db.close()


    def submitListing(self):
        form = self.form
        db = self.db
        cur = db.cursor()
        userid = form.getvalue("userid")
        listingdesc = form.getvalue("desc")
        listingcontact = form.getvalue("contact")
        listingurl = form.getvalue("url")
        sqlquery = """INSERT INTO `ds_business_listings`(`author_id`,`url`,`contact_info`, `description`,`submissionDate`) VALUES(%s,%s, %s, %s,NOW())"""
        sqlvalues = (userid, listingurl, listingcontact, listingdesc)
        try:
            cur.execute(sqlquery, sqlvalues)
            db.commit()
            if cur.rowcount:
                self.message = str(cur.rowcount) + ' records inserted'
            else:
                self.message = 'last insert id not found'
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            sys.stderr.write(e)
            return None
        finally:
            db.close()



    def submitPost(self):
        form = self.form
        db = self.db
        cur = db.cursor()
        userid = form.getvalue("userid")
        postcontent = form.getvalue("postcontent")
        posttitle = form.getvalue("posttitle")
        postexcerpt = form.getvalue("postexcerpt")
        poststatus = form.getvalue("poststatus")
        guid = form.getvalue("guid")
        sqlquery = """INSERT INTO `ds_posts` (`user_id`, `blog_date`, `blog_date_gmt`, `blog_content`, `blog_title`, `blog_excerpt`, `blog_status`, `blog_modified`, `blog_modified_gmt`, `guid`, `menu_order`, `blog_type`) VALUES (%s, NOW(), NOW(), %s, %s, %s, %s, NOW(), NOW(), %s, 0, 'post')"""
        sqlvalues = (userid, postcontent, posttitle, postexcerpt, poststatus, guid)
        try:
            cur.execute(sqlquery, sqlvalues)
            db.commit()
            if cur.rowcount:
                self.message = str(cur.rowcount) + ' records inserted'
            else:
                self.message = 'last insert id not found'
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            sys.stderr.write(e)
            return None
        finally:
            db.close()    
