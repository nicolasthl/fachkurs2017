class Expression:
	pass

class Operation(Expression)
	pass
class Sum(Operation)
	pass
class Diff(Operation)
	pass
class Multi(Operation)
	pass
class Div(Operation)
	pass

class Fraction(Expression)
	def __init__(self,num,denom):
		#what about "self"? => To adress the object itself.
		self.num = num
		self.denom = denom
	pass
