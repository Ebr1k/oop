class bookpage:
    def __init__(self, archive):
        self.__arch = archive

    def index(self):
        s = '''<a href=..>назад</a>/<a href=addform>добавить</a>
<table><th bgcolor=gray></th>
<th bgcolor=gray>название</th>

<th bgcolor=gray>показатель</th>
<th bgcolor=gray>компания</th>
<th bgcolor=gray>дата</th>
<th bgcolor=gray>значение</th>'''
        r = 1
        bg = ''
        for c in self.__arch.getDynamicsCodes():
            s += '<tr%s><td>%d</td>' % (bg, r)
            s += '<td>%s</td>' % self.__arch.getDynamics(c).getName()
            #s += '<td>%s</td>' % "<a href=imgview?img=%s>%s</a>" % (self.__arch.getDynamics(c).getImg(), self.__arch.getDynamics(c).getImg())
            #s += '<td>%s</td>' % self.__arch.getDynamics(c).getAuthorBiblioStr()
            #s += '<td>%s</td>' % self.__arch.getDynamics(c).getPublName()
            s += '<td>%s</td>' % self.__arch.getDynamics(c).getDate()
            s += '<td>%s</td>' % self.__arch.getDynamics(c).getSense()
            s += '<td><a href=editform?code=%s>редактировать</a></td>' % c
            s += '<td><a href=delr?code=%s>удалить</a></td></tr>' % c
            r += 1
            if bg:
                bg = ''
            else:
                bg = ' bgcolor=silver'
        s += '</table>'
        return s
    index.exposed = True

   # def imgview(self, img):
   #     return '<img src=../static/img/%s><br><a href=.>назад</a>' % img
   # imgview.exposed = True

    def enterpriseCombo(self, code=0):
        s = '<select name=enterprise>'
        for c in self.__arch.getEnterpriseCodes():
            if (code in self.__arch.getDynamicsCodes()) and (c == self.__arch.getDynamics(code).getEnterpriseCodes()):
                v = ' selected'
            else:
                v = ''
            s += '<option%s value=%s>%s</option>' % (v, str(c), self.__arch.getEnterprise(c).getName())
        s += '</select>'
        return s

    #def indexCombo(self, code=0):
    #    s = '<select name=index>'
    #    for c in self.__arch.getIndexCodes():
    #        if not(c in self.__arch.getDynamics(code).getIndexCodes()):
    #            s += '<option value=%s>%s</option>' % (str(c), self.__arch.getIndex(c).getBiblioStr())
    #    s += '</select>'
    #    return s

    #def authorList(self, code=0):
    #    s = '<table>'
    #    for c in self.__arch.getDynamics(code).getAuthorCodes():
    #        s += '''<tr><td>%s</td><td><a href=delauthor?code=%s&acode=%s>удалить</td></tr>''' % (self.__arch.getAuthor(c).getBiblioStr(), str(code), str(c))
    #    s += '</table>'
    #    return s

    def bookform(self, code=0, add=True):
        name, enterprise, date, sense = '', 0, 0, 0
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code=%s' % code
        if code in self.__arch.getDynamicsCodes():
            name = self.__arch.getDynamics(code).getName()
        #    img = self.__arch.getDynamics(code).getImg()
            enterprise = self.__arch.getDynamics(code).getPublCode()
            date = self.__arch.getDynamics(code).getYear()
            sense = self.__arch.getDynamics(code).getSense()
        s = '''<form action=%s method=post>
        <table>
        <tr><td>название</td><td><input type=text name=name value='%s'></td></tr>
        
        <tr><td>компания</td><td>%s</td></tr>
        <tr><td>дата</td><td><input type=number name=year value=%s></td></tr>
        <tr><td>значение</td><td><input type=number name=pages value=%s></td></tr>
        <tr><td><input type=submit></td><td></td></tr>
        </table>
        </form>''' % (a, name, self.publCombo(publ), str(year), str(pages))
        return s

        def addaction(self, name, img, publ, year, pages):
            self.__lib.newBook(name, img, publ=self.__lib.getPubl(int(publ)), year=int(year), pages=int(pages))
            return 'книга добавлена<br><a href=index>назад</a>'

        addaction.exposed = True

        def addform(self):
            s = u'Добавить новую книгу<br>'
            s += self.bookform(0)
            return s

        addform.exposed = True

        def editform(self, code):
            s = u'Редактировать книгу<br>'
            s += self.bookform(int(code), False)
            s += '''авторы
            <form action=addauthor?code=%s method=post>
            <table>
            <tr><td>%s</td><td><input type=submit value=добавить></td>
            </table>
            ''' % (str(code), self.authorCombo(int(code)))
            s += self.authorList(int(code))
            if self.__lib.getBook(int(code)).getImg():
                s = """<table>
                <tr valign=top><td><img src=../static/img/%s></td>
                <td>%s</td></tr>
                </table>
                """ % (self.__lib.getBook(int(code)).getImg(), s)
            return s

        editform.exposed = True

        def editaction(self, code, name, img, publ, year, pages):
            self.__lib.getBook(int(code)).setName(name)
            self.__lib.getBook(int(code)).setImg(img)
            self.__lib.getBook(int(code)).setPubl(self.__lib.getPubl(int(publ)))
            self.__lib.getBook(int(code)).setYear(int(year))
            self.__lib.getBook(int(code)).setPages(int(pages))
            return 'книга изменена<br><a href=index>назад</a>'

        editaction.exposed = True

        def addauthor(self, code, author):
            self.__lib.getBook(int(code)).appendAuthor(self.__lib.getAuthor(int(author)))
            return 'автор добавлен<br><a href=editform?code=%s>назад</a>' % str(code)

        addauthor.exposed = True

        def delauthor(self, code, acode):
            self.__lib.getBook(int(code)).removeAuthor(int(acode))
            return 'автор удален<br><a href=editform?code=%s>назад</a>' % str(code)

        delauthor.exposed = True

        def delr(self, code):
            self.__lib.removeBook(int(code))
            return 'книга удалена<br><a href=index>назад</a>'

        delr.exposed = True