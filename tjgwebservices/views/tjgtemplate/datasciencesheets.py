class TemplateSheets():
    templatetext = ""
    mainstylesheet = ""
    javascriptsheet = ""
    paths = ["/", "/home", "/index", "/error"]
    csspaths = ["/static/css/dsmain.css", 
            "/static/css/book.css",
            "/static/css/calendar.css", 
            "/static/css/chat.css",  
            "/static/css/form.css",  
            "/static/css/page.css",  
            "/static/css/style.css", 
            "/static/css/heading.css"]
    jspaths = ["/static/js/dsscript.js", 
            "/static/js/book.js", 
            "/static/js/calendar.js", 
            "/static/js/chat.js", 
            "/static/js/slideshow.js", 
            "/static/js/validation.js"]
    pagpaths = ["/static/pages/datascience/visualization",
                "/static/pages/datascience/training",
                "/static/pages/datascience/topics",
                "/static/pages/datascience/services",
                "/static/pages/datascience/research",
                "/static/pages/datascience/reports",
                "/static/pages/datascience/register",
                "/static/pages/datascience/projects",
                "/static/pages/datascience/products",
                "/static/pages/datascience/home",
                "/static/pages/datascience/covid19",
                "/static/pages/datascience/contact",
                "/static/pages/datascience/config",
                "/static/pages/datascience/applications",
                "/static/pages/datascience/analysis",
                "/static/pages/datascience/about"]


    def printMainStyleSheet(self):
        self.mainstylesheet= "".join(open('tjgwebservices/views/static/css/main.css','r').readlines())
        return self.mainstylesheet;

    def printJavaScriptSheet(self):
        self.javascriptsheet = "".join(open('tjgwebservices/views/static/js/script.js','r').readlines())
        return self.javascriptsheet;

    def __init__(self):
        #self.templateName = arg1
        #if self.templateName == "/static/css/main.css":
        #    self.templatetext = self.printMainStyleSheet()
        #elif self.templateName == "/static/js/script.js":
        #   self.templatetext = self.printJavaScriptSheet() 
        pass

class PostSheets():

    postpaths = ["/chat/checkconversation", 
            "/chat/newconversation",
            "/chat/continueconversation"]

    def __init__(self):
        pass
