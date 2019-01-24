def approx_derivative(f,x, delta = 1e-6):
	return (f(x+delta)-f(x-delta))/(2*delta)

def approx_derivative_2(f,delta=1e-6):
	def f_prime(x):
		return (f(x+delta)-f(x-delta))/(2*delta)
	return f_prime