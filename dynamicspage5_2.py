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

    def dynamicsform(self, code=0, add=True):
        date, sense, enterprise, index = '', 0, 0, 0
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code=%s' % code

        if code in self.__arch.getDynamicsCodes():
            enterprise = self.__arch.getDynamics(code).getEnterpriseCode()
            index = self.__arch.getDynamics(code).getIndexCode()
            date = self.__arch.getDynamics(code).getDate()
            sense = self.__arch.getDynamics(code).getSense()

        s = '''<form action=%s method=post>
        <table>
        <tr><td>дата</td><td><input type=text name=date value="%s"></td></tr>
        <tr><td>значение</td><td><input type=number name=sense value="%s"></td></tr>
        <tr><td>показатель</td><td>%s</td></tr>
        <tr><td>компания</td><td>%s</td></tr>
        <tr><td><input type=submit></td><td></td></tr>
        </table>
        </form>''' % (a, str(date), str(sense), self.indexCombo(code), self.enterpriseCombo(code))
        return s

    def addaction(self, enterprise, index, date, sense):
        # Исправлен вызов newDynamics
        self.__arch.newDynamics(
            date=date,
            sense=int(sense),
            index=self.__arch.getIndex(int(index)),
            enterprise=self.__arch.getEnterprise(int(enterprise))
        )
        return 'динамика показателей добавлена<br><a href=index>назад</a>'

    addaction.exposed = True

    def addform(self):
        s = 'Добавить новую динамику<br>'
        s += self.dynamicsform(0)
        return s

    addform.exposed = True

    def editform(self, code):
        s = 'Редактировать динамику<br>'
        s += self.dynamicsform(int(code), False)
        return s

    editform.exposed = True

    def editaction(self, code, enterprise, index, date, sense):
        # Исправлен вызов методов изменения
        dynamics = self.__arch.getDynamics(int(code))
        dynamics.setEnterprise(self.__arch.getEnterprise(int(enterprise)))
        dynamics.setIndex(self.__arch.getIndex(int(index)))
        dynamics.setDate(date)
        dynamics.setSense(int(sense))
        return 'динамика изменена<br><a href=index>назад</a>'

    editaction.exposed = True

    def delr(self, code):
        self.__arch.removeDynamics(int(code))
        return 'динамика удалена<br><a href=index>назад</a>'

    delr.exposed = True