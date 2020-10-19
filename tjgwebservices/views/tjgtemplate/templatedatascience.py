#!/usr/bin/env python3

class DSHead():
    
    def printTemplateHead(self):
        templateHeader = "".join(open('tjgwebservices/views/static/dsheader.tpl','r').readlines())
        templateHeader = templateHeader.replace("{website.title}","II Data School")
        templateHeader = templateHeader.replace("{website.version}","0.0.0.0.1")
        return templateHeader

       
    def __init__(self,arg1,arg2):
        self.pathname = arg1
        self.method = arg2
        self.templatetext = ""
        self.templatetext= self.printTemplateHead()

class DSTopNav():
    

    def printTopNav(self):
        templateHeader = "".join(open('tjgwebservices/views/static/dstopnav.tpl','r').readlines())
        return templateHeader


    def __init__(self,arg1,arg2):
        self.pathname = arg1
        self.method = arg2
        self.templatetext = ""
        self.templatetext= self.printTopNav()

class DSSideNav():
    
    def printSideNav(self):
        self.templatemodule.append('<img src="img/iidataschool_logo1.png" alt="Logo" title="Logo" style="background:#fff;width:100%;display:block;float:left;clear: both;" />')
        self.templatemodule.append('<ul>')
        self.templatemodule.append('<li>Menu</li>')
        for ref in self.l:
            self.templatemodule.append('<li><a href="http://'+str(ref[0][1])+'">'+str(ref[0][0])+'</a></li>\n')
        self.templatemodule.append('<li>Additional References</li>')
        for ref in self.addl:
            self.templatemodule.append('<li><a href="http://'+str(ref[0][1])+'">'+str(ref[0][0])+'</a></li>\n')
        self.templatemodule.append('<li>Sites</li>')
        for ref in self.sitel:
            self.templatemodule.append('<li><a href="http://'+str(ref[0][1])+'">'+str(ref[0][0])+'</a></li>\n')
        self.templatemodule.append('</ul>')
        self.templatemodule.append('<hr />')
        self.templatemodule.append('<ul>')
        self.templatemodule.append('<li><button class="loginbtn" onclick="document.getElementById(\'id01\').style.display=\'block\'">Login</button></li>')
        self.templatemodule.append('<li><button class="loginbtn" onclick="document.getElementById(\'id02\').style.display=\'block\'">Register</button></li>')
        self.templatemodule.append('</ul>')
        self.templatemodule.append('<hr />')
        return self.templatemodule



    def __init__(self,arg1, arg2, arg3):
        self.pathname = arg1
        self.method = arg2
        self.l = arg3[0]
        self.addl = arg3[1]
        self.sitel = arg3[2]
        self.templatetext = ""
        self.templatemodule=[]
        self.templatetext= ''.join(self.printSideNav())

class DSSideImg():
    
    def printImages(self):
        for image in self.images:
            self.templatemodule.append('<p><b>'+str(image[0][0])+'</b>')
            self.templatemodule.append('<img src="'+str(image[0][2])+'"')
            self.templatemodule.append(' alt="'+str(image[0][0])+'"')
            self.templatemodule.append(' title="'+str(image[0][0])+'" />')
            self.templatemodule.append( str(image[0][1]))
            self.templatemodule.append('</p>')
            self.templatemodule.append('<br/>')   
        return self.templatemodule


    def __init__(self,arg1,arg2, arg3):
        self.pathname = arg1
        self.method = arg2
        self.images = arg3
        self.templatetext = ""
        self.templatemodule = []
        self.templatetext= ''.join(self.printImages())


class DSCalendar():
    
    def printBookTemplate(self):
        self.templatemodule.append('<div id="calendarElement">')
        self.templatemodule.append('</div>')
        self.templatemodule.append('<div class="calendarTable">')
        self.templatemodule.append('		<div class="textDates" id="day">')
        self.templatemodule.append('		</div>')
        self.templatemodule.append('</div>')
        return self.templatemodule

    def __init__(self,arg1,arg2, arg3):
        self.pathname = arg1
        self.method = arg2
        self.sitetitle = arg3
        self.templatetext = ""
        self.templatemodule = []
        self.templatetext= ''.join(self.printBookTemplate())


