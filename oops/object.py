class rjit:
    compony ="pninfosys"
    age=23
    collage="itm"

    def itm(self,h):
        print(f"HELLO ITM{ self.compony}is {self.age}is{self.collage}\n{h}")
        print(h)


ram = rjit()
# raj =rjit()
print(ram.compony)
ram.itm(23) 
ram.compony="google" 
ram.itm(23)
print(ram.compony)
print(ram.age)
print(ram.compony)
ram.itm("gwalior")    