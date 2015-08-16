from inspect import Signature, Parameter

# Make a signature for a func(x, y=42, *, z=None)
parms = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None) ]

sig = Signature(parms)
print('sig=',sig)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print('name=',name,'value=',value)

func(1,2,z=3)
func(1)
func(1,z=3)
func(y=2,x=1)
try:
    func(1,2,3,4)
except TypeError as e:
    print(e)
