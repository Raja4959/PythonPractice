def single_digit(n):
    if n<10:
        return n
    else:
        total =0
        number = n
        while number > 0:
            d = number %10
            total = total + d
            number = number //10
        return single_digit(total)
        
reg = "AP39MG8127"
num = 116391378127
print("coding numbers",single_digit(num))

total = 0
unit_sum = 0
for char in reg:
    total = total + ord(char)
    unit_sum += single_digit(total)

print("sum ",single_digit(total))
print("unit_sum ",single_digit(unit_sum))
        
        
