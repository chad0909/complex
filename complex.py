'''
최동근: maintainer
이기욱: addition,subtraction
이혜미: multiplication

'''
class Complex:
    def __init__(self,re=0,im=0):
        self.re = re
        self.im = im
    def __str__(self):
        return str(self.re) + "+" + str(self.im) + "i"
    def multiply(self, c1):
        c = Complex()
        c.re = self.re * c1.re - self.im * c1.im
        c.im = self.re * c1.im + self.im * c1.re
        return c


c1 = Complex(1,2)
print(c1)

c2 = Complex(2,3)
print(c1.multiply(c2))
