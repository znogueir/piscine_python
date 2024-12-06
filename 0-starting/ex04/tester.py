from whatis import whatis

whatis([])  # returns without doing anything
whatis(["whatis"])  # same

whatis(["whatis", 12])  # works
whatis(["whatis", 12352625])  # works

# whatis(["whatis", "aasga"])  # assertion err: not an int
whatis(["whatis", 12, 14])  # assertion err: more than one arg
# whatis(["whatis", "asdg", 232])  # assertion err: more than one arg
# whatis(["whatis", "asdga"])  # assertion err: not an int
