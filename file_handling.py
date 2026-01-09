f=open('data.txt','r+')

data=f.read()

date=f.write('Adding this new line\n')

print(data)

f.close()