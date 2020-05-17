print("How many kilometers did you run?")
kms=input()
print("okay you said, " + kms)

miles= float(kms)/1.60934 

print(f"You ran {round(miles,2)} miles today ")