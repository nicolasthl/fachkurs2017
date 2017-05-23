from math import gcd
#from math import lcm


class Expression:
	def evaluate(self):
		pass

class Operation(Expression):
	def __init__(self, left_operand, right_operand):
		assert isinstance(left_operand, Expression) and \
		isinstance(right_operand, Expression)

		self.left_operand = left_operand
		self.right_operand = right_operand
	pass

class Sum(Operation):
	def evaluate(self):
		return self.left_operand.evaluate() + self.right_operand.evaluate()

class Diff(Operation):
	pass

class Multi(Operation):
	def evaluate(self):
		return self.left_operand.evaluate() * self.right_operand.evaluate()

class Div(Operation):
	pass

class Fraction(Expression):
	def __init__(self,num,denom):
		#what about "self"? => To adress the object itself.
		if denom == 0:
			raise ZeroDivisionError
		self.num = num
		self.denom = denom
		self.simplify()
	pass


	def __eq__(self, other):
		#underscore methods: pre-defined! also: 'magic' methods
		return self.num == other.num and \
		self.denom == other.denom 

	def __mul__(self, other):
		return self.product(other)
	
	def __add__(self,other):
		return self.add(other)

	def simplify(self):						#obsolete, as we perform already in constructor
		divisor = gcd(self.num, self.denom)
		self.num = self.num // divisor 		#souble slash for integer
		self.denom = self.denom // divisor

	def add(self, other):
		return Fraction(self.num * other.denom + self.denom * other.num, self.denom * other.denom)

	def product(self, other):
		return Fraction(self.num * other.num, 
						self.denom * other.denom) 

	def evaluate(self):
		return self