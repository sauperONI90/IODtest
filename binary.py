def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]
    return binary_str.zfill(8)

def negative_decimal_to_binary(decimal):
    binary_str = bin(abs(decimal))[2:].zfill(8)
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    twos_complement_int = int(inverted, 2) + 1
    twos_complement_binary = bin(twos_complement_int)[2:].zfill(8)
    return twos_complement_binary

user_input = int(input("Enter a decimal number: "))
if user_input >= 0:
    binary_result = decimal_to_binary(user_input)
else:
    binary_result = negative_decimal_to_binary(user_input)
print("Binary:", binary_result)
