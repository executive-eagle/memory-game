#!usr/bin/env python3

# This module will allow us to time the user
import time
import random

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
def printBoard(board):
	print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
	print('-+-+-')
	print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
	print('-+-+-')
	print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
	

symbol_list = [u'\u2660', u'\u2663', u'\u2666', u'\u2665', u'\u263b']

print(symbol_list)
printBoard(board)

def placer(board):
	s = list(range(9))
	print(s)
	#Shuffles the list
	q = s.copy()
	random.shuffle(q)
	
	for k, v in board.items():
		for num in q:
			if num in [0, 1]:
				board[k] = symbol_list[0]
				print(board[k])
			elif num in [2, 3]:
				board[k] = symbol_list[1]
				print(board[k])
			elif num in [4, 5]:
				board[k] = symbol_list[2]
				print(board[k])
			elif num in [6, 7]:
				board[k] = symbol_list[3]
				print(board[k])
			else:
				board[k] = symbol_list[4]
				
	print(board)
placer(board)
		
		
		