class LoginModal(object):

    def printModal(self):
        self.templatemodule.append('	<div class="modal" id="id01">')
        self.templatemodule.append('  <span title="Close Modal" class="close" onclick="document.getElementById(\'id01\').style.display=\'none\'">x</span>')
        self.templatemodule.append('  <form action="/?loginredirect=login" method="post">')
        self.templatemodule.append('    <div class="container">')
        self.templatemodule.append('      <label for="uname"><b>Username</b></label>')
        self.templatemodule.append('      <input name="uname" required="" type="text" placeholder="Enter Username">')
        self.templatemodule.append('    <label for="psw">Password</label>')
        self.templatemodule.append('    <input name="psw" required="" type="password">')
        self.templatemodule.append('      <button class="submitbtn" type="submit">Login</button>')
        self.templatemodule.append('      <label>')
        self.templatemodule.append('        <input name="remember" type="checkbox" checked="checked"> Remember me')
        self.templatemodule.append('      </label>')
        self.templatemodule.append('		<input name="login" type="hidden" value="login">')
        self.templatemodule.append('    </div>')
        self.templatemodule.append('    <div class="container" style="background-color:#f1f1f1">')
        self.templatemodule.append('      <button class="cancelbtn" onclick="document.getElementById(\'id01\').style.display=\'none\'" type="button">Cancel</button>')
        self.templatemodule.append('      <span class="psw">Forgot <a href="#">password?</a></span>')
        self.templatemodule.append('    </div>')
        self.templatemodule.append('  </form>')
        self.templatemodule.append('</div>')
        return self.templatemodule

    def __init__(self,arg1,arg2):
        self.pathname = arg1
        self.method = arg2
        self.templatetext = ""
        self.templatemodule = []
        self.templatetext= ''.join(self.printModal())


