#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import os
import uuid
from PIL import Image
import zipfile
import config

class StoreProvider(object):

	def __init__(self,mf):
		self.mf = mf
		if not os.path.isdir(config.input_path):
			os.mkdir(config.input_path)
		if not os.path.isdir(config.store_path):
			os.mkdir(config.store_path)
			
	def refresh(self):
		item_count = 0
		for item in os.listdir(config.input_path):
			if item.endswith(config.input_ext):
				sub_path = os.path.join(config.input_path, item)
				if os.path.isfile(sub_path):
					okfile = open(sub_path[:-4]+'.ok','w')
					okfile.write('store ok')
					okfile.close()

					store_path = os.path.join(config.store_path,item)
					os.rename(sub_path,store_path)
					self._submit(item,store_path)
					item_count = item_count + 1
		return item_count
	
	def _submit(self,project_name,store_path):
		project_id = uuid.uuid1().get_hex()
		distpath = os.path.join(config.store_path,project_id)
		with zipfile.ZipFile(store_path) as zf:
			zf.extractall(distpath)
		first_image_path = self._find_image(project_id,distpath)
		if first_image_path == None:
			first_image_path = 'default.jpg'
		self.mf.add_project(project_id,project_name,store_path,first_image_path)
	
	def _find_image(self, project_id, project_path):
		first_image_path = None
		for file_name in os.listdir(project_path):
			file_path = os.path.join(project_path,file_name)
			if os.path.isdir(file_path) :
				self._find_image(project_id, file_path)
			else:
				image_info = _get_image_info(file_path)
				if image_info != None :
					if first_image_path == None:
						first_image_path = image_info(3)
					image_id = uuid.uuid1().get_hex()
					self.mf.add_stuff(image_id,project_id,file_name,image_info(2),file_path,image_info(3),image_info(0),image_info(1))
		return first_image_path
	
	def _get_image_info(self,image_path):
		fn,en = os.path.splitext(image_path)
		if en in config.image_exts:
			im = Image.open(image_path)
			width,height = im.size
			if width > config.thumbnail[0] or height > config.thumbnail[1]:
				im.thumbnail(config.thumbnail)
				thumbnail_path = fn+'.thumbnail.jpg'
				im.save(thumbnail_path,'JPEG')
				return (width,height,en,thumbnail_path)
			else:
				return (width,height,en,image_path)
		else:
			return None
		
	
