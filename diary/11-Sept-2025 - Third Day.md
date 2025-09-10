# THIRD DAY(11-Sept-2025):

## Third Project (Scrapping web data with File csv)

[VIEW PROJECT](https://github.com/JonathanManzanoDiaz/experting-python/tree/b6c48fc32c7dc85d9d7cbdca8207d94a2e8a4a2d/0002-todo-list-with-txt)

```
Learned:
beautifulsoup4
http requests
```

This project it wasn't hard
The problem was with the open file of python

When I was making the requests i dont have any problem
First problem: When I created the file, I changed the name and was in "w" not in "a+" where the file is created if it's not exist, but the problem is in my code I was having another name
csv_quotes.csv and the file was csv-quotes.csv.
When I fixed this tiny problem
I need to write in the file the data.

Second problem: In this situation I was having another problem the encoding it was not specified, then I was seeing strange character, after reading documentation i find encoding="" and fixed it

Third Problem: I was having a problem because the data is only one line of the 10 lines I was scrapping, after realizing it, I used a for loop for fixed this problem

Fourth Problem: After the for loop is writed is working well but is typing in one line, that is a problem so i fixed with with writerow([texto, author]) and this is the final of the project