class RegisterModal(object):
    
    def printModal(self):
        self.templatemodule.append('	<div class="modal" id="id02">')
        self.templatemodule.append('  <span title="Close Modal" class="close" onclick="document.getElementById(\'id02\').style.display=\'none\'">x</span>')
        self.templatemodule.append('<form action="/index.py?loginredirect=register" method="post">')
        self.templatemodule.append('<div class="container">')
        self.templatemodule.append('<h1>Register</h1>')
        self.templatemodule.append('<p>Please fill in this form to create an account.</p>')
        self.templatemodule.append('<hr>')
        self.templatemodule.append('<label for="name"><b>Your Name</b></label>')
        self.templatemodule.append('<input name="name" required="" type="text" placeholder="Enter Name">')
        self.templatemodule.append('<label for="uname"><b>User Name</b></label>')
        self.templatemodule.append('<input name="uname" required="" type="text" placeholder="Enter User Name">')
        self.templatemodule.append('<label for="email"><b>Email</b></label>')
        self.templatemodule.append('<input name="email" required="" type="text" placeholder="Enter Email">')
        self.templatemodule.append('<label for="region"><b>Region</b></label>')
        self.templatemodule.append('<select name="region">')
        self.templatemodule.append('<option value="americas">Americas</option>')
        self.templatemodule.append('<option value="africa">Africa</option>')
        self.templatemodule.append('<option value="asia">Asia</option>')
        self.templatemodule.append('<option value="europe">Europe</option>')
        self.templatemodule.append('</select>')
        self.templatemodule.append('<label for="profession"><b>Profession</b></label>')
        self.templatemodule.append('<select name="profession">')
        self.templatemodule.append('<option value="it">IT Professional</option>')
        self.templatemodule.append('<option value="student">Student</option>')
        self.templatemodule.append('<option value="education">Education</option>')
        self.templatemodule.append('<option value="commerce">Commerce</option>')
        self.templatemodule.append('<option value="other">Other</option>')
        self.templatemodule.append('</select>')
        self.templatemodule.append('<label for="referred"><b>Referred by</b></label>')
        self.templatemodule.append('<select name="referred">')
        self.templatemodule.append('<option value="website">Website</option>')
        self.templatemodule.append('<option value="search">Search</option>')
        self.templatemodule.append('<option value="ad">Online Ad</option>')
        self.templatemodule.append('<option value="email">Email</option>')
        self.templatemodule.append('<option value="other">Other</option>')
        self.templatemodule.append('</select>')
        self.templatemodule.append('<label for="psw"><b>Password</b></label>')
        self.templatemodule.append('<input name="psw" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" id="psw" required="" type="password" placeholder="Enter Password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}">')
        self.templatemodule.append('<label for="psw-repeat"><b>Repeat Password</b></label>')
        self.templatemodule.append('<input name="psw-repeat" id="pswconfirm" required="" type="password" placeholder="Repeat Password">')
        self.templatemodule.append('<hr>')
        self.templatemodule.append('<input name="login" type="hidden" value="register">')
        self.templatemodule.append('<div id="message">')
        self.templatemodule.append('<h3>Password must contain the following:</h3>')
        self.templatemodule.append('<p class="invalid" id="letter">A <b>lowercase</b> letter</p>')
        self.templatemodule.append('<p class="invalid" id="capital">A <b>capital (uppercase)</b> letter</p>')
        self.templatemodule.append('<p class="invalid" id="number">A <b>number</b></p>')
        self.templatemodule.append('<p class="invalid" id="length">Minimum <b>8 characters</b></p>')
        self.templatemodule.append('<p class="invalid" id="match">Confirm password <b>matches</b></p>')
        self.templatemodule.append('</div>')
        self.templatemodule.append('<p><input name="terms" required="" type="checkbox" value="agree">By creating an account you agree to our <a href="http://tjgwebservices.com/terms/" target="_blank">Terms of Service</a> and <a href="http://tjgwebservices.com/privacy/" target="_blank">Privacy Policy</a>.</p>')
        self.templatemodule.append('<p>I agree to the privacy agreement and terms of service for this site.<br></p>')
        self.templatemodule.append('<button class="registerbtn" id="register" type="submit">Register</button>')
        self.templatemodule.append('</div>')
        self.templatemodule.append('</form>')
        self.templatemodule.append('</div>')
        return self.templatemodule

    def __init__(self,arg1,arg2):
        self.pathname = arg1
        self.method = arg2
        self.templatetext = ""
        self.templatemodule = []
        self.templatetext= ''.join(self.printModal())


class Figures(object):

    def printFigures(self):
        self.templatemodule.append(' <ol>')
        self.templatemodule.append('   <li></li>')
        self.templatemodule.append('   <li></li>')
        self.templatemodule.append('   <li></li>')
        self.templatemodule.append(' </ol>')
        for fig in self.figures:
            self.templatemodule.append('<figure>')
            self.templatemodule.append('    <h1>'+fig[0][0]+'</h1>\n')
            self.templatemodule.append('    <p>'+fig[0][1]+'</p>\n')
            self.templatemodule.append('    <ul>\n')
            for fig1 in fig[0][2]:
                self.templatemodule.append('<li>'+fig1+'</li>')
            self.templatemodule.append('    </ul>\n')
            self.templatemodule.append('    </figure>\n')
        return self.templatemodule


    def __init__(self,arg1,arg2,  arg3):
        self.pathname = arg1
        self.method = arg2
        self.figures = arg3
        self.templatetext = ""
        self.templatemodule = []
        self.templatetext= ''.join(self.printFigures())

