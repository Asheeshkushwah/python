a = {
    "name":"pninfosys",
    "collage":"rjit",
    #"collage":"itm" , #duplicates not allowed
    "mark":[1,2,3,4,] , #list
    "education":{'ram':'mca'},
    1:2,

}

# print(a["name12"])
# print(a.get("name12"))
# print(a.get("collage123"))
# print(a['collage'])

# print(a.keys())
# print(type(a.keys()))
# print(type(a.list()))
# print(a.values())
# print(a.items())

#update dictionary

# updatedict ={
#     "branch":"it",
#     "phone":2134567,
#     "salary":4000,
#     "name":"rohit"  #update

# }
# a.update(updatedict) #update the dictionary
# print(a)

#get
try:
    print(a["name123"])
except Exception as w:
        print(w)
print(a["collage"])

