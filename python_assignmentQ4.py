#Open a file in read mode
f=open('test1.txt','r+')

#Read a file
data=f.read()

#Display the file content
print(data)

#Close the file
f.close()