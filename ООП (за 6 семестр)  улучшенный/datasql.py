import os
import sqlite3 as db
from data import data

emptydb = """
PRAGMA foreign_keys = ON;

create table enterprise
(code integer primary key,
name text,
phone text,
contact text);

create table indexs
(code integer primary key,
name text,
importance text,
unit text);

create table dynamics
(code integer primary key,
date text,
sense integer,
indexs integer references indexs(code) on update cascade on delete set null,
enterprise integer references enterprise(code) on update cascade on delete set null);
"""

class datasql(data):
    def read(self):
        conn = db.connect(self.getInp())
        curs = conn.cursor()
        curs.execute("select code, name, phone, contact from enterprise")
        data=curs.fetchall()
        for r in data:self.getArch().createEnterprise(r[0], r[1], r[2], r[3])
        curs.execute("select code, name, importance, unit from indexs")
        data=curs.fetchall()
        for r in data:self.getArch().createIndex(r[0], r[1], r[2], r[3])
        curs.execute("select code, sense, indexs, enterprise from dynamics")
        data = curs.fetchall()
        for r in data: self.getArch().createDynamics(r[0], r[1], self.getArch().getIndex(int(r[2])), self.getArch().getEnterprise(int(r[3])))
        conn.close()
    def write(self):
        conn = db.connect(self.getOut())
        curs = conn.cursor()
        curs.executescript(emptydb)
        for a in self.getArch().getEnterpriseList():
            curs.execute("insert into enterprise(code, name, phone, contact) values('%s','%s','%s','%s')"%(
            str(a.getCode()),a.getName(), a.getPhone(), a.getContact()))
        for p in self.getArch().getIndexList():
            curs.execute("insert into indexs(code, name, importance, unit) values('%s','%s','%s','%s')"%(
            str(p.getCode()), p.getName(), str(p.getImportance()), p.getUnit()))
        for c in self.getArch().getDynamicsList():
            if c.getEnterprises(): ent = c.getEnterpriseCode()
            else: ent = "NULL"
            if c.getIndex(): inx = c.getIndexCode()
            else: inx = "NULL"
            curs.execute("insert into dynamics(code, sense, indexs, enterprise) values('%s','%s','%s','%s')" % (
                str(c.getCode()), str(c.getSense()), inx, ent))
        conn.commit()
        conn.close()