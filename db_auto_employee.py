#!/usr/bin/python3

import MySQLdb
import pandas as pd
import numpy as np
from IPython.display import display
from tabulate import tabulate
import getpass
import sys

host = input("Enter host name: ")
usr = input("Enter username: ")
password = getpass.getpass(prompt = "Enter password: ")
database = input("Enter Database name: ")

db = MySQLdb.connect(host, usr, password, database)
cursor = db.cursor()

print("\nCONNECTED TO DATABASE: " + database + " ..................................................................\n")

emp = {'ID':[' '], 'First_Name':[' '], 'First_Name':[' '], 'Last_Name':[' '], 'EMP_Title':[' '], 'EMP_StartDate':[' '], 'EMP_Branch':[' '], 'EMP_Salary':[' ']} 

def pd_centered(df):
    return df.style.set_table_styles([
        {"selector": "th", "props": [("text-align", "center")]},
        {"selector": "td", "props": [("text-align", "center")]}])
def sql_insert():
	lol = []
	lov = []
	c = 0
	global table
	table = input("\nEnter Table name: ")
	print()
	for i in range(len(emp['ID'])):
		lol.append([])
		lov.append("f"+str(i))

	while c < len(emp['ID']):
		for lov in emp.values():
			lol[c].append(lov[c])
		c += 1

	del lol[0]
	#print(lol)
	for record in lol:

		sql = "INSERT INTO " + table + "(ID, First_Name, Last_Name, EMP_Title, EMP_StartDate, EMP_Branch, EMP_Salary) " + "VALUES" + str(tuple(record))
		try:
			#execute the sql command
			cursor.execute(sql)
			#commit your changes in database
			db.commit()
			print("Employee successfully entered to the Database.")
			print("\nWould you like to view the updated database?")
			prompt = input("Press Y|y for Yes, any other key for No: ")
			if prompt == 'Y' or prompt == 'y':
				sql_select()
			else:
				print('\nOK\nBye!')
		except:
			#rollback in case there is any error
			db.rollback()


def get_data():
	for field in emp.keys():
		data = input("Enter Employee " + field + ": ")
		emp[field].append(data)
	print("\nAdd another Employee?")
	prompt = input("Press Y|y for Yes, any other key for No: ")
	print()
	if prompt == 'Y' or prompt == 'y':
		get_data()
	else:
		#print(emp)
		index  = [' ']
		index.extend(["*" for i in range(1, len(emp['ID']))])
		df = pd.DataFrame(emp, index = index)
		#st_df = pd_centered(df)
		#display(st_df)
		print("\nCheck Employee data to be entered on the Database.................................................\n")
		print(tabulate(df, headers = 'keys', tablefmt = 'fancy_grid'))
		print("\nWould you like to continue?")
		prompt = input("Press Y|y for Yes, any other key for No: ")
		if prompt == 'Y' or prompt == 'y':
			sql_insert()
	return emp

def sql_select():
	table = input("\nEnter Table name: ")
	print("\nView all records?")
	prompt = input("Press Y|y for Yes, any other key for No: ")
	if prompt == 'Y' or prompt == 'y':
		sql = "SELECT * FROM " + table 
		try:
			cursor.execute(sql)	
			data = cursor.fetchall()
			index = ['*' for i in range(len(data))]
			df = pd.DataFrame(data, index = index)
			print(tabulate(df, headers = emp.keys(), tablefmt = 'fancy_grid'))
		except:
			print("ERROR: unable to fecth data")
	else:
		prompt = input("\nPress -\n# 1 to view specific fields & all records\n# 2 to to view specific fields & records\n# 3 to view limited number of records\n# ")
		if prompt == '1':
			print("\nFields: ", end = "")
			for k in emp.keys():
				print(k, end = "  ")
			print("\n")
			view = input("Enter Field name(s) to view (separated by comma(s) without spaces): ")
			print()
			sql1 = "SELECT " + view + " FROM " + table
			head = view.split(',')
			try:
				cursor.execute(sql1)	
				data = cursor.fetchall()
				index = ['*' for i in range(len(data))]
				df = pd.DataFrame(data, index = index)
				print(tabulate(df, headers = head, tablefmt = 'fancy_grid'))
			except:
				print("ERROR: unable to fecth data")
		elif prompt == '2':
			print("\nFields: ", end = "")
			for k in emp.keys():
				print(k, end = "  ")
			print("\n")
			view = input("Enter Field name(s) to view (separated by comma(s) without spaces): ")
			cond = input("Enter condition(s) to access specific record(s) (field operator Value): ")
			print()
			sql2 = "SELECT " + view + " FROM " + table + " WHERE " + cond
			head = view.split(',')
			try:
				cursor.execute(sql2)	
				data = cursor.fetchall()
				index = ['*' for i in range(len(data))]
				df = pd.DataFrame(data, index = index)
				print(tabulate(df, headers = head, tablefmt = 'fancy_grid'))
			except:
				print("ERROR: unable to fecth data")	
		elif prompt == '3':
			print("\nFields: ", end = "")
			for k in emp.keys():
				print(k, end = "  ")
			print("\n")
			view = input("Enter Field name(s) to view (separated by comma(s) without spaces): ")
			lt = input("Enter Offset value ('0' for first row): ")
			ct = input("Enter Number of Rows to view: ")
			print()
			sql3 = "SELECT " + view + " FROM " + table + " LIMIT " + lt + ", " + ct
			head = view.split(',')
			try:
				cursor.execute(sql3)	
				data = cursor.fetchall()
				index = ['*' for i in range(len(data))]
				df = pd.DataFrame(data, index = index)
				print(tabulate(df, headers = head, tablefmt = 'fancy_grid'))
			except:
				print("ERROR: unable to fecth data")	

print("Would you like to enter a new Employee to the database?")
prompt = input("Press Y|y for Yes, any other key for No: ")
print()
if prompt == 'Y' or prompt == 'y':
	print("NOTE: Enter Date in format: YYYY-MM-DD\n")
	get_data()
else:
	print("\nWould you like to view the selected Database?")
	prompt = input("Press Y|y for Yes, any other key for No: ")
	if prompt == 'Y' or prompt == 'y':
		sql_select()
	else:
		print("\nOK\nBye!")



#disconnect from server
db.close()
print("\nDATABASE CONNECTION CLOSED.")