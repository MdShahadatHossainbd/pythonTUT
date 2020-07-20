# Reverse string in Python
input_str = "GeeksForGeeks"

result = ''
for i in range(len(input_str)-1,-1,-1):
    result = result + input_str[i]
print(result)



#print(input_str[::-1])
#print(input_str[-1::-1])
#print(input_str[-7:])
"""
reverse_str = reversed(input_str)
print(''.join(reverse_str))
"""