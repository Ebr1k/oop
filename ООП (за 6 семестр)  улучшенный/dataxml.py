#-*- coding:utf-8 -*-
import os,xml.dom.minidom
from data import data

class dataxml(data):
    def read(self):
        dom=xml.dom.minidom.parse(self.getInp())
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=="enterprise"):
                code,name,phone, contact=0,"","",""
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="phone":phone=t[1]
                    if t[0]=="contact":contact=t[1]
                self.getArch().createEnterprise(code,name,None,phone,contact)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=="index"):
                code,name,importance, unit=0,"","", ""
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="importance":importance=int(t[1])
                    if t[0] == "unit": unit = t[1]
                self.getArch().createIndex(code,name,importance, unit)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=="dynamics"):
                code,date,sense, index, enterprise=0,"","", None, None
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="date":date=t[1]
                    if t[0]=="sense":sense=int(t[1])
                    if t[0]=="enterprise":enterprise=self.getArch().getEnterprise(int(t[1]))
                    if t[0] == "index": index = self.getArch().getIndex(int(t[1]))
                self.getArch().createDynamics(code,date,sense, index, enterprise)
            #здесь был код
    def write(self):
        dom=xml.dom.minidom.Document()
        root=dom.createElement("archive")
        dom.appendChild(root)
        for a in self.getArch().getEnterpriseList():
            aut=dom.createElement("enterprise")
            aut.setAttribute("code",str(a.getCode()))
            aut.setAttribute("name",a.getName())
            aut.setAttribute("phone",a.getPhone())
            aut.setAttribute("contact",a.getContact())
            root.appendChild(aut)
        for p in self.getArch().getIndexList():
            pub=dom.createElement("index")
            pub.setAttribute("code",str(p.getCode()))
            pub.setAttribute("name",p.getName())
            pub.setAttribute("importance",str(p.getImportance()))
            root.appendChild(pub)
        for b in self.getArch().getDynamicsList():
            bk=dom.createElement("dynamics")
            bk.setAttribute("code",str(b.getCode()))
            bk.setAttribute("date",str(b.getDate()))
            bk.setAttribute("sense",str(b.getSense()))
            bk.setAttribute("index", str(b.getIndexCode()))
            bk.setAttribute("enterprise", str(b.getEnterpriseCode()))
            root.appendChild(bk)
        f = open(self.getOut(),"w")
        f.write(dom.toprettyxml())