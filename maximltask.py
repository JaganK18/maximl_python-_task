str=input()
n=len(str)
len_ans=10000000
max_char_distinct=1
for i in range(n):
    for j in range(i+1,n+1):
        sub_str=str[i:j]
        len_sub=len(sub_str)
        max_char=len(set(sub_str))
        if(max_char>max_char_distinct):
            len_ans=len_sub
            max_char_distinct=max_char
        elif(max_char==max_char_distinct):
            if(len_ans>len_sub):
                len_ans=len_sub
print(len_ans)

