from db import *
import os
import sys
from filter_ip import get_ip

_func_list = list((
		"query  status",
		"update status",
		"man show help",
		"exit"
	))

def init():
	_ip_list = get_ip()
	for x in _ip_list:
		insert_data(x)

def show_interface(inner_list):
	clear()
	print("===============White List CLI===============")
	for x in range(len(inner_list)):
		print(inner_list[x])
	print("============================================")

def normal_exit():
		sys.exit(0)

def man():
	clear()
	show_interface(_func_list)

def clear():
	os.system('cls')

def main():
	while 1==1:
		show_interface(_func_list)
		print("Enter you order:")
		order = input()
		order_to_func(order)()

def order_to_func(order):
	orders = {
		"query" : query_status,
		"update" : update_count,
		"exit" : normal_exit,
		"man" :  man
	}

	return orders.get(order, man)

if __name__ == '__main__':
	main()