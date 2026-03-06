# Day 2
# Script that processes a list of users
# prints only adult users (18+)
# and calculates the average age.

users = [
    {"name": "John", "age": 25},
    {"name": "Mark", "age": 17},
    {"name": "Bob", "age": 30},
    {"name": "James", "age": 15},
    {"name": "Luke", "age": 22},
    {"name": "Joe", "age": 26}
]


count_adults = 0
sum_adults = 0

sum_all = 0

for user in users:
    if user["age"] >= 18:
        print(f'{user["name"]} is an adult')
        sum_adults += user["age"]
        count_adults += 1
    sum_all += user["age"]

print(f'Average age of all users: {sum_all / len(users)}')
print(f'Average age of Adults: {sum_adults / count_adults}')

