# 2.6.6 More about input() and type casting

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))

hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypothenuse length is", hypo)

print("///")

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)