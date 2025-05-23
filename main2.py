from arсhive import archive
from dataxml import dataxml

arch1=archive()
dat1=dataxml(arch1,"old.xml","new.xml")
dat1.read()
dat1.write()

