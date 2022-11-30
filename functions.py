import pandas as pd

# check which user is logged in and return its username
def getLoggedUser():
    df_users = pd.read_csv('users.csv')
    for index, row in df_users.iterrows():
        if row['logged'] == True:
            return row['username']

# check if user logged in has admin access and return True/False
def verifyAdmin():
    df_users = pd.read_csv('users.csv')
    for index, row in df_users.iterrows():
        if row['logged'] == True & row['admin'] == True:
            return True
    print('Admin account is required')
    return False

# Inventory class 
class Inventory:
  def showInventory():
    df_inventory = pd.read_csv('inventory.csv')
    for index, row in df_inventory.iterrows():
      print(Book.getBookTitle(row['isbn']))
      print("Price: $", row['retailPrice'])
      print("ISBN: ", row['isbn'],"\n")

  # add book to inventory    
  def addBook(isbn, stock, retailPrice, purchaseCost):
      if(verifyAdmin() == True):
          df_inventory = pd.read_csv('inventory.csv')
          df_inventory.loc[len(df_inventory.index)] = [isbn, stock, retailPrice, purchaseCost]
          df_inventory.to_csv('inventory.csv', index=False)
  
  # remove book from inventory
  def removeBook(isbn):
      if(verifyAdmin() == True):
          df_inventory = pd.read_csv('inventory.csv')
          df_inventory = df_inventory[df_inventory['isbn'] != isbn]
          df_inventory.to_csv('inventory.csv', index=False)
  
  # update stock of book in inventory
  def updateStock(isbn, stock):
      if(verifyAdmin() == True):
          df_inventory = pd.read_csv('inventory.csv')
          i = None
          for index, row in df_inventory.iterrows():
              if row['isbn'] == str(isbn):
                  i = index
          df_inventory.at[i,'stock'] = stock
          df_inventory.to_csv('inventory.csv', index=False)
  
  # update purchase cost of book in inventory
  def updatePurchaseCost(isbn, purchaseCost):
      if(verifyAdmin() == True):
          df_inventory = pd.read_csv('inventory.csv')
          i = None
          for index, row in df_inventory.iterrows():
              if row['isbn'] == str(isbn):
                  i = index
          df_inventory.at[i,'purchaseCost'] = purchaseCost
          df_inventory.to_csv('inventory.csv', index=False)
  
  # update retail price of book in inventory
  def updateRetailPrice(isbn, retailPrice):
      if(verifyAdmin() == True):
          df_inventory = pd.read_csv('inventory.csv')
          i = None
          for index, row in df_inventory.iterrows():
              if row['isbn'] == str(isbn):
                  i = index
          df_inventory.at[i,'retailPrice'] = retailPrice
          df_inventory.to_csv('inventory.csv', index=False)
  
  # update isbn of book in inventory
  def updateIsbn(isbn, newIsbn):
      if(verifyAdmin() == True):
          df_inventory = pd.read_csv('inventory.csv')
          i = None
          for index, row in df_inventory.iterrows():
              if row['isbn'] == str(isbn):
                  i = index
          df_inventory.at[i,'isbn'] = newIsbn
          df_inventory.to_csv('inventory.csv', index=False)

