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
def addBook(isbn, stock, retailPrice, purchaseCost):
    if(verifyAdmin() == True):
        df_inventory = pd.read_csv('inventory.csv')
        df_inventory.loc[len(df_inventory.index)] = [isbn, stock, retailPrice, purchaseCost]
        df_inventory.to_csv('inventory.csv', index=False)

def removeBook(isbn):
    if(verifyAdmin() == True):
        df_inventory = pd.read_csv('inventory.csv')
        df_inventory = df_inventory[df_inventory['isbn'] != isbn]
        df_inventory.to_csv('inventory.csv', index=False)

def updateStock(isbn, stock):
    if(verifyAdmin() == True):
        df_inventory = pd.read_csv('inventory.csv')
        i = None
        for index, row in df_inventory.iterrows():
            if row['isbn'] == str(isbn):
                i = index
        df_inventory.at[i,'stock'] = stock
        df_inventory.to_csv('inventory.csv', index=False)

def updatePurchaseCost(isbn, purchaseCost):
    if(verifyAdmin() == True):
        df_inventory = pd.read_csv('inventory.csv')
        i = None
        for index, row in df_inventory.iterrows():
            if row['isbn'] == str(isbn):
                i = index
        df_inventory.at[i,'purchaseCost'] = purchaseCost
        df_inventory.to_csv('inventory.csv', index=False)

def updateRetailPrice(isbn, retailPrice):
    if(verifyAdmin() == True):
        df_inventory = pd.read_csv('inventory.csv')
        i = None
        for index, row in df_inventory.iterrows():
            if row['isbn'] == str(isbn):
                i = index
        df_inventory.at[i,'retailPrice'] = retailPrice
        df_inventory.to_csv('inventory.csv', index=False)

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
def addUser(username, displayName, password, email, address, zip, preferredPayment, logged, admin):
    df_users = pd.read_csv('users.csv')
    df_users.loc[len(df_users.index)] = [username, displayName, password, email, address, zip, preferredPayment, logged, admin]
    df_users.to_csv('users.csv', index=False)

def deleteUser(username):
    df_users = pd.read_csv('users.csv')
    df_users = df_users[df_users['username'] != username]
    df_users.to_csv('users.csv', index=False)

def login(username, password):
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
            if(row['username'] == str(username)) & (row['password'] == str(password)):
                i = index
    df_users.at[i,'logged'] = True
    df_users.to_csv('users.csv', index=False)

def logout():
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
            if(row['username'] == username):
                i = index
    df_users.at[i,'logged'] = False
    df_users.to_csv('users.csv', index=False)

def changeUsername(newUsername):
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
        if row['username'] == username:
            i = index
    df_users.at[i,'username'] = newUsername
    df_users.to_csv('users.csv', index=False)

def changeDisplayName(displayName):
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
        if row['username'] == username:
            i = index
    df_users.at[i,'displayName'] = displayName
    df_users.to_csv('users.csv', index=False)

def changePassword(password):
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
        if row['username'] == username:
            i = index
    df_users.at[i,'password'] = password
    df_users.to_csv('users.csv', index=False)

def changeEmail(email):
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
        if row['username'] == username:
            i = index
    df_users.at[i,'email'] = email
    df_users.to_csv('users.csv', index=False)

def changeAddress(address):
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
        if row['username'] == username:
            i = index
    df_users.at[i,'address'] = address
    df_users.to_csv('users.csv', index=False)

def changeZip(zip):
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
        if row['username'] == username:
            i = index
    df_users.at[i,'zip'] = zip
    df_users.to_csv('users.csv', index=False)

def changePreferredPayment(preferredPayment):
    username = getLoggedUser()
    df_users = pd.read_csv('users.csv')
    i = None
    for index, row in df_users.iterrows():
        if row['username'] == username:
            i = index
    df_users.at[i,'preferredPayment'] = preferredPayment
    df_users.to_csv('users.csv', index=False)

# Cart class
def checkInventory(isbn):
    df_inventory = pd.read_csv('inventory.csv')
    i = None
    for index, row in df_inventory.iterrows():
        if (row['isbn'] == str(isbn)) & (row['stock'] > 0):
            return True
    return False

def addItem(isbn):
    username = getLoggedUser()
    df_cart = pd.read_csv('cart.csv')
    df_inventory = pd.read_csv('inventory.csv')
    for index, row in df_inventory.iterrows():
        if (row['isbn'] == str(isbn)):
            retailPrice = row['retailPrice']
    df_cart.loc[len(df_cart.index)] = [isbn, retailPrice, username]
    df_cart.to_csv('cart.csv', index=False)

def removeItem(isbn):
    username = getLoggedUser()
    df_cart = pd.read_csv('cart.csv')
    i = None
    for index, row in df_cart.iterrows():
        if (row['isbn'] == str(isbn)):
            i = index
    df_cart.drop(i, axis=0, inplace=True)
    df_cart.to_csv('cart.csv', index=False)

def totalPrice():
    username = getLoggedUser()
    df_cart = pd.read_csv('cart.csv')
    totalPrice = 0
    for index, row in df_cart.iterrows():
        totalPrice = totalPrice + row['retailPrice']
    return totalPrice

def checkout():
    username = getLoggedUser()
    df_cart = pd.read_csv('cart.csv')
    df_inventory = pd.read_csv('inventory.csv')
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
def newBook(isbn, title, genre, author, datePublished):
    df_books = pd.read_csv('books.csv')
    df_books.loc[len(df_books.index)] = [isbn, title, genre, author, datePublished]
    df_books.to_csv('books.csv', index=False)

def getBookTitle(isbn):
    df_books = pd.read_csv('books.csv')
    for index, row in df_books.iterrows():
        if row['isbn'] == str(isbn):
            print(row['title'])

def getBookGenre(isbn):
    df_books = pd.read_csv('books.csv')
    for index, row in df_books.iterrows():
        if row['isbn'] == str(isbn):
            print(row['genre'])

def getBookAuthor(isbn):
    df_books = pd.read_csv('books.csv')
    for index, row in df_books.iterrows():
        if row['isbn'] == str(isbn):
            print(row['author'])

def getBookDate(isbn):
    df_books = pd.read_csv('books.csv')
    for index, row in df_books.iterrows():
        if row['isbn'] == str(isbn):
            print(row['datePublished'])

def changeBookTitle(isbn, title):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "title"] = title
    df_books.to_csv('books.csv', index=False)

def changeBookGenre(isbn, genre):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "genre"] = genre
    df_books.to_csv('books.csv', index=False)

def changeBookAuthor(isbn, author):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "author"] = author
    df_books.to_csv('books.csv', index=False)

def changeBookDate(isbn, datePublished):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "datePublished"] = datePublished
    df_books.to_csv('books.csv', index=False)

def changeBookIsbn(isbn, newIsbn):
    df_books = pd.read_csv('books.csv')
    df_books.loc[df_books["isbn"] == str(isbn), "isbn"] = newIsbn
    df_books.to_csv('books.csv', index=False)