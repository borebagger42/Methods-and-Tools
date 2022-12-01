import functions as fn

#Global Variable Declaration
logTest = True
introScreen = True
menuScreen = True

#logs out any users still active
while(logTest):
  logTest = fn.User.logout()

#Prompts the user to select a number and stores it in global variable sel  
def select():
  global sel
  inpCheck = True
  while(inpCheck):
    print("Your Selection: ", end="")
    sel = input()
    if (sel.isdigit()):
      sel = int(sel)
      inpCheck = False
      return(sel)
    else:
      print("You did not type a valid integer, please try again")
  

print("Welcome to our shop! \nTo navigate our menu: \nPlease type the integer value associated with the option you would like to select and no other characters!")
while (introScreen): #Loops until someone exits
  print("\n1. Log In \n2. Create Account \n3. Exit")
  selI = select()
  if (selI == 1): #Log in option
    print("Please enter your username: ", end="")
    username = input()
    print("Please enter your password: ", end="")
    password = input()
    if (fn.User.login(username,password)):
      print("Congrats you are logged in")
      menuScreen = True
  elif (selI == 2): #Create account option
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
    menuScreen = True
  elif(selI == 3): #Exit option
    introScreen = False
    menuScreen = False
  else:
    menuScreen = False
    
  while (menuScreen): #Loops until someone logs out, deletes their account, or exits
    print("\nHere are your options: ")
    print("1. Change Account Info \n2. Edit/View Cart \n3. View Inventory \n4. View Book Information \n5. Checkout (This will add your current cart to your Order History) \n6. View Order History \n7. Add to Order History \n8. Logout \n9. Delete Account \n10. Exit")
    selM = select()
    if (selM == 1): #Another branch of the menu to change all account options
      print("1. Change username \n2. Change Display Name \n3. Change Password \n4. Change Email \n5. Change Address \n6. Change Zip \n7. Change Preferred Payment \n8. Exit")
      selAO = select()
      print("Please enter your updated information: ", end="")
      updatedInfo = input()
      if (selAO == 1): #Each of these if branches are different types of account info to change
        fn.User.changeUsername(updatedInfo)
        print("Your Username has been updated")
      elif (selAO == 2):
        fn.User.changeDisplayName(updatedInfo)
        print("Your Display Name has been updated")
      elif (selAO == 3):
        fn.User.changePassword(updatedInfo)
        print("Your Password has been updated")
      elif (selAO == 4):
        fn.User.changeEmail(updatedInfo)
        print("Your Email has been updated")
      elif (selAO == 5):
        fn.User.changeAddress(updatedInfo)
        print("Your Address has been updated")
      elif (selAO == 6):
        fn.User.changeZip(updatedInfo)
        print("Your Zip has been updated")
      elif (selAO == 7):
        fn.User.changePreferredPayment(updatedInfo)
        print("Your Preffered Payment has been updated")
      elif (selAO == 8): #Exit option
        menuScreen = False
        introScreen = False
      
    elif (selM == 2):  #Show inventory option
      print("\nHere are your options: ")
      print("1. View Cart \n2. Add To Cart \n3. Remove From Cart \n4. Exit")
      selC = select()
      if(selC == 1): #Show cart Option
        fn.Cart.showCart()
      elif(selC == 2): #Add to cart option
        print("Please enter the ISBN of the book you want to purchase: ", end="")
        isbn = input()
        fn.Cart.addItem(isbn)
        print(fn.Book.getBookTitle(isbn), "added to cart \n")
      elif(selC == 3): #Remove from Cart option
        print("Please enter the ISBN of the book you want to remove from your cart: ", end="")
        isbn = input()
        fn.Cart.removeItem(isbn)
        print(fn.Book.getBookTitle(isbn), "removed from cart \n")
      elif(selC == 4): #Exit option
        menuScreen = False
        introScreen = False
    elif (selM == 3): #Show inventory option
      fn.Inventory.showInventory()
    elif (selM == 4): #View book information option
      print("Please enter the ISBN of the book you would like to see the information about: ", end="")
      isbn = input()
      fn.Book.showBookInfo(isbn)
    elif (selM == 5): #Check out option
      fn.Cart.checkout()
      print("You have checked out! \n")
    elif (selM == 6): #Show order history option
      fn.User.showOrderHistory()
    elif(selM == 7): #Add to order history option
      print("Please enter the order details: ", end="")
      order = input()
      fn.User.addOrderHistory(order)
    elif (selM == 8): #Logout option
      fn.User.logout()
      menuScreen = False
    elif (selM == 9): #delete account option
      print("Please enter your current username: ", end="")
      username = input()
      fn.User.deleteUser(username)
      print("Your account has been deleted \nexiting...")
      menuScreen = False
    elif (selM == 10): #Exit option
      menuScreen = False
      introScreen = False
