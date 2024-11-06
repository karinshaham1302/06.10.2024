import statistics

# terms:
# 1
num1: int = int(input('Enter the first number:'))
num2: int = int(input('Enter the second number:'))
smallest = min(num1, num2)
for _ in range(3):
    print(smallest, end=' ')
print()

# 2
number1: int = int(input('Enter the first number:'))
number2: int = int(input('Enter the second number:'))
avg = statistics.mean([number1, number2])
print(f'The avg is: {avg}')
print()

# 3
num_1: int = int(input('Enter the first number:'))
num_2: int = int(input('Enter the second number:'))
num_3: int = int(input('Enter the third number:'))
largest = max(num_1, num_2, num_3)
print(f'The largest number is: {largest}')
print()

# 4
minutes = int(input('Enter the long of the movie in minutes:'))
hours = minutes // 60
minutes_left = minutes % 60
print(f' the movie is {hours} hours and {minutes_left} minutes')
print()

# 5
number = input('Enter a 4 digit number:')
right_num = number[-1]
print(f'Thr righter digit number is: {right_num}')
print()

# 6
number = input('Enter a 4 digit number:')
if len(number) == 4:
    second_dig = number[-2]
    print(f'Thr second digit number is: {second_dig}')
else:
    print('try again')
print()

# loops:
# 1
top = int(input('Enter a positive number:'))
for i in range(1, top + 1):
    print(i, end=' ')
print()

2
num1: int = int(input('Enter the first number:'))
num2: int = int(input('Enter the second number:'))
start = min(num1, num2)
end = max(num1, num2)
for i in range(start, end + 1):
    print(i, end=' ')
print()

# data:
# 1
total_sum = 0
SENTINEL = -99
while True:
    num = int(input('Enter a number:'))
    if num == SENTINEL:
        print(None)
        break
    else:
        total_sum += num
print('the total sum is:', total_sum)
print()

# 2
max_num = None
min_num = None
SENTINEL = -99
while True:
    num = int(input('Enter a number:'))
    if num == SENTINEL:
        print(None)
        break
    elif num <= 0:
        break
    elif max_num is None and min_num is None:
        max_num = num
        min_num = num
    elif num > max_num:
        (
            max_num) = num
    elif num < min_num:
        min_num = num
    else:
        max_num is not None and min_num is not None and min_num is not None
print(f'The highest number is: {max_num}')
print(f'The lowest number is: {min_num}')
print()

# 3
num1: int = int(input('Enter the first number:'))
num2: int = int(input('Enter the second number:'))
num3: int = int(input('Enter the third number:'))
num4: int = int(input('Enter the fourth number:'))
num5: int = int(input('Enter the fifth number:'))
if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    position = 1
elif num2 >= num3 and num2 >= num4 and num2 >= num5:
    position = 2
elif num3 >= num4 and num3 >= num5:
    position = 3
elif num4 >= num5:
    position = 4
else:
    position = 5
print(f' the highest number is at position {position}')
print()

# Complex loops:
# 2
count = 0
votes_for = []
votes_against = []
votes_abstain = []
votes_veto = []
vot_type = input('Enter the type of the vote:')
while count < 44:
    if votes_veto == 4:
        print(f'the country voting veto: {votes_veto[0]}')
        break
    try:
        vote = int(input(f'Enter the vote of the country {count}'))
        if vote == 1:
            votes_for.append(count)
        elif vote == 2:
            votes_against.append(count)
        elif vote == 3:
            votes_abstain.append(count)
        else:
            print('The vote is not correct')
    except ValueError:
        print('The vote is not correct')

print('total votes for:', len(votes_for))
print('total votes against:', len(votes_against))
print('total votes abstain:', len(votes_abstain))
if votes_for:
    print(f'The first country voting: {votes_for[0]}')
else:
    print('Non of the country vote for')
if votes_against:
    print(f'The last country voting: {votes_against[-1]}')
else:
    print('Non of the country vote against')

