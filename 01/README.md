[Open Solution in Google Colab](https://colab.research.google.com/github/ghostdart/Artificial-Intelligence-Labs/blob/main/01-Intro-to-python-and-jupyter/sol.ipynb)

![](media/image1.jpeg)

> Artificial Intelligence CS461 Laboratory Manual

# Course Instructor Lab Instructor(s) Section

> Semester Spring 2021

# FAST School of Computing Department of Software Engineering FAST-NU, Lahore, Pakistan.

> ![](media/image2.jpeg)**FAST NUCES, Lahore Campus** Faculty of
> Computer Sciences Lab Journal 01

### (Spring 2021)

<table>
<thead>
<tr class="header">
<th><blockquote>
<p>Course:</p>
</blockquote></th>
<th><blockquote>
<p>Artificial Intelligence</p>
</blockquote></th>
<th><blockquote>
<p>Date: 15-03-2021</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Course Code:</p>
</blockquote></td>
<td><blockquote>
<p>CS 461</p>
</blockquote></td>
<td><blockquote>
<p>Max Marks: 100</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Faculty’s Name:</p>
</blockquote></td>
<td><blockquote>
<p>Dr. Mubasher Baig</p>
</blockquote></td>
<td><blockquote>
<p>Lab Engineer: Saad Ali</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **Objective(s) :**
> 
> The Objectives of this lab are to understand the basics of Python ,
> Core components variables, control statements, loops, and functions.

### APPETIZERS: \[GETTING STARTED\]

> In this task you are required to use the online Jupyter notebook to
> learn the basic building blocks of Python by creating and executing
> simple Python scripts.

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>A 1.1</strong></p>
</blockquote></th>
<th><blockquote>
<p>Open the URL <strong>https://jupyter.org/try</strong> in your web browsers. You must reach the following webpage</p>
<p><img src="media/image3.jpeg" style="width:4.98765in;height:3.12125in" /></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>A 1.2:</strong></p>
</blockquote></td>
<td><blockquote>
<p>Click on the <strong>Try JupyterLab</strong> link: and an environment will be created for you on an online system. You will see the following page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><img src="media/image4.jpeg" style="width:4.73148in;height:2.81479in" /></p>
<p>In the <strong>Notebook</strong> section select the Python 3 option and you will reach the notebook editor page.</p>
<p><img src="media/image5.jpeg" style="width:4.82207in;height:2.47135in" /></p>
<p>Use Save As option in the File Menu to save it using your Registration no as the file name (Name Format: LXXYYYY.ipynb</p>
<p>A ipython notebook consists of multiple cells each having a python script/code that can be executed</p>
<p><img src="media/image6.jpeg" style="width:4.26139in;height:1.27219in" /></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>A 1.3</strong></p>
</blockquote></td>
<td><blockquote>
<p>Python has four primitive datatypes int, float, Boolean and string. We can use the print function to display messages on the output window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Variables and OUTPUT</strong></p>
</blockquote></td>
<td><blockquote>
<p>Following script creates four variables of the primitive types.</p>
<p>Enter the code in your notebooks as shown below and then run the code in each cell in order.</p>
<p><img src="media/image7.jpeg" style="width:5.48784in;height:5.16073in" /></p>
<p><strong>Note</strong></p>
<p>Python uses Tab/Space to indicate a block of statements and unlike C++ {} are not used. Read more about it online. You must be able to see how important the proper indentation is in this language.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>A 1.4</strong></p>
</blockquote></th>
<th><blockquote>
<p>Finally copy the following Python script and paste it in the last cell of your script. Try using</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>different values of the variable <strong>how_many_snakes</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>how_many_snakes = 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>snake_string = """</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Welcome to Python3!</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>/ . .\\</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>\ ---&lt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>\ /</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p><span class="underline"> </span> / /</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>-=: <span class="underline"> </span> /</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt;3, Python</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>"""</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>print(snake_string * how_many_snakes)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>WHAT OUTPUT IS PRODUCED By THE SCRIPT IN EACH CELL</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p><strong>Save your notebook and download it. Submit the script along with the output on the</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>classroom.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> **Raw Inputs**
> 
> .

![](media/image8.jpeg)

> **Python** provides the following operators

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Arithmetic operators:</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Operator</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Meaning</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>+, -, *, /</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Adding, subtracting, multiplying, and dividing two numeric values</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>**</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Exponentiation/power</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>//, %</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Integer Division and remainder</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>More Operators</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Comparison</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>==, !=, &lt;, &lt;=, &gt;, &gt;=</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Logical</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>and , or, not</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Bitwise</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>&amp;, |, ^, ~, &lt;&lt;, &gt;&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Basic Loops in Python

<table>
<thead>
<tr class="header">
<th><blockquote>
<p>A 3.1</p>
</blockquote></th>
<th><blockquote>
<p>Create the following scripts in your notebook run these scripts and submit the script along with the output on google classroom</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>for loop and while loop</strong></p>
</blockquote></td>
<td><blockquote>
<p><img src="media/image9.jpeg" style="width:5.21735in;height:3.55323in" /></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Creating Function:</strong> Create the following function and call it using the script given in the second cell. Submit the notebook along with the output on Google Classroom</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>A 3.1</strong></p>
</blockquote></td>
<td><blockquote>
<p><img src="media/image10.jpeg" style="width:4.47536in;height:3.36833in" /></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Program Writing

<table>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>P 1.1 [30]</strong></p>
</blockquote></th>
<th><blockquote>
<p>Exercise 1: Write a function that returns <strong>True</strong> if the numeric parameter is a palindrome and</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>False</strong> otherwise</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p><em>Input: x = 121 Output: true</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Exercise 2: Print the following pattern using for loop</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><ul>
<li><blockquote>
<p><em>5 4 3 2 1</em></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td><ul>
<li><blockquote>
<p><em>4 3 2 1</em></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td><ul>
<li><blockquote>
<p><em>3 2 1</em></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td><ul>
<li><blockquote>
<p><em>2 1</em></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td><ul>
<li><blockquote>
<p><em>1</em></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Exercise 3: Write a loop to find the factorial of any number</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><ul>
<li><blockquote>
<p><em>Input : 5</em></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td><ul>
<li><blockquote>
<p><em>5 x 4 x 3 x 2 x 1 = 120</em></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td><ul>
<li><blockquote>
<p><em>Output: 120</em></p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>P 1.2 [70]</strong></p>
</blockquote></td>
<td><blockquote>
<p>Exercise 1: Print First 10 natural numbers using while loop</p>
<p><em>Expected output:</em></p>
<p><em>0 1 2 3 4 5 6 7 8 9 10</em></p>
<p>Exercise 2: Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration</p>
<p><em>list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]</em></p>
<p><em>Expected output:</em></p>
<p><em>15</em></p>
<p><em>55</em></p>
<p><em>75</em></p>
<p><em>150</em></p>
<p>Exercise 3: Reverse the following list using for loop</p>
</blockquote>
<ul>
<li><blockquote>
<p><em>list1 = [10, 20, 30, 40, 50]</em></p>
</blockquote></li>
<li><blockquote>
<p><em>Expected Output = [50, 40, 30, 20, 10]</em></p>
</blockquote></li>
</ul>
<blockquote>
<p>Exercise 4: Write a program to display all prime numbers within a range</p>
<p><em>start = 25 end = 50 Expected Output:</em></p>
</blockquote>
<ul>
<li><blockquote>
<p><em>29</em></p>
</blockquote></li>
<li><blockquote>
<p><em>31</em></p>
</blockquote></li>
<li><blockquote>
<p><em>37</em></p>
</blockquote></li>
<li><blockquote>
<p><em>41</em></p>
</blockquote></li>
<li><blockquote>
<p><em>43</em></p>
</blockquote></li>
<li><blockquote>
<p><em>47</em></p>
</blockquote></li>
</ul>
<blockquote>
<p>Exercise 5: Reverse a given integer number</p>
</blockquote>
<ul>
<li><blockquote>
<p><em>Input : 53469</em></p>
</blockquote></li>
<li><blockquote>
<p><em>Output : 96435</em></p>
</blockquote></li>
</ul>
<blockquote>
<p>Exercise 6: Use a loop to display elements from a given list that are present at even index positions</p>
</blockquote>
<ul>
<li><blockquote>
<p><em>my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]</em></p>
</blockquote></li>
<li><blockquote>
<p><em>Output: 20, 40, 60, 80, 100</em></p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Submit your notebook along with the output on google classroom Use one cell per Exercise</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>
