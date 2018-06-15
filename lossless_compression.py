#!/usr/bin/env python3

from time import time
def compress(stream): #lossless data compression
	# ####################################################
	# G O S  version of lossless data compression
	# written by: Bryan Angelo
	# Christmas eve.. hooray! (2017)
	# it works perfectly! but I don't understand why!!!
	# ####################################################
	
	len_stream = len(stream) - 1
	stream_compressed = ""
	current_char = ""
	i = 0
	while i <= len_stream:
		if not i == len_stream:
			i_add = 1
		else:
			i_add = 0
		
		if stream[i+i_add] == stream[i]:
			current_char += stream[i]
		else:
			if not current_char == "":
				current_char += stream[i]
				stream_compressed += str(len(current_char)) + current_char[0]
				current_char = ""
			else:
				stream_compressed += stream[i]
		if i_add == 0:
			if len(current_char) > 1:
				stream_compressed += str(len(current_char)) + current_char[0]
			else:
				stream_compressed += current_char[0]
		i += 1
	return stream_compressed
	
word = input("Enter something: ")
start = time()
compressed = compress(word)
print("Fast enough: {0}".format(time() - start))
print(compressed)