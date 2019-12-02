import collections

discounts = {2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}


def calculate_total(books):
    price = []
    if len(books) > 1:  # to separate solution with 0 or only 1 book in the order
        for i in range(5, 1, -1):  # checking solutions starting with the largest possible discount for package
            temp_list_of_books = books[:]
            pack = []
            temp_price = []
            while len(temp_list_of_books) > 0:  # to go through the whole order list
                founded = 1
                """ 
                checkpoint if the going through list of books resulted in the new 
                founding into the package
                """
                while len(pack) < i and len(temp_list_of_books) > 0 and founded > 0:
                    books_count = collections.Counter(temp_list_of_books)
                    founded = 0
                    for book in sorted(temp_list_of_books[:], key=books_count.get, reverse=True):
                        if book not in pack and len(pack) < i:
                            pack.append(book)
                            temp_list_of_books.remove(book)
                            founded += 1
                    if len(set(temp_list_of_books)) == 1:
                        """checkpoint if the rest of the books on the list create the package"""
                        temp_price.append(len(temp_list_of_books) * 800)
                        temp_list_of_books.clear()
                temp_price.append(len(pack) * 800 * discounts.get(len(pack), 1))
                pack = []
            price.append(int(sum(temp_price)))  # summary of prices + discount in every founded package
    else:
        price.append(int(len(books) * 800 * discounts.get(len(books), 1)))

    return min(price)
