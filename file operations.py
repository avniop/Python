file_read = open('Codingal.txt', 'r')
print("file in read mode-")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode-")
file_write.write("Hi i am Avni. I am learning python")
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("File in append mode-")
file_append.write("I am enjoying learning python")
file_append.close()