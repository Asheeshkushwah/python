sub1 =int(input("enter frist subject marks:\n"))
sub2 =int(input("enter frist subject marks:\n"))
sub3 =int(input("enter frist subject marks:\n"))



if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one subject")
elif(sub1+sub2+sub3)/3  <40:
    print("you are fail due to total percentage less than 40")
else:
    print("congatulation ! you passes the exam")    