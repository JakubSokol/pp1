import mymath

input_value = None
random_value = None
while input_value == None or input_value != random_value:
    input_value=mymath.read_number()
    random_value=mymath.generate_number()
    if input_value != random_value:
        print("try again")
        print(f"input {input_value}, gen {random_value}")

print("you win")