#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

#c.execute("CREATE TABLE foo (date TEXT, trans TEXT)")
#c.execute("INSERT INTO foo VALUES ('2011-01-29', 'foobar')")
#conn.commit()
print 'Odczyt...'

c.execute('SELECT * from foo')
result = c.fetchall()
newid = c.lastrowid
print result
print newid