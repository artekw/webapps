#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sqlite3
import os
from bottle import route, debug, run, template, request, static_file

debug(True)

upload_dst='/home/artek/pyweb/upl'
root_app ='/home/artek/pyweb'

@route('/')
@route('/home')
def home():
	pages = ['home', 'upload', 'all']
	return template('home.tpl', pages=pages)

@route('/dobase')
def create_dbase():
	con = sqlite3.connect('imgbase.db')
	con.execute("CREATE TABLE img (id INTEGER PRIMARY KEY, filename char(100) NOT NULL)")
	return "Baza utworzona!"
	
@route('/upload', method='GET')
def do_upload():
    return template('upload_form.tpl')

@route('/upload', method='POST')
def get_upload():
    data = request.files.get('data')

    if data.file:
		raw = data.file.read()
		filename = data.filename
	  
		conn = sqlite3.connect('imgbase.db')
		c = conn.cursor()	  
		c.execute("INSERT INTO img (filename) VALUES (?)", [filename])
		new_id = c.lastrowid
		conn.commit()
		f=open(upload_dst + '/' + str(new_id) + '.' + filename.split('.')[1],'w')
		f.write(raw)
		f.close
		return "Wysłano plik %s o objętości (%d bajtów) na pozycję %d." % (filename, len(raw), new_id)
    return "Wypełnij formularz."

@route('/upl/:filename#.*#')
def static_image(filename):
	return static_file(filename, root='/home/artek/pyweb/upl')
	
@route('/style/:filename#.*#')
def static_style(filename):
	return static_file(filename, root='/home/artek/pyweb/style')
		
@route('/last')
def show_last():
	conn = sqlite3.connect('imgbase.db')
	c = conn.cursor()
	c.execute("SELECT id from img")
	result = c.fetchall()[-1][0]
	c.close()

	return static_image(str(result) + '.jpg')

@route('/all')
def show_all():
	conn = sqlite3.connect('imgbase.db')
	c = conn.cursor()
	c.execute("SELECT id from img")
	result = c.fetchall()
	c.close()

	return template('all.tpl', rows=result)

run(host='0.0.0.0', port=5000, reloader=True)
