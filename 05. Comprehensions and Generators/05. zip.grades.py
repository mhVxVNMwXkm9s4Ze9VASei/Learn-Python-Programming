# zip.grades.py
grades = [18, 23, 30, 27]
avgs = [22, 21, 29, 24]
print(list(zip(avgs, grades)))
print(list(map(lambda *a: a, avgs, grades))) # equivalent to zip
