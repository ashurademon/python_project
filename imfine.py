f=open("D:\Python_project\Vaccine Trials.csv",'r')
line=f.readlines()
print(line[2])
ln = line[2].split(",")
print(ln)
print(ln[5])