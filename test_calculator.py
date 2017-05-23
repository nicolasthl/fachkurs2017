import calculator.py as calc

#we will code a test calculator here
def test_trivial_example():
	assert 1 == 1
	#assert means: test on a boolean condition, assign it's result.

def test_fraction():
	pass



#this actually is a test funcition, declared by 'test_...' prefix
#if we call "python3 -m 'pytest'" in a given directory, it will check for every python test funcitons.