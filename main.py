'''from package.mod1 import func1, func2
from package.mod2 import func3, func4


print(func1())
print(func2())
print(func3())
print(func4())'''

'''from package import mod1, mod2

print(mod1.func1())
print(mod1.func2())
print(mod2.func3())
print(mod2.func4())'''

#Required to import the package
import package as pkg

print(pkg.mod1.func1())
print(pkg.mod1.func2())
print(pkg.mod2.func3())
print(pkg.mod2.func4())

