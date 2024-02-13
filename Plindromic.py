import time

# NAIVE
def is_Palindromic(p):
    j = len(p)-1
    for i in range(int(len(p)/2)):
        if p[i] == p[j]:
            j-=1
        else :
            return 0
    return 1


# RECURSION
def is_Palindromic_recursion(p):
    i = 0
    j = len(p)-1

    if i==j:
        return True
    if i+1 > j-1:
        return p[i]==p[j]

    return p[i]==p[j] and is_Palindromic_recursion(p[i+1:j])

print(is_Palindromic_recursion('aabcobaa'))



# NAIVE
my_list = set()
def LongestPalidromicChain_N(p):
    t1 = time.time()
    for i in range(1, int(len(p))):
        for j in range(len(p)-i):
            val = is_Palindromic(p[j:j+i+1])
            if val:
                my_list.add(p[j:j+i+1])

    t2 = time.time()
    print('Time Naiive:', t2-t1)

    return my_list

# print(LongestPalidromicChain_N("aaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkjaaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkjaaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkjaaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkjaaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkj"))     # 9 (0-9)


# DYNAMIC PROGRAMMING
# my_list = set()
# word = ''
# def LongesPalidromicChain_DP(p):
#     t1 = time.time()
#     cache = {}

#     for i in range(1, int(len(p))):
#         for j in range(len(p)-i):
#             word = p[j:j+i+1]
#             if word in cache:
#                 if cache[word]:
#                     my_list.add(word)
#             else:
#                 cache[word] = is_Palindromic(word)
#                 if cache[word]:
#                     my_list.add(word)

#     t2 = time.time()
#     print('Time DP: ', t2-t1)

#     return my_list



# print(LongesPalidromicChain_DP("asdfabcbajabaj"))     # 14 (0-14)
# print(LongesPalidromicChain_DP("aaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkjaaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkjaaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkjaaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkjaaabcbaaaa;lskdjflaskdjfosdgnoaiergnoaeringoarengeokedfgndsafgjjjjjjjjjjjkkkkkkkjdlfkjlkj"))     # 9 (0-9)


