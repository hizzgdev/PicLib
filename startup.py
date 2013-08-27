#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

from bottle import Bottle,debug,run,static_file,view
from piclib import PicLib

app = Bottle()
debug(True)
plib = PicLib()


@app.get('/')
@app.get('/projects')
@app.get('/projects/:page')
@app.get('/projects/:page/')
@view('projects')
def project_list(page='1'):
	return dict(sys_name='sysname',page=page)

@app.get('/html/:filename')
def static_file_route(filename='index.html'):
	return static_file(filename,root='./html')

@app.get('/refresh')
@app.get('/refresh/')
def resource_refresh():
	item_count = plib.refresh()
	return dict(item_count=item_count)

if __name__ == '__main__':
	run(app=app,host='0.0.0.0',port=8080)
