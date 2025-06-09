class dynamicspage:
    def __init__(self, archive):
        self.__arch = archive

    def index(self):
        s = '''<a href=..>назад</a>/<a href=addform>добавить</a>
<table><th bgcolor=gray></th>


<th bgcolor=gray>показатель</th>
<th bgcolor=gray>компания</th>
<th bgcolor=gray>дата</th>
<th bgcolor=gray>значение</th>'''
        r = 1
        bg = ''
        for c in self.__arch.getDynamicsCodes():
            s += '<tr%s><td>%d</td>' % (bg, r)
            s += '<td>%s</td>' % self.__arch.getDynamics(c).getIndex().getName()
            #s += '<td>%s</td>' % "<a href=imgview?img=%s>%s</a>" % (self.__arch.getDynamics(c).getImg(), self.__arch.getDynamics(c).getImg())
            #s += '<td>%s</td>' % self.__arch.getDynamics(c).getAuthorBiblioStr()
            s += '<td>%s</td>' % self.__arch.getDynamics(c).getEnterprises().getName()
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

    '''def enterpriseCombo(self, code=0):
        s = '<select name=enterprise>'
        for c in self.__arch.getEnterpriseCodes():
            if (code in self.__arch.getDynamicsCodes()) and (c == self.__arch.getDynamics(code).getEnterpriseCodes()):
                v = ' selected'
            else:
                v = ''
            s += '<option%s value=%s>%s</option>' % (v, str(c), self.__arch.getEnterprise(c).getName())
        s += '</select>'
        return s

    def indexCombo(self, code=0):
        s = '<select name=index>'
        for c in self.__arch.getIndexCodes():
            if not(c in self.__arch.getDynamics(code).getIndexCodes()):
                s += '<option value=%s>%s</option>' % (str(c), self.__arch.getIndex(c).getName())
        s += '</select>'
        return s'''

    def enterpriseCombo(self, code=0):
        s = '<select name=enterprise>'
        selected_enterprise = 0
        if code in self.__arch.getDynamicsCodes():
            selected_enterprise = self.__arch.getDynamics(code).getEnterpriseCode()

        for c in self.__arch.getEnterpriseCodes():
            if c == selected_enterprise:
                v = ' selected'
            else:
                v = ''
            s += '<option%s value=%s>%s</option>' % (v, str(c), self.__arch.getEnterprise(c).getName())
        s += '</select>'
        return s

    def indexCombo(self, code=0):
        s = '<select name=index>'
        selected_index = 0
        if code in self.__arch.getDynamicsCodes():
            selected_index = self.__arch.getDynamics(code).getIndexCode()

        for c in self.__arch.getIndexCodes():
            if c == selected_index:
                v = ' selected'
            else:
                v = ''
            s += '<option%s value=%s>%s</option>' % (v, str(c), self.__arch.getIndex(c).getName())
        s += '</select>'
        return s
    #def authorList(self, code=0):
    #    s = '<table>'
    #    for c in self.__arch.getDynamics(code).getAuthorCodes():
    #        s += '''<tr><td>%s</td><td><a href=delauthor?code=%s&acode=%s>удалить</td></tr>''' % (self.__arch.getAuthor(c).getBiblioStr(), str(code), str(c))
    #    s += '</table>'
    #    return s

    def dynamicsform(self, code=0, add=True):
        date, sense, enterprise, index  =  '', 0, 0, 0
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code=%s' % code
        if code in self.__arch.getDynamicsCodes():
        #    name = self.__arch.getDynamics(code).getName()
        #    img = self.__arch.getDynamics(code).getImg()
            enterprise = self.__arch.getDynamics(code).getEnterpriseCode()
            index = self.__arch.getDynamics(code).getIndexCode()
            date = self.__arch.getDynamics(code).getDate()
            sense = self.__arch.getDynamics(code).getSense()
        s = '''<form action=%s method=post>
        <table>
        <tr><td>дата</td><td><input type=text name=date value=%s></td></tr>
        <tr><td>значение</td><td><input type=number name=sense value=%s></td></tr>
        <tr><td>показатель</td><td>%s</td></tr>
        <tr><td>компания</td><td>%s</td></tr>
        <tr><td><input type=submit></td><td></td></tr>
        </table>
        </form>''' % (a, str(date), int(sense), self.indexCombo(index), self.enterpriseCombo(enterprise))
        return s

        def addaction(self, enterprise, index, date, sense):
            self.__arch.newDynamics(self, date=str(date), sense=int(sense), index=self.__arch.getIndex(int(index)), enterprise=self.__arch.getEnterprise(int(enterprise)))
            return 'динамика показателей добавлена<br><a href=index>назад</a>'

        addaction.exposed = True

        def addform(self):
            s = u'Добавить новую динамику<br>'
            s += self.dynamicsform(0)
            return s

        addform.exposed = True

        def editform(self, code):
            s = u'Редактировать динамику<br>'
            s += self.dynamicsform(int(code), False)
            s += '''показатели
            <form action=addindex?code=%s method=post>
            <table>
            <tr><td>%s</td><td><input type=submit value=добавить></td>
            </table>
            ''' % (str(code), self.indexCombo(int(code)))
            s += self.indexList(int(code))
            '''if self.__lib.getDynamics(int(code)).getImg():
                s = """<table>
                <tr valign=top><td><img src=../static/img/%s></td>
                <td>%s</td></tr>
                </table>
                """ % (self.__lib.getBook(int(code)).getImg(), s)'''
            return s

        editform.exposed = True

        def editaction(self, enterprise, index, date, sense):
            self.__arch.getDynamics(int(code)).setEnterprise(self.__arch.getEnterprise(int(enterprise)))
            self.__arch.getDynamics(int(code)).setIndex(self.__arch.getIndex(int(index)))
            self.__arch.getDynamics(int(code)).setDate(int(date))
            self.__arch.getDynamics(int(code)).setSense(int(sense))
            return 'динамика изменена<br><a href=index>назад</a>'

        editaction.exposed = True

        #def addauthor(self, code, author):
        #    self.__lib.getBook(int(code)).appendAuthor(self.__lib.getAuthor(int(author)))
        #    return 'автор добавлен<br><a href=editform?code=%s>назад</a>' % str(code)

        #addauthor.exposed = True

        #def delauthor(self, code, acode):
        #    self.__lib.getBook(int(code)).removeAuthor(int(acode))
        #    return 'автор удален<br><a href=editform?code=%s>назад</a>' % str(code)

        #delauthor.exposed = True

        def delr(self, code):
            self.__arch.removeDynamics(int(code))
            return 'динамика удалена<br><a href=index>назад</a>'

        delr.exposed = True