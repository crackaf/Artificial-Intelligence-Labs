![](images/media/image1.png)

Lab Manual 03

CL461-Artificial Intelligence Lab

<table>
<tbody>
<tr class="odd">
<td>Course Instructor</td>
<td>Dr. Aamir Wali</td>
</tr>
<tr class="even">
<td>Lab Instructor (s)</td>
<td><p>Mahmood Hussain</p>
<p>Maliha Arshad</p></td>
</tr>
<tr class="odd">
<td>Section</td>
<td>F</td>
</tr>
<tr class="even">
<td>Semester</td>
<td>Spring 2021</td>
</tr>
</tbody>
</table>

Department of Computer Science

FAST-NU, Lahore, Pakistan

# Table of Contents

[1 Objectives 2](#objectives)

[2 Task Distribution 3](#task-distribution)

[3 Python Sets 3](#python-sets)

[3.1 Set Initialization Examples 3](#set-initialization-examples)

[3.2 Set Modification Examples 4](#set-modification-examples)

[3.3 Set Operations 4](#set-operations)

[3.4 Frozensets 5](#frozensets)

[4 Python Exception Handling 6](#python-exception-handling)

[4.1 Types of Exceptions 6](#types-of-exceptions)

[4.2 Exception Handling with Try Except Clause
6](#exception-handling-with-try-except-clause)

[4.3 Re-raise the exception 7](#re-raise-the-exception)

[4.4 Catch certain types of exception
7](#catch-certain-types-of-exception)

[4.5 Try….Finally 8](#try.finally)

[4.6 Try..except and finally 8](#try..except-and-finally)

[5 Python File Handling 9](#python-file-handling)

[5.1 Open & Close a file 9](#open-close-a-file)

[5.2 Kinds of modes 9](#kinds-of-modes)

[5.3 Working of read() mode 9](#working-of-read-mode)

[5.4 Working of write() mode 10](#working-of-write-mode)

[5.5 Working of append() mode 10](#working-of-append-mode)

[6 Python Iterators 10](#python-iterators)

[6.1 Building Custom Iterators 11](#building-custom-iterators)

[7 Exercise (25 marks) 12](#exercise-25-marks)

[7.1 Set Operations (5 marks) 12](#set-operations-5-marks)

[7.2 Exception Handling for Division (5 marks)
12](#exception-handling-for-division-5-marks)

[7.3 Reading text from a file and storing it in reversed order (10
marks)
12](#reading-text-from-a-file-and-storing-it-in-reversed-order-10-marks)

[8 Submission Instructions 12](#submission-instructions)

# Objectives

After performing this lab, students shall be able to understand Python
data structures which include:

  - Python sets

  - Python exception handling

  - Python file handling

  - Python iterators

# Task Distribution

| **Total Time**            | **170 Minutes** |
| ------------------------- | --------------- |
| Python Sets               | 20 Minutes      |
| Python Exception Handling | 20 Minutes      |
| Python File Handling      | 20 Minutes      |
| Python Iterators          | 10 Minutes      |
| Exercise                  | 90 Minutes      |
| Online Submission         | 10 Minutes      |

# Python Sets

Sets have following characteristics:

  - Set in Python is a data structure equivalent to sets in mathematics.

  - Sets are a mutable collection of distinct (unique) immutable values
    that are unordered.

  - Any immutable data type can be an element of a set: a number, a
    string, a tuple.

  - Mutable (changeable) data types cannot be elements of the set.

  - In particular, list cannot be an element of a set (but tuple can),
    and another set cannot be an element of a set.

  - You can perform standard operations on sets (union, intersection,
    difference).

## Set Initialization Examples

You can initialize a set in the following ways:

\# Initialize empty set

emptySet = set()

\# Pass a list to set() to initialize it

dataScientist = set(\['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'\])

dataEngineer = set(\['Python', 'Java', 'Scala', 'Git', 'SQL',
'Hadoop'\])

\# Direct initialization using curly braces

dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}

dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}

\# Curly braces can only be used to initialize a set containing values

emptyDict= {}

## Set Modification Examples

Let’s consider the following set for our add/remove examples:

\# Initialize set with values

graphicDesigner = {'InDesign', 'Photoshop', 'Acrobat', 'Premiere',
'Bridge'}

\# Add a new immutable element to the set

graphicDesigner.add('Illustrator')

\# TypeError: unhasable type ‘list’

graphicDesigner.add(\['Powerpoint', 'Blender'\])

\# Remove an element from the set

graphicDesigner.remove('Illustrator')

\# Another way to remove an element. What is the difference?

graphicDesigner.discard('Premiere')

\# Remove and return an arbitrary value from a set

graphicDesigner.pop()

\# Remove al values from the set

graphicDesigner.clear()

## Set Operations

Python sets have methods that allow you to perform these mathematical
operations like union, intersection, difference, and symmetric
difference.

Let’s initialize two sets to work on our examples:

\# Initialize sets

dataScientist = set(\['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'\])

dataEngineer = set(\['Python', 'Java', 'Scala', 'Git', 'SQL',
'Hadoop'\])

\# set built-in function union

dataScientist.union(dataEngineer)

\# Equivalent Result

dataScientist | dataEngineer

\# Intersection operation

dataScientist.intersection(dataEngineer)

\# Equivalent Result

dataScientist & dataEngineer

\# These sets have elements in common so isdisjoint would return False

dataScientist.isdisjoint(dataEngineer)

\# Difference Operation

dataScientist.difference(dataEngineer)

\# Equivalent Result

dataScientist – dataEngineer

\# Symmetric Difference Operation

dataScientist.symmetric\_difference(dataEngineer)

\# Equivalent Result

dataScientist ^ dataEngineer

## Frozensets

You have encountered nested lists and tuples. The problem with nested
sets is that you cannot normally have nested sets as sets cannot contain
mutable values including sets.

  - A frozenset is very similar to a set except that a frozenset is
    immutable.

  - The primary reason to use them is to write clearer, functional code.

  - By defining a variable as a frozen set, you’re telling future
    readers: do not modify this.

  - If you want to use a frozen set you’ll have to use the function to
    construct it. No other way.

\# Nested Lists and Tuples

nestedLists = \[\['the', 12\], \['to', 11\], \['of', 9\], \['and', 7\],
\['that', 6\]\]

nestedTuples = (('the', 12), ('to', 11), ('of', 9), ('and', 7), ('that',
6))

\# Initialize a frozenset

immutableSet = frozenset()

\# Initialize a frozenset

nestedSets = set(\[frozenset()\])

A major disadvantage of a frozenset is that since they are immutable, it
means that you cannot add or remove values.

\# AttributeError: 'frozenset' object has no attribute 'add'

immutableSet.add("Strasbourg")

# Python Exception Handling

An exception is an error that is thrown by our code when the execution
of the code results in an unexpected outcome. Normally, an exception
will have an error type and an error message. Some examples are as
follows.

ZeroDivisionError: division by zero  
TypeError: must be str, not int

ZeroDivisionError and TypeError are the error type and the text that
comes after the colon is the error message. The error message usually
describes the error type.

## Types of Exceptions

Here’s a list of the common exceptions you’ll come across in Python:

1.  **ImportError**: It is raised when you try to import the library
    that is not installed or you have provided the wrong name

2.  **IndexError:** Raised when an index is not found in a sequence. For
    example, if the length of the list is 10 and you are trying to
    access the 11th index from that list, then you will get this error

3.  **IndentationError**: Raised when indentation is not specified
    properly

4.  **ZeroDivisionError**: It is raised when you try to divide a number
    by zero

5.  **ValueError**: Raised when the built-in function for a data type
    has the valid type of arguments, but the arguments have invalid
    values specified

6.  **Exception**: Base class for all exceptions. If you are not sure
    about which exception may occur, you can use the base class. It will
    handle all of them

## Exception Handling with Try Except Clause

Python provides us with the try except clause to handle exceptions that
might be raised by our code. The basic anatomy of the try except clause
is as follows:

try:  
// some code  
except:  
// what to do when the code in try raise an exception

In plain English, the try except clause is basically saying, “Try to do
this, except (otherwise) if there’s an error, then do this instead”.

There are a few options on what to do with the thrown exception from
the try block. Let’s discuss them.

## Re-raise the exception

Let’s take a look at how to write the try except statement to handle an
exception by re-raising it.

First, let’s define a function that takes two input arguments and
returns their sum.

def myfunction(a, b):  
return a + b

Next, let’s wrap it in a try except clause and pass input arguments with
the wrong type so the function will raise the TypeError exception.

try:  
myfunction(100, "one hundred")  
except:  
raiseTraceback (most recent call last):  
File "\<input\>", line 2, in \<module\>  
File "\<input\>", line 2, in myfunction  
TypeError: unsupported operand type(s) for +: 'int' and 'str'

## Catch certain types of exception

Another option is to define which exception types we want to catch
specifically. To do this, we need to add the exception type to
the except block.

try:  
myfunction(100, "one hundred")  
except TypeError:  
print("Cannot sum the variables. Please pass numbers only.")Cannot sum
the variables. Please pass numbers only.

To make it even better, we can actually log or print the exception
itself.

try:  
myfunction(100, "one hundred")  
except TypeError as e:  
print(f"Cannot sum the variables. The exception was: {e}")Cannot sum the
variables. The exception was: unsupported operand type(s) for +: 'int'
and 'str'

Furthermore, we can catch multiple exception types in one except clause
if we want to handle those exception types the same way. Let’s pass an
undefined variable to our function so that it will raise the NameError.
We will also modify our except block to catch
both TypeError and NameError and process either exception type the
same way.

try:  
myfunction(100, a)  
except (TypeError, NameError) as e:  
print(f"Cannot sum the variables. The exception was {e}")Cannot sum the
variables. The exception was name 'a' is not defined

## Try….Finally

So far the try statement had always been paired with except clauses. But
there is another way to use it as well. The try statement can be
followed by a **finally** clause. Finally clauses are called clean-up or
termination clauses, because they must be executed under all
circumstances, i.e. a "finally" clause is always executed regardless if
an exception occurred in a try block or not. A simple example to
demonstrate the finally clause:

**try**:

x = float(input("Your number: "))

inverse = 1.0 / x

**finally**:

print("There may or may not have been an exception.")

print("The inverse: ", inverse)

Your number: 34

There may or may not have been an exception.

The inverse: 0.029411764705882353

## Try..except and finally

"finally" and "except" can be used together for the same try block, as
it can be seen in the following Python example:

**try**:

x = float(input("Your number: "))

inverse = 1.0 / x

**except** **ValueError**:

print("You should have given either an int or a float")

**except** **ZeroDivisionError**:

print("Infinity")

**finally**:

print("There may or may not have been an exception.")

Your number: 23

There may or may not have been an exception.

# Python File Handling

Python allows users to handle files by supporting to read and write
files, along with many other file handling options. More details can be
learnt
[here](https://towardsdatascience.com/knowing-these-you-can-cover-99-of-file-operations-in-python-84725d82c2df)

## Open & Close a file

When you want to read or write a file, the first thing to do is to open
the file. Python has a built-in function **open** that opens the file
and returns a file object. To return a file object we use open()
function along with two arguments, that accepts file name and the mode,
whether to read or write.

The syntax is given below:

**open(filename, mode)**

## Kinds of modes

There are three basic types of modes in which files can be opened in
Python.

| **mode** | **meaning**                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------- |
| r        | open for reading (default)                                                                          |
| r+       | open for both reading and writing (file pointer is at the beginning of the file)                    |
| w        | open for writing (truncate the file if it exists)                                                   |
| w+       | open for both reading and writing (truncate the file if it exists)                                  |
| a        | open for writing (append to the end of the file if exists & file pointer is at the end of the file) |

Always keep in mind that the mode argument is not mandatory. If not
passed, then Python will assume it to be “** r **” by default.

Let’s look at this program and try to analyze how the read mode works:

\# a file named "book", will be opened with the reading mode.

file = open('book.txt', 'r')

\# This will print every line one by one in the file

for each in file:

print (each)

## Working of read() mode

There is more than one way to read a file in Python. If you need to
extract a string that contains all characters in the file then we can
use **file.read()**. The full code would work like this:

<table>
<tbody>
<tr class="odd">
<td><p># Python code to illustrate read() mode</p>
<p>file = open("file.text", "r")</p>
<p>print (file.read())</p></td>
</tr>
</tbody>
</table>

Another way to read a file is to call a certain number of characters
like in the following code the interpreter will read the first five
characters of stored data and return it as a string:

<table>
<tbody>
<tr class="odd">
<td><p># Python code to illustrate read() mode character wise</p>
<p>file = open("file.txt", "r")</p>
<p>print (file.read(5))</p>
<h2 id="working-of-write-mode">Working of write() mode</h2>
<p>Let’s see how to create a file and how write mode works:<br />
To manipulate the file, write the following in your Python environment:</p>
<table>
<tbody>
<tr class="odd">
<td><p># Python code to create a file</p>
<p>file = open('book.txt','w')</p>
<p>file.write("This is the write command")</p>
<p>file.write("It allows us to write in a particular file")</p>
<p>file.close()</p></td>
</tr>
</tbody>
</table>
<p>The close() command terminates all the resources in use and frees the system of this particular program.</p>
<h2 id="working-of-append-mode">Working of append() mode</h2>
<p># Python code to illustrate append() mode</p>
<p>file = open('book.txt','a')</p>
<p>file.write("This will add this line")</p>
<p>file.close()</p></td>
</tr>
</tbody>
</table>

# Python Iterators

An iterator is an object that contains a countable number of values. It
is an object that can be iterated upon, meaning that you can traverse
through all the values. Technically, in Python, an iterator is an object
which implements the iterator protocol, which consist of the
methods \_\_iter\_\_() and \_\_next\_\_().

Every time you ask an iterator for the **next **item, it calls
its \_\_next\_\_method. If there is another value available, the
iterator returns it. If not, it raises a StopIteration exception. More
information about iterators can be found [here](#python-iterators).

This behavior (only returning the next element when asked to) has two
main advantages:

1.  Iterators need less space in memory. They remember the last value
    and a rule to get to the next value instead of memorizing every
    single element of a (potentially very long) sequence.

2.  Iterators don’t check how long the sequence they produce might get.
    For instance, they don’t need to know how many lines a file has or
    how many files are in a folder to iterate through them.

(One important note: don’t confuse iterators with iterables. Iterables
are objects that can create iterators by using
their \_\_iter\_\_ method)

## Building Custom Iterators

Building an iterator from scratch is easy in Python. We just have to
implement the \_\_iter\_\_() and the \_\_next\_\_() methods.

The \_\_iter\_\_() method returns the iterator object itself. If
required, some initialization can be performed.

The \_\_next\_\_() method must return the next item in the sequence.

Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")

myit = iter(mytuple)

print(next(myit))

print(next(myit))

print(next(myit))

To iterate the characters of a string:

mystr = "banana"

for x in mystr:

print(x)

The for loop actually creates an iterator object and executes the next()
method for each loop.

# Exercise (25 marks)

## Set Operations (5 marks)

Consider two sets X and Y. You may take any type of values for these
sets. Try to find a solution to get a set having all elements in either
X or Y, but not both.

## Exception Handling for Division (5 marks)

Write a function to divide two numbers P and Q. Implement exception
handling technique (try..except clause) for handling possible exceptions
in the scenario.

## Reading text from a file and storing it in reversed order (10 marks)

Design a code which reads text from the file “Alphabets.txt” and stores
its data in reverse order in another file. For this you may upload the
given text file on Google Collab’s session and define the path as:

file\_path= ‘/Alphabets.txt’

The same convention can be followed for defining path of the resultant
file (reversed text file)

For more information read
[this](#reading-text-from-a-file-and-storing-it-in-reversed-order-10-marks).

# Submission Instructions

Always read the submission instructions carefully.

  - Rename your Jupyter notebook to your roll number and download the
    notebook as **.ipynb** extension.

  - To download the required file, go to **File-\>Download .ipynb**

  - Only submit the **.ipynb** file. DO NOT **zip** or **rar** your
    submission file

  - Submit this file on Google Classroom under the relevant assignment.

  - Late submissions will not be accepted
