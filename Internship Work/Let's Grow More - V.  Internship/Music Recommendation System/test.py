class Test:
    def init(self):
        self.x = 0

class Derived_Test(Test):
    def _init_(self):
        self.init()
        self.y = 1

def main():
    b = Derived_Test()
    print(b.x,b.y)

main()

# class a:
#     x = 200
#     def disp(self): 
#         print("Properties of base class 1:", self.x) 
        
# class b(a): 
#     y = 100 
#     def f1(self): 
#         self.disp() 
#         print("Properties of sub class 1:", self.y) 
        
# class c(a, b): 
#     z = 300 
#     def f2(self): 
#         self.f2() 
#         print("Properties of sub class 2:", self.z) 
        
        
        
# obj1 = c() 
# obj1.f2()
