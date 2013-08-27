#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import os
import datetime
import sqlite3
import config

class ManifestProvider(object):

	def __init__(self):
		self.conn = None
		is_empty = not os.path.isfile(config.database)
		conn = sqlite3.connect(config.database)
		if is_empty:
			self._db_init(conn)
		self.conn = conn

	def _db_init(self,conn):
		c = conn.cursor()
		for sql in file(config.install_sql):
			sql_ = sql.strip()
			if len(sql_) > 0:
				c.execute(sql_)
		conn.commit()
	
	def _execute(self,sql,parameter=None):
		c = self.conn.cursor()
		if parameter == None:
			c.execute(sql)
		else:
			c.execute(sql,parameter)
		self.conn.commit()

	def _query(self,sql,parameter=None):
		c = self.conn.cursor()
		if parameter == None:
			c.execute(sql)
		else:
			c.execute(sql,paramter)
		rows = c.fetchall()
		return rows

	def get_sys_info(self):
		sql = 'select * from piclib'
		rows = self._query(sql)
		return rows[0]
	
	def set_sys_refresh_time(self,t):
		sql = 'update piclib set refresh_time=?'
		parameters = (t,)
		self._execute(sql,parameters)

	def set_sys_resource_time(self,t):
		sql = 'update piclib set resource_time=?'
		parameters = (t,)
		self._execute(sql,parameters)

	def add_project(self,project_id,project_name,resource_path,thumbnail_path):
		sql = 'insert into project(id,project_name,create_time,resource_path,thumbnail_path) values(?,?,?,?,?)'
		parameters = (project_id,project_name,datetime.datetime.now(),resource_path,thumbnail_path)
		self._execute(sql,parameters)
	
	def add_stuff(self,stuff_id,project_id,stuff_name,stuff_extname,stuff_path,thumbnail_path,width=0,height=0):
		sql = 'insert into stuff(id,project_id,stuff_name,ext_name,stuff_path,thumbnail_path,width,height) values(?,?,?,?,?,?,?,?)'
		parameters = (stuff_id,project_id,stuff_name,stuff_extname,stuff_path,thumbnail_path,width,height)
		self._execute(sql,parameters)
	
if __name__ == '__main__':
		mf = ManifestProvider()
		#mf.add_project('sssss','sssss','sssss')
		mf.set_sys_resource_time(datetime.datetime.now())

