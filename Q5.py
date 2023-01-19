def reversed_string(str1):
    str2=""
    str1=str1.split()
    str1=str1[::-1]
    for word in str1:
        str2+=word
        str2+=" "
    print(str2)
reversed_string("hi there my name is fatmeh")