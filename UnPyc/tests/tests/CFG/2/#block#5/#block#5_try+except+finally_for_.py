for i in range(3):
	try:
		raise NameError('YourNameIncorrect')
	except:
		raise NameError('YourNameIncorrect')
	finally:
		raise NameError('YourNameIncorrect')
