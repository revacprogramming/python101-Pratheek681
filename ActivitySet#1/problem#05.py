# Functions



def computepay(h, r):
  if h<40:
    pay = h*r
  elif h>40:
        pay = 40*r+(hrs-40)*1.5*rte
  return pay


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
