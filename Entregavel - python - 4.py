'''
4-
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

out = 0
for n in range(1000):
    out+= (int(n)**int(n))
print(str(out)[:10])