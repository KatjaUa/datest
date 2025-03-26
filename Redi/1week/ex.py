
x = [1, 2, "hi"]
for i in range(0, len(x)-1):
    print(i, x[i])


print()

y = [1, 2, "hi"]
y[0:2]
for i in range(0, len(y)-1):
    print(i, y[i])   


w = float(input("Weight (kg): "))
h = float(input("Height (cm): ")) / 100  # Convert cm to m

bmi = w / (h * h)

if bmi < 18.5:
    cat = "Underweight"
elif bmi < 24.9:
    cat = "Normal"
elif bmi < 29.9:
    cat = "Overweight"
else:
    cat = "Obese"

print(f"BMI: {bmi:.2f}\nCategory: {cat}")


