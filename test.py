#!/usr/bin/python
# -*- coding: utf-8 -*-

from graphite_escaping import metrics_name_to_graphite, metrics_name_from_graphite
from simple_color_print import bcolors


def test_consistency(name):

	# if metrics_name_from_graphite(metrics_name_to_graphite(name)) == name.replace(".", "_"):
	assert type(metrics_name_from_graphite(metrics_name_to_graphite(name))) == type(name), 'inconsistent object type'
	if metrics_name_from_graphite(metrics_name_to_graphite(name)) == name:
		return True
	else:
		return False

def colored_print(status):
	if status:
		# print "Test Consistency: ", bcolors.OKGREEN + "PASS" + bcolors.ENDC
		print "Test Consistency: ", bcolors.green_print("PASS")
	else:
		# print "Test Consistency: ", bcolors.WARNING + "FAIL" + bcolors.ENDC
		print "Test Consistency: ", bcolors.red_print("FAIL")


def test_unit(test):
	print '==== Test for =====', test , '======'
	to_graphite = metrics_name_to_graphite(test)
	print test, ' ==> ', to_graphite
	from_graphite = metrics_name_from_graphite(to_graphite)
	print to_graphite, ' ==> ', from_graphite
	colored_print(test_consistency(test))

def tests():
	# test_1: abc_edf
	test_unit('abc_edf')

	# test_2: abc @edf#
	test_unit('abc @edf#')

	# test_3: abc.@edf#
	test_unit('abc.@edf#')

	# test_3: abc.@edf#
	test_unit('abc_ @ e_df#')

	# test_4: a.b.c_ @ e_df#
	test_unit('a.b.c_ @ e_df#')

	# test_5: a.b._c d  ._feg
	test_unit('a.b.___c d _feg')

	# test_6: '_ . .fda'
	test_unit('_ . .fda')

	# test_7: '_.'
	test_unit('_.')
	
	# test for international characters
	# test_8: '汉 字.汉*字' (Chinese)
	test_unit('汉 字.汉*字')

def main():
	tests()

if __name__ == '__main__':
	main()

