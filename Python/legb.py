"""
[LEGB]
Local       -   local scope
enclosing   -   scope between outer and inner function
global      -   global scope like x below
built-in    -   built-in functions like min, max, sum etc
                which can be referenced using import builtin.

dir - returns variables in current scope.
"""
import builtins


x = 'global x'

def test():
    y = 'local y'
    x = 'local x'
    # print(y)
    print(x)
    print(dir(builtins))
    print(dir())


test()
print(x)
