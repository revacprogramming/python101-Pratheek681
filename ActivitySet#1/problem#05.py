# Functions


def computepay(h, r):
  if h<40:
    pay = h*r
   elif h>40
      pay = 1.5*h*r
return pay


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
