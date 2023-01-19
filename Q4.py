import string
def longest_word(file_path):
    with open(file_path,'r') as myId:
        myId.seek(0)
        str1=""
        for line in myId:
            for letter in line:
                if not string.punctuation.__contains__(letter):
                    str1+=letter
    str1=str1.split()
    max_length=0
    max_word=""
    for word in str1:
        if len(word)>max_length:
            max_word=word
    print(max_word)
longest_word('my_id.txt')