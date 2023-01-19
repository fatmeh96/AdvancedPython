def first_n_lines(file_path,n):
    data=""
    with open(file_path,'r') as myId:
        myId.seek(0)
        for i in range(n):
            data+=myId.readline()
    print(data)
first_n_lines('my_id.txt',1)
