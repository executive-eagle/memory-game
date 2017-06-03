#!usr/bin/env python3

# This module will allow us to time the user
import time

'''
print('You have 5 seconds to guess correctly.')

mario = True
while mario:
	second = 1
	for second in range(1, 6, 1):
		time.sleep(1)
		#print(second)
		user_response = input('> Where is Mario?')
		second += 1

	mario = False
	
	
print('Mario is dead.')
'''

# The board
board = {'top-l': '', 'top-m': '', 'top-r': '',
		 'mid-l': '', 'mid-m': '', 'mid-r': '',
		 'low-l': '', 'low-m': '', 'low-r': ''}

symbol_list = [u'\u2660', u'\u2663', u'\u2666', u'\u2665', u'\u263b']

print(symbol_list)





