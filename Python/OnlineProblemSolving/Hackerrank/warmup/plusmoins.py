N = float(input())
numbers = list(map(float, input().split()))
a = len(list(filter(lambda x: x > 0, numbers)))
b = len(list(filter(lambda x: x == 0, numbers)))
c = len(list(filter(lambda x: x < 0, numbers)))
print("{:.3f}\n{:.3f}\n{:.3f}".format(a/N,c/N,b/N))