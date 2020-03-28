import numpy as np

is_Day = int(input())
diff = np.diff(np.array([int(input()) for i in range(is_Day)]))
# diff = list([int(input()) for i in range(is_Day)])
print(diff)
for j in diff:
    if 0 == j:
        print("stay")
    elif 0 < j:
        print("up", diff[j])
    else:
        print("down", abs(diff[j]))
