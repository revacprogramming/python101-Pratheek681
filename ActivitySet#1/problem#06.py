# Loops & Iterators

largest = None
smallest = None


   
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    num = int(num)
    if largest is None or num>largest:
        largest = num
    elif smallest is None or num<smallest:
        smallest = num
   



print("Maximum", largest)
print("minimum",smallest)


