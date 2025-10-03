def power (base, exponent):
    result = 1
    for a in range(exponent):
        result = result * base
    return result

print(power(2,3))