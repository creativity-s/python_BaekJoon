croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
# replace 함수 사용
for i in croatia:
    word = word.replace(i, '*') # input변수와 동일한 변수를 *로 치환

print(len(word))