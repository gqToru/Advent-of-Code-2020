# --- Day 2: Password Philosophy ---

acc = 0
new_acc = 0

data = open('./files/day2.txt')
for each_line in data:
    (policy, password) = each_line.split(': ')
    (rangePolicy, letter) = policy.split(' ')
    (min_policy, max_policy) = rangePolicy.split('-')
    count = password.count(letter)
    if(count >= int(min_policy) and count <= int(max_policy)):
        acc += 1

#     --- Part Two ---

    if (letter == password[int(min_policy)-1] or letter == password[int(max_policy)-1]) and (password[int(min_policy)-1] != password[int(max_policy)-1]):
        new_acc += 1

print('old policy: ', acc)
print('new policy: ', new_acc)