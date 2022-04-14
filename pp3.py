k = int(input())
R_no = input().split()
R_no.sort()
i=0
crn=0
while i<len(R_no):
    if(i+k < len(R_no)):
        if(R_no[i] != R_no[i+k-1]):
            crn = R_no[i]
        else:
            i = i+k
    else:
        crn = R_no[i]
    i= i+1
print("The captain's room number is:",crn)