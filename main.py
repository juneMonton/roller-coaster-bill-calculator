print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

#if height==120:
#  print("You can ride the rollercoaster")
# else:
#   print("Sorry, you have to grow taller before you can ride")

# if height>=120:
#   print("You can ride the rollercoaster!")
#   age=int(input("What is your age?"))
#   if age<=18:
#     print("Please pay $7.")
#   else:
#     print("Please pay $12.")
# else:
#   print("Sorry, you have to grow taller before you can ride")

if height>=120:
  print("You can ride the rollercoaster!")
  age=int(input("What is your age?"))
  if age<12:
    bill=5
    print("Child tickets are $5.")
  elif age<=18:
    bill=7
    print("Teens tickets are $7.")
  else:
    bill=12
    print("Adult tickets are $12.")
  want_photo=input("Do you want a photo taken? Y or N.")
  if want_photo=="Y":
    bill+=3
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride")