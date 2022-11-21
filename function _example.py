import pandas as pd

df = pd.read_csv('books.csv')

#newBook(isbn, title, genre, author, datePublished)
isbn = '9780451524935'
title = '1984'
genre = 'Fiction'
author = 'George Orwell'
datePublished = '01.01.1961'

df.loc[len(df.index)] = [isbn, title, genre, author, datePublished]

#getBookGenre(ISBN)
for index, row in df.iterrows():
    if row['isbn'] == isbn:
        print(row['genre'])

#setBookGenre(ISBN)
genre = 'Dystopian fiction'
for index, row in df.iterrows():
    if row['isbn'] == isbn:
        row['genre'] = genre

#getBookGenre(ISBN)
for index, row in df.iterrows():
    if row['isbn'] == isbn:
        print(row['genre'])