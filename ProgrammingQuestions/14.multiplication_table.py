# 1. table for given number
def multiplication_table(number, start=1, end=10):
    for i in range(start, end + 1):
        result = number * i
        print(f"{number} x {i} = {result}")


# 2. Tables for given range
def multiplication_tables_for_range(start, end, table_range=10):
    for num in range(start, end + 1):
        print(f"\nMultiplication table for {num}:\n")
        for i in range(1, table_range + 1):
            result = num * i
            print(f"{num} x {i} = {result}")


# 1.Example usage:
given_number = int(input("Enter the number for the multiplication table: "))
multiplication_table(given_number)

# 2.Example usage:
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
# table_range = int(input("Enter the range for multiplication tables: "))
multiplication_tables_for_range(start_range, end_range)
