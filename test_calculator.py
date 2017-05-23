#import calculator as calc
from calculator import *


#we will code a test calculator here
def test_trivial_example():
	assert 1 == 1
	#assert means: test on a boolean condition, assign it's result.

def test_fraction_init():
	frac = Fraction(3,4)
	assert frac.num == 3
	assert frac.denom == 4
	pass

#frac = calc.Fraction (3, 0)
#this actually is a test funcition, declared by 'test_...' prefix
#if we call "python3 -m 'pytest'" in a given directory, it will check for every python test funcitons.

def test_fraction_multiply():
	assert Fraction(1,2) * Fraction(2,4) == Fraction(1,4)

def test_fraction_addition():
	assert Fraction(1,2) + Fraction (1,4) == Fraction(3,4)

def test_fraction_simplify():
	assert Fraction(1,2) == Fraction(2,4)

def test_fraction_equate():
	pass

def test_sum():
	assert Sum(Fraction(1,2), Fraction(1, 4)).evaluate() == Fraction(3,4)