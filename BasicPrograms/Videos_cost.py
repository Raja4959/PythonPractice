# 4.A video library rents new videos for Rs.75 a day and old movies for Rs.50 a day. Write a program
# to calculate the total charge for a customer’s video rentals. The program should prompt the user
# for the number of each type of video and output the total cost. (4MARKS)

new_videos = int(input("number of new videos : "))
old_videos = int(input("number of old videos : "))
no_of_days = int(input("number of days : "))
total_cost = (new_videos*75*no_of_days) + (old_videos*50*no_of_days)
print("The total cost is ", total_cost)
