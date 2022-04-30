
#program to print the number of lines with the word error from the file

#open the file using the location of folder
file1=open(r'C:\Users\Ak\Downloads\Telegram Desktop\workfile.log', "r")
l = file1.readlines()
ls = []
n = 0
w='error'
for l in l:
    if w in l:
        ls.insert(n, l)
        n += 1
file1.close()
if len(ls)!=0:
    length = len(ls)
    print("Lines containing the word error are - ")
    for i in range(length):
        print(end=ls[i])
print(length,'= TOTAL NUMBER OF LINES WITH THE WORD ERROR')


