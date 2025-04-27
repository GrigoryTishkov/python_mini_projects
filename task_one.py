n = int(input())
list1 = [int(x) for x in input().split()]
max_len = 0

for i in range(n):
    left, right = i, i

    while left >= 0 and right < n and list1[left] == list1[right]:
        current_len = right - left
        if current_len > max_len:
            max_len = current_len
        left -= 1
        right += 1

    left, right = i, i + 1
    while left >= 0 and right < n and list1[left] == list1[right]:
        current_len = right - left
        if current_len > max_len:
            max_len = current_len
        left -= 1
        right += 1
if max_len > 2:
    max_len += 1
print(max_len)
# 1 2 3 4 3 2 1
