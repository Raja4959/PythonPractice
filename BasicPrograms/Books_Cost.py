# 1.Suppose the price of a book is Rs.250, but bookstores get a 20%
# discount. Shipping costs are Rs.20 for the first five copies and Rs.5 for each
# additional copy. Write a program to calculate the total wholesale cost for 60
# copies? (5 MARKS)

book_cost = 250
discount = 20/100 #20%==0.2
no_of_books = 60

shipping_cost = (5*20)+((no_of_books-5)*5)  # finding total shipping cost

total_discount = book_cost*discount*no_of_books  # finding total discount

total_cost = book_cost * no_of_books  # actual cost

# cost after discouting and adding shipping cost
whole_sale_cost = total_cost + shipping_cost - total_discount

print("The total wholesale cost for 60 copies =", whole_sale_cost)
