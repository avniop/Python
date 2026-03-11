with open('Codingal.txt','w') as file:
    file.write("Hi i am Avni. I am learning python")
file.close()


with open('Codingal.txt','r') as file:
    data = file.readlines()
    print("Words in the file are-")
    for line in data:
        words = line.split()
        for line in data:
            word = line.split()
            print(word)
file.close()
    
