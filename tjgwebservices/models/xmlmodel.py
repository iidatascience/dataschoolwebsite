#!/usr/bin/env python3
""
import cgitb
cgitb.enable(display=0, logdir="/var/log/pythoncgi/")

class XMLDoc(object):
	def __init__(self, doc):
		self.doc = doc

	def retrieveValue(self,value):
		return self.doc.getElementsByTagName(value)[0].childNodes[0].nodeValue.strip()

	def retrieveLinks(self,value):
		l = []
		links = self.doc.getElementsByTagName(value)[0].getElementsByTagName('link')
		for link in links:
			l.append(link.childNodes[0].nodeValue.strip())
		return l

	def retrieveLinks2(self,value):
		l = []
		links = self.doc.getElementsByTagName(value)[0].getElementsByTagName('link')
		for link in links:
			el = []
			title = link.getElementsByTagName('title')[0].childNodes[0].nodeValue.strip()
			url = link.getElementsByTagName('url')[0].childNodes[0].nodeValue.strip()
			el.append([title,url])
			l.append(el)
		return l

	def retrieveFigures(self):
		f = []
		figures=self.doc.getElementsByTagName('figures')[0].getElementsByTagName('figure')
		for figure in figures:
			ef = []
			title = figure.getElementsByTagName('title')[0].childNodes[0].nodeValue.strip()
			description = figure.getElementsByTagName('description')[0].childNodes[0].nodeValue.strip()
			figurelist = figure.getElementsByTagName('list')[0].getElementsByTagName('element')
			listarray = []
			for element in figurelist:
				listarray.append(element.childNodes[0].nodeValue.strip())
			ef.append([title,description,listarray])
			f.append(ef)
		return f

	def retrieveArticles(self):
		a = []
		articles=self.doc.getElementsByTagName('articles')[0].getElementsByTagName('article')
		for article in articles:
			ea = []
			title = article.getElementsByTagName('title')[0].childNodes[0].nodeValue.strip()
			section = article.getElementsByTagName('section')[0].childNodes[0].nodeValue.strip()
			ea.append([title,section])
			a.append(ea)
		return a

	def retrieveSystems(self):
		s = []
		systems=self.doc.getElementsByTagName('systems')[0].getElementsByTagName('system')
		for system in systems:
			es = []
			requirements = system.getElementsByTagName('requirement')
			sr = []
			for requirement in requirements:
				sr.append(requirement.childNodes[0].nodeValue.strip())
			assets = system.getElementsByTagName('assets')[0].getElementsByTagName('asset')
			sa = []
			for asset in assets:
				sa.append([asset.childNodes[0].nodeValue.strip(),asset.getAttribute("value")])
			liabilities = system.getElementsByTagName('liabilities')[0].getElementsByTagName('liability')
			sl = []
			for liability in liabilities:
				sl.append([liability.childNodes[0].nodeValue.strip(),liability.getAttribute("value")])
			es.append([sr,sa,sl])
			s.append(es)
		return s

	def retrieveImages(self):
		i = []
		images=self.doc.getElementsByTagName('images')[0].getElementsByTagName('image')
		for image in images:
			ei = []
			title = image.getElementsByTagName('title')[0].childNodes[0].nodeValue.strip()
			description = image.getElementsByTagName('description')[0].childNodes[0].nodeValue.strip()
			path= image.getElementsByTagName('path')[0].childNodes[0].nodeValue.strip()
			ei.append([title,description,path])
			i.append(ei)
		return i

	def retrievePages(self):
		p = []
		pages=self.doc.getElementsByTagName('bookpages')[0].getElementsByTagName('bookpage')
		for page in pages:
			ep = []
			title = page.getElementsByTagName('title')[0].childNodes[0].nodeValue.strip()
			content = page.getElementsByTagName('content')[0].childNodes[0].nodeValue.strip()
			ep.append([title,content])
			p.append(ep)
		return p
