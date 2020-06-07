import random
import string

nums = [str(i) for i in range(1, 10)]
for i in range(20):
    char_num = random.sample(nums, 3) + random.sample(string.ascii_lowercase, 5)
    code = random.sample(nums, 1) + random.sample(char_num, 8)
    print(''.join(code))
