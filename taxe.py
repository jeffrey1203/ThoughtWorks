#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import re,os,sys
from item import *

class Item(object):
	"""商品"""
	def __init__(self,name,price):
		self.name = name
		self.price = price
		self.rate = 1.1
		self.oriPrice = self.price
		self.taxe = 0
	def calculation(self,price):
		if self.isimported:
			self.rate = self.rate + 0.05
		else:
			pass
		self.price = round(self.price * self.rate,2)
		if 0<((self.price * 100)%10)<5:
			self.price = round(self.price,1)+0.05
		else:
			pass
		self.taxe = self.price - self.oriPrice
	def isImported(self):
		if 'imported' in self.name:
			self.isimported = True
		else:
			self.isimported = False
	def judgeClass(self):
		for word in FOOD+BOOK+MEDICAL:
			if word in self.name:
				self.rate = self.rate - 0.1
			else:
				pass
class Cuaculate_Taxe(object):
	"""计算税并且打印结果"""
	def __init__(self):
		'''定义变量'''
		super(Cuaculate_Taxe, self).__init__()
		#self.arg = arg
		self.itemname = []
		self.itemprice = []
		self.itempriceFinal = []
		self.totalprice = 0
		self.taxe = 0
		self.thePrint = []
	def getItems(self):
		'''获取输入的数据'''
		receipt = re.compile(r"^(\d+) (.*) at (\d+).(\d+)$")
		path = sys.path[0]
		print path
		files = open(path+'\\test2.txt','r')    
		alllines_of_text = files.readlines()
		files.close()
		self.items_name_list = []
		for line in alllines_of_text:
			result = receipt.finditer(line)
			for i in result:
				words=i.group(2).replace(' ','')
				self.thePrint.append(i.group(1)+' '+i.group(2))
				self.items_name_list.append(words)
				self.itemname.append(i.group(2))
				self.itemprice.append(float(i.group(3))+0.01*float(i.group(4)))		
	def buildItem(self,name,price):
		'''计算过程'''
		tempItem = Item(name,price)
		tempItem.isImported()
		tempItem.judgeClass()
		tempItem.calculation(tempItem.price)
		self.itempriceFinal.append(round(tempItem.price,2))
		self.totalprice = self.totalprice + tempItem.price
	def printAll(self):
		'''打印计算结果'''
		for i in range(len(self.thePrint)):
			print self.thePrint[i]+':'+str(self.itempriceFinal[i])
		print 'Sales Taxes:'+str('%.2f') %(self.totalprice-sum(self.itemprice))
		print 'Total:'+str('%.2f') %self.totalprice

if __name__ == '__main__':
	new = Cuaculate_Taxe()
	new.getItems()
	for eachItem in range(len(new.items_name_list)):
		new.buildItem(new.itemname[eachItem],new.itemprice[eachItem])
	new.printAll()
				
		
