def add_two_strings_by_parts(num1, num2, initial_carry=0):
    max_length = max(len(num1), len(num2))
    
    # Equalize the lengths of the numbers
    if len(num1) > len(num2):
        num2 = ("0" * (max_length - len(num2))) + num2
    elif len(num1) < len(num2):
        num1 = ("0" * (max_length - len(num1))) + num1

    result = []
    carry = initial_carry

    # Traverse the strings from right to left
    for i in range(max_length - 1, -1, -1):
        total = int(num1[i]) + int(num2[i]) + carry
        digit = total % 10
        carry = total // 10
        result.append(str(digit))

    # Add the final carry if exists
    if carry:
        result.append(str(carry))

    # Reverse the result and convert to string
    return ''.join(result[::-1])

def add_two_strings(num1, num2):
    num1_main, num1_frac = num1.split(".")[0], num1.split(".")[1]
    num2_main, num2_frac = num2.split(".")[0], num2.split(".")[1]

    max_frac_len = max(len(num1_frac), len(num2_frac))
    num1_frac += '0' * (max_frac_len - len(num1_frac))
    num2_frac += '0' * (max_frac_len - len(num2_frac))

    frac_sum = add_two_strings_by_parts(num1_frac, num2_frac)

    initial_carry = 0
    if len(frac_sum) > max_frac_len:
        initial_carry = 1
        frac_sum = frac_sum[1:]    

    main_sum = add_two_strings_by_parts(num1_main, num2_main, initial_carry)
    return main_sum + "." + frac_sum

# Example usage
print(add_two_strings("123.456", "77.345"))  # Output should reflect the sum of the two numbers
