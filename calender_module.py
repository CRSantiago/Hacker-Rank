# Task

# You are given a date. Your task is to find what the day is on that date.

# Input Format

# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

# Output Format

# Output the correct day in capital letters.

# Sample Input

# 08 05 2015
# Sample Output

# WEDNESDAY
# Explanation

# The day on August 15th 2015 was WEDNESDAY.

import calendar

if __name__ == '__main__':
    weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

    get_date = input("Enter a date in MM DD YYYY format and we will return the day of the week!")
    (month,day,year) = map(int, get_date.split())
    weekday = calendar.weekday(year,month,day)
    print(weekdays[weekday])