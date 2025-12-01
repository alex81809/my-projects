def is_armstrong(num):
    "Checks if a number is an Armstrong number."
    
    s_num = str(num)
    order = len(s_num)
    
    sum_of_powers = 0
    temp_num = num
    
    while temp_num > 0:
        digit = temp_num % 10
        
        sum_of_powers += digit ** order

        temp_num //= 10
    return num == sum_of_powers

try:
    number_to_check = int(input("Enter a number to check: "))

    if number_to_check < 0:
        print("Please enter a non-negative integer.")
    elif is_armstrong(number_to_check):
        print(f"✅ {number_to_check} is an Armstrong number.")
    else:
        print(f"❌ {number_to_check} is not an Armstrong number.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
