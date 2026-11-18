def sumi(n):
    if n<10:
        return n
    return n%10 + sumi(n//10)

print(sumi(1234))