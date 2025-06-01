file_string='PLAIN PLAN'


def find_distance(word1,word2):
    if len(word1)==0:
        return len(word2)
    elif len(word2)==0:
        return len(word1)
    elif word1[0]==word2[0]:
        return find_distance(word1[1:],word2[1:])
    else:
        return 1+min(find_distance(word1[1:],word2),find_distance(word1,word2[1:]),find_distance(word1[1:],word2[1:]))


word1,word2=file_string.split()

print(find_distance(word1,word2))
