def differ_by(s1,s2):
    differ_n = 0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            differ_n += 1
    print(differ_n)

string1 = input('Please type the first string:\n')
string2 = input('Please type the second string:\n')
differ_by(string1,string2)