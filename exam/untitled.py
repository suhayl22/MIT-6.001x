def insert(atMe, newFrob):
	last = None
	if newFrob.myName() < atMe.myName():
		while newFrob.myName() < atMe.myName():
			last = atMe
			atMe = atMe.getBefore()
		if atMe == None:
			last.setBefore(newFrob)
			newFrob.setAfter(atMe)
		else:
			atMe.setAfter(newFrob)
			newFrob.setBefore(atMe)
			last.setBefore(newFrob)
			newFrob.setAfter(last)
	else:
		while newFrob.myName() > atMe.myName():
			last = atMe
			atMe = atMe.getAfter()
		if atMe == None:
			last.setAfter(newFrob)
			newFrob.setBefore(atMe)
		else:
			atMe.setBefore(newFrob)
			newFrob.setAfter(atMe)
			last.setAfter(newFrob)
			newFrob.setBefore(last)