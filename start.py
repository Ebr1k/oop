import cherrypy
import sys
import os

sys.path.insert(0, "./archiveProject.py")
from archiveProject import archive
from dataxml import dataxml
from datasql import datasql
from dynamicspage5_2 import dynamicspage
from indexpagetest import indexpage
from enterprisepagetest import enterprisepage


class start:
    def __init__(self):
        self.__arch = archive()
        self.__load = False
        self.__fname = ''
        self.__dformat = ''
        self.__dataxml = dataxml(self.__arch)
        self.__datasql = datasql(self.__arch)
        self.dynamicspage = dynamicspage(self.__arch)
        self.indexpage = indexpage(self.__arch)
        self.enterprisepage = enterprisepage(self.__arch)

    def index(self):
        if not (self.__load):
            s = """<form action=openfile metod=post>
Открыть файл<br>
<input type=text name=fname value=''>
<select name=dformat>
<option value=XML>XML</option>
<option value=SQL>SQL</option>
</select><br>
<input type=submit>
</form>
"""
        else:
            sxml, sjson, ssql = '', '', ''
            if self.__dformat == 'XML':
                sxml = ' selected'
            elif self.__dformat == 'SQL':
                ssql = ' selected'

            s = """
<a href=dynamicspage\>динамики</a><br>
<a href=indexpage\>показатели</a><br>
<a href=enterprisepage\>компании</a><br>
<hr>
<form action=savefile metod=post>
Сохранить файл<br>
<input type=text name=fname value=%s>
<select name=dformat>
<option%s value=XML>XML</option>
<option%s value=SQL>SQL</option>
</select><br>
<input type=submit>
</form>
""" % (self.__fname, sxml, ssql)
        return s

    index.exposed = True

    def openfile(self, fname='', dformat=''):
        try:
            if dformat == 'XML':
                self.__dataxml.readFile(fname)
            elif dformat == 'SQL':
                self.__datasql.readFile(fname)
            self.__load = True
            self.__fname = fname
            self.__dformat = dformat
            return "Данные загружены<br><a href=./index>назад</a>"
        except:
            return "Файл %s не найден или выбран неправильный формат %s<br><a href=./index>назад</a>" % (fname, dformat)

    openfile.exposed = True

    def savefile(self, fname='', dformat=''):
        if dformat == 'XML':
            self.__dataxml.writeFile(fname)
        elif dformat == 'SQL':
            if os.path.isfile(fname): os.remove(fname)
            self.__datasql.writeFile(fname)
        return "Данные сохранены<br><a href=./index>назад</a>"

    savefile.exposed = True


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(start(), '/', conf)
