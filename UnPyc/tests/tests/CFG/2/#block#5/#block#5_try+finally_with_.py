with 1:
	try:
		raise NameError('YourNameIncorrect')
	finally:
		raise NameError('YourNameIncorrect')
	try:
		raise NameError('YourNameIncorrect')
	finally:
		raise NameError('YourNameIncorrect')
	print 1
