#sorted method is used to make given string in ascending oreder
name1 = input('enter a name1 ')
name2 = input('enter name2 ')
if len(name1)==len(name2):
    if sorted(name1)==sorted(name2):
        print('These are anagrams')
    else:
        print('These are not anagrams')
else:
    print('These are not anagrams')