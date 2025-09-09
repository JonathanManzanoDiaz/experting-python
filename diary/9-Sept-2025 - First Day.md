# FIRST DAY(09-Sept-2025):

### I'm learning python

I learned the basics of python for making the first project

## First Project (Password Generator)

[VIEW PROJECT](https://github.com/JonathanManzanoDiaz/experting-python/0001-password-generator)

```
Learned:
Strings → concatenación, join, slicing.
Loops and if's → for, while, if/else.
Basic Modules → random y string.
Functions → how to define and call functions (def).
```

Before I started the project:
I need to imagine what I need for start the project, so in my mind I think in this:
First: a variable with the generated password.

Second: Question the user how large want the password

Third: Generate a list with the specific data, at first I was thinking in making a list with the alphabet in minus and mayus and with some punctuation chars but after reading about strings in python I noticed that there is an existing list already and you can add the others one for making a better list
so I made listPassword with ascii letters, ascii digits and ascii punctuation

Fourth: I was thinking in making a random number with random.
Problem -> The number can't be more larger than the list length, so I made a variable where I add the length of the list generated

Fifth: After all that finished I was thinking in making a for in where the range is the password length where I asked the number to the user.

Inside the for in range, I added the generated number because after each loop the number is different so:
random char is generated with randrange, starting in 0 and finishing in number(the length of the list generated)
and the generated password is the random character generated with the password
generatedPassword + listPassword[random_char]

I printed the password and exit of the program.
