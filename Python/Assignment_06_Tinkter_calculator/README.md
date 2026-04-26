# ASSIGNMENT 6:
## Module 6: Calculator using TKinter
 
### Task 1: Create a Dictionary of Student Marks

#### Problem Statement: Write a Python code using TKinter to develop a calculator. :


#### Solution :   
&nbsp;&nbsp;&nbsp;&nbsp; The frontend code is available in `UI.py` file.  
&nbsp;&nbsp;&nbsp;&nbsp;  The backend code is available in `calculator_main.py` file.

#### Thought Process: 
Recently I have been studying about dunder functions in Python and wanted
to implement something similar in my day-to-day Python activities.  
So in order to achieve that I have developed a frontend and a 
backend kind of setup in the code. The main file is ui.py, which hosts the UI part of the code. 
In UI.py you will mostly find all the concepts related to how to use TKinter 
and how to design your visual aspects, how buttons are ordered, 
basically just the touch point for the end users.
The main backend calculations are hosted in Calculator_main.py. Since I wanted to leverage the 
built-in functions and the eval methodology, I have mostly 
played with how to handle calculations using only strings.  
In the essence of code it is a very simple way that I have kept it all together:
1. Expression initialization, where expression is initialized
2. Append function that mostly just appends the buttons that you will be clicking
3. Error handling methodology, where it just checks if there is any error that is potentially problem-causing and is handled
4. Finally the eval function, where instead of using the built-in directly, it tries to execute the string expression as it is and generate the results for it



# Solution can be viewed at github [link](https://github.com/akki6843/TuteDude/tree/master/Python/Assignment_05_%20Data%20Structures%20and%20Strings%20in%20Python)