# Loops & Iterators
largest = None
smallest = None
while True:
 try:
      num = input("Enter a number: ")
      if num == "done":
        break
      num = int(num)
      if largest is None or num>largest:
        largest=num
      elif smallest is None or num<smallest:
         smallest=num

 except ValueError:
      print("Invalid!!!")
      continue



print("Maximum", largest)
print("Minimum", smallest)

