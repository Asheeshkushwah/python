a={
"php":1200,
"python":1300,
"html":1400,
"angular":1500,
"company":1600
}

print(a.keys())
b=input("choice the course\n")


print("the course fee is:",a.get(b))