# User Class
class User:
  # add user to users
  def addUser(username, displayName, password, email, address, zip, preferredPayment, logged, admin, orderHistory):
      df_users = pd.read_csv('users.csv')
      df_users.loc[len(df_users.index)] = [username, displayName, password, email, address, zip, preferredPayment, logged, admin, orderHistory]
      df_users.to_csv('users.csv', index=False)
  
  # delete user from users
  def deleteUser(username):
      df_users = pd.read_csv('users.csv')
      df_users = df_users[df_users['username'] != username]
      df_users.to_csv('users.csv', index=False)
  
  # log in a user
  def login(username, password):
      df_users = pd.read_csv('users.csv')
      i = None
      for index, row in df_users.iterrows():
        if(row['username'] == str(username)) & (row['password'] == str(password)):
          i = index
      if (i == None):
        print("failed to log in")
        return(False)
      else:
        df_users.at[i,'logged'] = True
        df_users.to_csv('users.csv', index=False)
        return(True)
  
  # log out a user
  def logout():
      username = getLoggedUser()
      df_users = pd.read_csv('users.csv')
      i = None
      for index, row in df_users.iterrows():
        if(row['username'] == username):
          i = index
      if (i == None):
        return(False)
      else:
        df_users.at[i,'logged'] = False
        df_users.to_csv('users.csv', index=False)
        return(True)
  
  # change username of user in users
  def changeUsername(newUsername):
      username = getLoggedUser()
      df_users = pd.read_csv('users.csv')
      i = None
      for index, row in df_users.iterrows():
        if row['username'] == username:
          i = index
      df_users.at[i,'username'] = newUsername
      df_users.to_csv('users.csv', index=False)
  
  # change display name of user in users
  def changeDisplayName(displayName):
      username = getLoggedUser()
      df_users = pd.read_csv('users.csv')
      i = None
      for index, row in df_users.iterrows():
        if row['username'] == username:
          i = index
      df_users.at[i,'displayName'] = displayName
      df_users.to_csv('users.csv', index=False)
  
  # change password of user in users
  def changePassword(password):
      username = getLoggedUser()
      df_users = pd.read_csv('users.csv')
      i = None
      for index, row in df_users.iterrows():
        if row['username'] == username:
          i = index
      df_users.at[i,'password'] = password
      df_users.to_csv('users.csv', index=False)

  # change email of user in users 
  def changeEmail(email):
      username = getLoggedUser()
      df_users = pd.read_csv('users.csv')
      i = None
      for index, row in df_users.iterrows():
        if row['username'] == username:
          i = index
      df_users.at[i,'email'] = email
      df_users.to_csv('users.csv', index=False)
  
  # change address of user in users
  def changeAddress(address):
      username = getLoggedUser()
      df_users = pd.read_csv('users.csv')
      i = None
      for index, row in df_users.iterrows():
        if row['username'] == username:
          i = index
      df_users.at[i,'address'] = address
      df_users.to_csv('users.csv', index=False)
  
  # change zip of user in users
  def changeZip(zip):
      username = getLoggedUser()
      df_users = pd.read_csv('users.csv')
      i = None
      for index, row in df_users.iterrows():
        if row['username'] == username:
          i = index
      df_users.at[i,'zip'] = zip
      df_users.to_csv('users.csv', index=False)
  
  # change preferred payment of user in users
  def changePreferredPayment(preferredPayment):
      username = getLoggedUser()
      df_users = pd.read_csv('users.csv')
      i = None
      for index, row in df_users.iterrows():
        if row['username'] == username:
          i = index
      df_users.at[i,'preferredPayment'] = preferredPayment
      df_users.to_csv('users.csv', index=False)

  def addOrderHistory(order):
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
      if row['username'] == username:
        i = index
    df_users.at[i,'orderHistory'] += order
    df_users.to_csv('users.csv', index=False)

  def showOrderHistory():
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    for index, row in df_users.iterrows():
      if row['username'] == str(username):
        print(row['orderHistory'])
  

