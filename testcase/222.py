class a:
    def a(self,aa):
        print(self,aa)
class b(a):
    def b(self,bb):
        print(self,bb)
class c(b):
    def c(self,cc):
        print(self,cc)
p1=c()
p1.a(aa=123)
p1.b(bb=456)
p1.c(cc=789)

