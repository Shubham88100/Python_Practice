#Create a file
f=open('test2.txt','w+')

#Write a file
data=f.write("Hey, I am learning python \n")
f.seek(0)

#Open/Read the file
data1=f.read()

#Print the data of file
print(data1)

#Close the file
f.close()






