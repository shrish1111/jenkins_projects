def palindrome():
    str1=input("Enter a string: ")
    str1_list=list(str1)
    str2_list=[]
    length=int(len(str1))
    i=-1
    while i>=(-length):
        str2_list.append(str1_list[i])
        i-=1
    if str1_list==str2_list:
        print("it is palindrome")
        print(str1_list)
        print(str2_list)
    else:
        print("it is not palindrome")
        print(str1_list)
        print(str2_list)
palindrome()
