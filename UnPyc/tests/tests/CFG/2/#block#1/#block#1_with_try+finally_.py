try:
	with 1:
		print 2
		if True:
			isBlock=False
			print isBlock
		print 2
		if True:
			isBlock=False
			print isBlock
		print 1
finally:
	with 1:
		print 2
		if True:
			isBlock=False
			print isBlock
		print 2
		if True:
			isBlock=False
			print isBlock
		print 1