# Cart class
class Cart:
  # show cart of a user
  def showCart():
    username = getLoggedUser()
    df_cart = pd.read_csv('cart.csv')
    for index, row in df_cart.iterrows():
      if(row['username'] == username):
        print(Book.getBookTitle(row['isbn']))
        print("Price: $", row['retailPrice'])
    print("\nYour total is: $",Cart.totalPrice())

  # check inventory if book is available
  def checkInventory(isbn):
    df_inventory = pd.read_csv('inventory.csv')
    for index, row in df_inventory.iterrows():
      if (row['isbn'] == str(isbn)) & (row['stock'] > 0):
        return True
    return False

  # add item to user's cart
  def addItem(isbn):
    username = getLoggedUser()
    df_cart = pd.read_csv('cart.csv')
    df_inventory = pd.read_csv('inventory.csv')
    retailPrice = None
    for index, row in df_inventory.iterrows():
      if (row['isbn'] == str(isbn)):
        retailPrice = row['retailPrice']
    if (retailPrice == None):
      print("Not a valid ISBN, try again")
    else:
      df_cart.loc[len(df_cart.index)] = [isbn, retailPrice, username]
      df_cart.to_csv('cart.csv', index=False)

  # remove item from user's cart
  def removeItem(isbn):
    username = getLoggedUser()
    df_cart = pd.read_csv('cart.csv')
    i = None
    for index, row in df_cart.iterrows():
      if ((row['isbn'] == str(isbn)) & (row['username'] == username)):
        i = index
    df_cart.drop(i, axis=0, inplace=True)
    df_cart.to_csv('cart.csv', index=False)
  
  # get total price of user's cart
  def totalPrice():
    username = getLoggedUser()
    df_cart = pd.read_csv('cart.csv')
    totalPrice = 0
    for index, row in df_cart.iterrows():
      if(row['username'] == username):
        totalPrice = totalPrice + row['retailPrice']
    return totalPrice

  # checkout user's cart
  def checkout():
    username = getLoggedUser()
    df_cart = pd.read_csv('cart.csv')
    df_inventory = pd.read_csv('inventory.csv')
    #adding the cart to the order history of the user
    order = "Order: "
    for index, row in df_cart.iterrows():
      if(row['username'] == username):
        order += Book.getBookTitle(row['isbn'])
        order += "Price: $" + str(row['retailPrice'])
    order += "Order total: $"+str(Cart.totalPrice())
    User.addOrderHistory(order)
    
    for index, row in df_cart.iterrows():
      if row['username'] == str(username):
        isbn = row['isbn']
        i = None
        stock = None
        for index, row in df_inventory.iterrows():
          if row['isbn'] == str(isbn):
            i = index
            stock = row['stock']
        df_inventory.at[i,'stock'] = stock - 1     
    df_cart = df_cart[df_cart['username'] != str(username)]
    df_cart.to_csv('cart.csv', index=False)
    df_inventory.to_csv('inventory.csv', index=False)

# Book class
class Book:
  # show book data
  def showBookInfo(isbn):
    print("Title: ", Book.getBookTitle(isbn))
    print("Author: ", Book.getBookGenre(isbn))
    print("Genre: ", Book.getBookAuthor(isbn))
    print("Release Date: ", Book.getBookDate(isbn))
  
  # add book to books
  def newBook(isbn, title, genre, author, datePublished):
    df_books = pd.read_csv('books.csv')
    df_books.loc[len(df_books.index)] = [isbn, title, genre, author, datePublished]
    df_books.to_csv('books.csv', index=False)

  # get book title from its isbn
  def getBookTitle(isbn):
    df_books = pd.read_csv('books.csv')
    for index, row in df_books.iterrows():
      if row['isbn'] == str(isbn):
          return(row['title'])
  
  # get book genre from its isbn
  def getBookGenre(isbn):
    df_books = pd.read_csv('books.csv')
    for index, row in df_books.iterrows():
      if row['isbn'] == str(isbn):
        return(row['genre'])

  # get book author from its isbn
  def getBookAuthor(isbn):
    df_books = pd.read_csv('books.csv')
    for index, row in df_books.iterrows():
      if row['isbn'] == str(isbn):
        return(row['author'])
  
  # get book's date of publication from its isbn
  def getBookDate(isbn):
    df_books = pd.read_csv('books.csv')
    for index, row in df_books.iterrows():
      if row['isbn'] == str(isbn):
          return(row['datePublished'])
  
  # change book title in books
  def changeBookTitle(isbn, title):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "title"] = title
    df_books.to_csv('books.csv', index=False)

   # change book genre in books
  def changeBookGenre(isbn, genre):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "genre"] = genre
    df_books.to_csv('books.csv', index=False)

  # change book author in books
  def changeBookAuthor(isbn, author):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "author"] = author
    df_books.to_csv('books.csv', index=False)

   # change book publication date in books
  def changeBookDate(isbn, datePublished):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "datePublished"] = datePublished
    df_books.to_csv('books.csv', index=False)

   # change book isbn in books
  def changeBookIsbn(isbn, newIsbn):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "isbn"] = newIsbn
    df_books.to_csv('books.csv', index=False)
