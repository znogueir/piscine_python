from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False


NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

# added
print("#####################")
print(NULL_not_found(Nothing))
print(NULL_not_found(Garlic))
print(NULL_not_found(Zero))
print(NULL_not_found(Empty))
print(NULL_not_found(Fake))

print(NULL_not_found("agsa"))
print(NULL_not_found(112414))
print(NULL_not_found([1, 1]))
print(NULL_not_found(float("infinity")))
print(NULL_not_found(True))
