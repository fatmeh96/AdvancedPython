import string
def words_frequency(file_path):
    with open(file_path,'r') as myId:
        myId.seek(0)
        str1=""
        dic1={}
        for line in myId:
            for letter in line:
                if not string.punctuation.__contains__(letter):
                    str1+=letter
    str1=str1.split()
    for word in str1:
        dic1[word]=str1.count(word)
    print(dic1)
    return dic1
words_frequency('my_id.txt')