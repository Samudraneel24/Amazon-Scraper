from bs4 import BeautifulSoup
import requests
import csv

Name = []
URL = []
Author = []
Price = []
Avg_Rating = []
No_Rating = []

file = open('in_book.csv', 'w')
write = csv.writer(file)
arr = ['Name', 'URL', 'Author', 'Price', 'Average Rating','Number of Ratings']
write.writerow(arr)

link = 'https://www.amazon.in/gp/bestsellers/books/'
prefix = 'https://www.amazon.in'
temp = link
page = 1
while(page <= 5):
    response = requests.get(temp)
    content = BeautifulSoup(response.content, "html.parser")
    books = content.find_all(class_="zg_itemImmersion")
    for book in books:
        try:
            Name.append(
                book.find(class_="p13n-sc-truncate p13n-sc-line-clamp-1").get_text())
        except:
            Name.append("Not available")
        try:
            Author.append(book.find(class_="a-row a-size-small").get_text())
        except:
            Author.append("Not available")
        try:
            Price.append('Rs.' + book.find(class_="p13n-sc-price").get_text())
        except:
            Price.append("Not available")
        try:
            No_Rating.append(
                book.find(class_="a-size-small a-link-normal").get_text())
        except:
            No_Rating.append("Not available")
        try:
            URL.append(
                prefix + book.find(class_="a-link-normal a-text-normal")['href'])
        except:
            URL.append("Not available")
        try:
            temp = book.find(class_="a-icon-row a-spacing-none")
            try:
                Avg_Rating.append(temp.find(class_="a-icon-alt").get_text())
            except:
                Avg_Rating.append("Not available")
        except:
            Avg_Rating.append("Not available")
    page += 1
    temp = link + "ref=zg_bs_pg_" + str(page) + "?ie=UTF8&pg=" + str(page)
for i in range(100):
    arr = [Name[i], URL[i], Author[i], Price[i], Avg_Rating[i], No_Rating[i]]
    write.writerow(arr)
