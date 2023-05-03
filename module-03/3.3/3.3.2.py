# 3.3.2 Logical expressions

var = 1
# Example 1:
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))

print("""
You may be familiar with De Morgan's laws. They say that:

The negation of a conjunction is the disjunction of the negations.

The negation of a disjunction is the conjunction of the negations.
""")

print("Let's write the same thing using Python:")

# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)