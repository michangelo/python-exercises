# python-exercises

A small collection of python exercises

## gross_pay_calculator.py

Prompts the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.

## letter_grade.py

Program to prompt for a grade score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, prints a grade using the following table:

```txt
Score    Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6      F
```

## done_integer.py

program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

### Example Input

```
['7', '2', 'bob', '10', '4', 'done']
```

### Desired output

```
Invalid input
Maximum is 10
Minimum is 2
```

## find_and_string_slice.py

Uses find() and string slicing to extract the number at the end of the line below. Converts the extracted value to a floating point
number and prints it out.

## split_and_sort.py

Opens the file **romeo.txt** and reads it line by line. For each line, splits the line into a list of words using the **split()**
method. The program should build a list of words. For each word on each line, checks to see if the word is already in the list and if not, appends it to the list. When the program completes, sorts and prints the resulting words in python sort() order as shown in the desired output.

You can download the sample data at

[http://www.py4e.com/code3/romeo.txt](http://www.py4e.com/code3/romeo.txt)

### Example input

```python
['romeo.txt']
```

### Desired output

```txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
```

## email_dictionary.py

Program to read through the **mbox-short.txt** and figure
out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

### Example input

```python
['mbox-short.txt']
```

### Desired output

```txt
cwen@iupui.edu 5
```

## email_hour_day.py

Program to read through the **mbox-short.txt** and figure
out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

```txt
From stephen.marquard@uct.ac.za Sat Jan  5 **09**:14:16 2008
```

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

### Autograder input

```python
['mbox-short.txt']
```

### Desired output

```txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
```