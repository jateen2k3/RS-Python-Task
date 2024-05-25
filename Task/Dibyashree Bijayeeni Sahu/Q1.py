def check_for_anagrams(string1,string2):
    word1=sorted(string1)
    word2=sorted(string2)

    if(word1==word2):
        print('they are anagrams')
    else:
        print('they are not anagrams')
string1='rat'
string2='tar'
check_for_anagrams(string1,string2)
