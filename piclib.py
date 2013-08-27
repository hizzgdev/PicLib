#! /usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
from piclibmf import ManifestProvider
from piclibstore import StoreProvider

class PicLib(object):

	def __init__(self):
		self.mf = ManifestProvider()
		self.store = StoreProvider(self.mf)

		sysinfo = self.mf.get_sys_info()
		self.sys_name = sysinfo[0]
		self.sys_create_time = sysinfo[1]
		self.sys_resource_time = sysinfo[2]
		self.sys_refresh_time = sysinfo[3]

	def refresh(self):
		item_count = self.store.refresh()
		now_time = datetime.datetime.now()
		self.mf.set_sys_refresh_time(now_time)
		if item_count > 0:
			self.mf.set_sys_resource_time(now_time)
		return item_count
	
