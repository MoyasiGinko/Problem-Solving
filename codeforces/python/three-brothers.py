def who_missing(a, b):
  all_brothers = [1, 2, 3]

  for i in all_brothers:
    if i != a and i != b:
      return i

a, b = map(int, input().split())

print(who_missing(a, b))
