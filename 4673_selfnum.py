natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):  # i = 850
    for j in str(i):       # j = "8", "5", "0"
        i += int(j)        # 850 + 8 + 5 + 0 = 863
    generated_num.add(i)   # 생성자가 있는 숫자를 set list 로 중복을 없애면서 .add

self_num = sorted(natural_num - generated_num) # self_num = 생성자가 없는 자연수 (모든 자연수 - generated_num)
for i in self_num:
    print(i)