m1=int(input("Enter marks: "))
m2=int(input("Enter marks: "))
m3=int(input("Enter marks: "))
if m1<=m3 and m1<=m2:
    avgMarks=(m2+m3)/2
elif m2<=m1 and m2<=m3:
    avgMarks=(m1+m3)/2
elif m3<=m1 and m3<=m2:
    avgMarks=(m2+m1)/2
print("Average of best two: ",avgMarks)
