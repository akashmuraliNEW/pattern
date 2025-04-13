import array
with open('fileHandling/files.txt','r') as f:
    text = f.read()
    for i in text:
        print(i,end='')
        array