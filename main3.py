from arсhive import archive
from datasql import datasql
from dataxml import dataxml
import os

arch1=archive()
arch2=archive()
dxml1 = dataxml(arch1, "old.xml", "new.xml")
dxml2 = dataxml(arch1, "old.xml", "new.xml")

dsql1=datasql(arch1, 'new.sqlite', 'new.sqlite')
dxml1.read()
if os.path.isfile(dsql1.getOut()):os.remove(dsql1.getOut())
dsql1.write()
dsql1.read()
dxml2.write()


