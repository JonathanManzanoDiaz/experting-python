# SECOND DAY(10-Sept-2025):

I learned the basics of python for making the first project

## Second Project (Todo List with File TxT)

[VIEW PROJECT](https://github.com/JonathanManzanoDiaz/experting-python/tree/461508b5fc0b676ec97f3378f67600961d10bd39/0001-password-generator)

```
Learned:
input/output in files → open("file.txt", "a"), readlines().
lists → save tasks in memory
```

This app is more heavy than the first for me.

I need to think in how I will execute this task
First:
Create the file txt and open it in python

First I was searching for how to open the file.
I find this open() with python, (r+ for reading and writing but if the file you open doesn't exit, it doesnt work, so i changed to open("tasks.txt, "a+")

I work with functions here, but first I did it all without any function.

First: the function i made is read task where you can read all the task

Second function is write tasks, for to show the user the task, when i dont use the function the coede is very large and repeatble, so i make a function with this task

third and last function input ask int because i have problems if you dont use the right number for the update task, so I used another function for this.

The first option is very easy for me, the problem is in the second one because I doesnt work when i delete the task, the problem was i wasn't using correctly open() because when you change some variable or delete a task of an list if you dont update your memory to file, it doesn't work.
You need to truncate your file, and add update your memory in to your file
I wasn't understanding this, so I was in this project like for 1 or 2 hours more than I planned.

The third one, is wasn't that hard because I know where the problem was with the option 2

I only need to reuse the options for delete but update the content

And the last one...
THe most easy, option 0, and exit,
after that I close tasks_file and all good
I dont know if I have more errors, but probably i have, but I will continue with more projects before update this to do list
