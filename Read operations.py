file = open('Codingal.txt', 'r')
print("file in read ()")
file.close()

file = open('Codingal.txt', 'r')
print("\n Read in Parts \n")
print(file.read(10))
file.close()

file = open('Codingal.txt', 'a')
file.write("Hi I am Avni. I am learning python")
file.close()