class Articles(object):


    def printArticles(self):
        self.templatemodule.append(' <article>')
        i=0
        for text in self.articles:
            self.templatemodule.append('<section><h2>'+text[0][0]+'</h2><p>')+text[0][1]+'</p><p><a class="btn" href="#">View details</a></p></section>\n'
            i +=1
            if(i==3):
                self.templatemodule.append('</article><article>\n')
                i=0
        self.templatemodule.append('</article>\n')
        return self.templatemodule

    def __init__(self,arg1,arg2,  arg3):
        self.pathname = arg1
        self.method = arg2
        self.articles = arg3
        self.templatetext = ""
        self.templatemodule = []
        self.templatetext= ''.join(self.printArticles())

class NavBook(object):

    def printBookTemplate(self):
        self.templatemodule.append('<div class="click swing panel">')
        self.templatemodule.append('<div class="first">')
        self.templatemodule.append('	<p>'+self.arg+'</p>')
        self.templatemodule.append('	<p>Welcome to '+self.arg+'</p>')
        self.templatemodule.append('</div>')
        self.templatemodule.append('<div class="front" id="text1">')
        self.templatemodule.append('	<h2>Training</h2>')
        self.templatemodule.append('</div>')
        self.templatemodule.append('<div class="last">')
        self.templatemodule.append('	<p>Training from '+self.arg+'</p>')
        self.templatemodule.append('</div>')
        self.templatemodule.append('<div class="back" id="text2">')
        self.templatemodule.append('<div class="pad">')
        self.templatemodule.append('	<h2>Training from '+self.arg+'</h2>')
        self.templatemodule.append('</div>')
        self.templatemodule.append('</div>')
        self.templatemodule.append('</div>')
        return self.templatemodule


    def __init__(self,arg1, arg2, arg3):
        self.pathname = arg1
        self.method = arg2
        self.arg = arg3
        self.templatetext = ""
        self.templatemodule = []
        self.templatetext= ''.join(self.printBookTemplate())


class Pages(object):

    def printPages(self):
        for text in self.pages:
            self.templatemodule.append(' <article class="articles">')
            self.templatemodule.append('<h2>'+text[0][0]+'</h2><p>'+text[0][1]+'</p>\n')
            self.templatemodule.append('<img src="img/imageanalysis'+str(self.r)+'.png" alt="Image Analysis" title="Image Analysis" />\n')
            self.r +=1
            if (self.r >=10):
                self.r = 1
            self.templatemodule.append('</article>\n')
        return self.templatemodule

    def __init__(self,arg1,arg2, arg3):
        self.pathname = arg1
        self.method = arg2
        self.pages = arg3
        self.r = 1
        self.templatetext = ""
        self.templatemodule = []
        self.templatetext= ''.join(self.printPages())

		
class FooterObject(object):

    def printFooter(self):
        self.templatemodule.append('<footer>')
        self.templatemodule.append('        <p>'+self.footertitle+'</p>')
        self.templatemodule.append('</footer>')
        self.templatemodule.append('</body>')
        self.templatemodule.append('<script src="/static/js/slideshow.js?v=0.'+self.version+'"></script>')
        self.templatemodule.append('<script src="/static/js/validation.js?v=0.'+self.version+'"></script>')
        self.templatemodule.append('<script src="/static/js/dsscript.js?v=0.'+self.version+'"></script>')
        self.templatemodule.append('<script src="/static/js/book.js?v=0.'+self.version+'"></script>')
        self.templatemodule.append('<script src="/static/js/calendar.js?v=0.'+self.version+'"></script>')
        self.templatemodule.append('<script src="/static/js/chat.js?v=0.'+self.version+'"></script>')
        self.templatemodule.append('</html>')
        return self.templatemodule

    def __init__(self,arg1,arg2, arg3, arg4):
        self.pathname = arg1
        self.method = arg2
        self.footertitle = arg3
        self.version = arg4
        self.templatetext = ""
        self.templatemodule = []
        self.templatetext= ''.join(self.printFooter())

