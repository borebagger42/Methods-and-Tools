import functions as fn

#Global Variable Declaration
logTest = True
introScreen = True
menuScreen = True
sel = None

#logs out any users still active
while(logTest):
  logTest = fn.User.logout()

#Prompts the user to select a number and stores it in sel  
def select():
  global sel
  inpCheck = True
  while(inpCheck):
    print("Your Selection: ", end="")
    sel = input()
    if (sel.isdigit()):
      sel = int(sel)
      inpCheck = False
    else:
      print("You did not type a valid integer, please try again")
  

print("Welcome to our shop! \nTo navigate our menu: \nplease type the integer value associated with the option you would like to select and no other characters!")
while (introScreen): #Loops until someone succesfully logs in, creates an account, or exits
  print("\n1. Log In \n2. Create Account \n3. Exit")
  select()
  if (sel == 1):
    print("Please enter your username: ", end="")
    username = input()
    print("Please enter your password: ", end="")
    password = input()
    if (fn.User.login(username,password)):
      print("Congrats you are logged in")
  elif (sel == 2):
    print("Please enter your username: ", end="")
    username = input()
    print("Please enter your displayName: ", end="")
    displayName = input()
    print("Please enter your password: ", end="")
    password = input()
    print("Please enter your email: ", end="")
    email = input()
    print("Please enter your address: ", end="")
    address = input()
    print("Please enter your zip: ", end="")
    zip = input()
    print("Please enter your preferred payment: ", end="")
    preferredPayment = input()
    fn.User.addUser(username, displayName, password, email, address, zip, preferredPayment, True, True,"Order History: ")
    print("Congrats you have added an account and are logged in!" )
  elif(sel == 3):
    introScreen = False
    menuScreen = False
    
  while (menuScreen):
    print("\nHere are your options: ")
    print("1. Change Account Info \n2. View Inventory \n3. View Cart \n4. Add To Cart \n5. Remove From Cart \n6. Checkout (This will add the order to your Order History) \n7. View Order History \n8. Logout \n9. Delete Account \n10. Exit")
    select()
    if (sel == 1):
      print("1. Change username \n2. Change Display Name \n3. Change Password \n4. Change Email \n5. Change Address \n6. Change Zip \n7. Change Preferred Payment \n8. Exit")
      select()
      print("Please enter your updated information: ", end="")
      updatedInfo = input()
      if (sel == 1):
        fn.User.changeUsername(updatedInfo)
        print("Your Username has been updated")
      if (sel == 2):
        fn.User.changeDisplayName(updatedInfo)
        print("Your Display Name has been updated")
      if (sel == 3):
        fn.User.changePassword(updatedInfo)
        print("Your Password has been updated")
      if (sel == 4):
        fn.User.changeEmail(updatedInfo)
        print("Your Email has been updated")
      if (sel == 5):
        fn.User.changeAddress(updatedInfo)
        print("Your Address has been updated")
      if (sel == 6):
        fn.User.changeZip(updatedInfo)
        print("Your Zip has been updated")
      if (sel == 7):
        fn.User.changePreferredPayment(updatedInfo)
        print("Your Preffered Payment has been updated")
      if (sel == 8):
        menuScreen = False
        introScreen = False
      
    if (sel == 2): 
      fn.Inventory.showInventory()
    if (sel == 3):
      fn.Cart.showCart()
    if (sel == 4):
      print("Please enter the ISBN of the book you want to purchase: ", end="")
      isbn = input()
      fn.Cart.addItem(isbn)
      print(fn.Book.getBookTitle(isbn), "added to cart \n")
    if (sel == 5):
      print("Please enter the ISBN of the book you want to remove from your cart: ", end="")
      isbn = input()
      fn.Cart.removeItem(isbn)
      print(fn.Book.getBookTitle(isbn), "removed from cart \n")
    if (sel == 6):
      fn.Cart.checkout()
      print("You have checked out! \n")
    if (sel == 7):
      fn.User.showOrderHistory()
    if (sel == 8):
      fn.User.logout()
      menuScreen = False
    if (sel == 9):
      print("Please enter your current username: ", end="")
      username = input()
      fn.User.deleteUser(username)
      print("Your account has been deleted \nexiting...")
      menuScreen = False
    if (sel == 10):
      menuScreen = False
      introScreen = False
