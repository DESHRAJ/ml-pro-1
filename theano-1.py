import theano
a = theano.tensor.vector()
b = theano.tensor.vector()
out = a**2+b**2+2*a*b
f = theano.function([a,b],out)
print f([0,11,2],[0,1,2])