# generator.expressions.py
cubes = [k ** 3 for k in range(10)] # regular list
print(cubes)
type(cubes)

cubes_gen = (k ** 3 for k in range(10)) # create as generator
print(cubes_gen)
type(cubes_gen)
print(list(cubes_gen))
print(list(cubes_gen))
