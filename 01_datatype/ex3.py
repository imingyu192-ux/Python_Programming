# 불리언
#True or Fasle
a = True
print(a, type(a))

print(1 < 0)
print(1 > 0)
print(1 == 0)
print(1 != 0)

print("apple" > "apble")

# bool()
print(bool(3))
print(bool(0))
print(bool("hello"))
print(bool(""))
print(bool([10]))
print(bool([]))

# None 자료형
a = None
print(a, type(a))
print(a, bool(a))

if a is None:
    print("값이 없습니다")
