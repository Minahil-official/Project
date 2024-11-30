# STEPS FOR OOP_LLM_LAIBRARY

## 1ST STEP
## Atributes
### 1. created a **Student** name class
```python
class student:
```
### 2. give it artribute name
### 3 created an atribute self.score and assing an empty dictionary to it
```python
 def __init__(self,name):
        self.name = name
        self.score = {}
```
## Methods
### 4.created a function named add_score
### - add parameter like self,subject and score
### - assingning the value of score to the subject 
```python
def add_score(self,subject,score):
        self.score[subject] = score
```
### 5. created another function with name *calculate_average*
### - calculate the average by take of values in dictionary and dividing it to the length of dictionary
```python
 def calculate_average(self):
        return sum(self.score.values())/len(self.score)
```
### 6 created my third function with name **is_passing**
### then apply for loop then inside the loop i apply condition for passing the subject
```python
def is_passing(self):
        for sub,num in self.score.items():
            if num <40:
                return (f'fail in {sub}')
            return 'pass'
```
## 2ND STEP
## - i created another class name **Performance tracker**.
```python
class Performance_tracker:
```
### Atributes
### - i pass self.student and assing an empty dictionary to it.
```python
def __init__(self):
        self.student = {}
```

### Methods

### - i created a method named *Add_student()* and pass it parameters self and name and add a *condition* to it  for the correction
### of name which should ne Isalpha() after that i call my Student class to my self.student dictionary

```python
def add_student(self,name):
        if not name.isalpha():
            raise ValueError("please enter valid name")
        self.student[name] = student(name)
```
### - my next step is do add another method which is *calculate_class_average(self)* to which i pass self parameter then
### i apply a for loop to it before *for loop i also created* a variable to  which i assing 0
### then i call my uper student class function *calculate_average* to my variable so that i can calcukate the average of my class.
### by dividing the len of the dictionary's values to the variable which i created earlier
```python
def calculate_class_average(self):
    total = 0
    for x in self.student.values():
        total += x.calculate_average()
        return total/len(self.student.values())
```
### - then i move forward and created another function with name *display_student_performance(self)* which i pass self.
### in this function i apply *for loop* to my self.student.items() i passed tow parameters to the loop which are x and y
### then i make a variable with name Average and assing itmy uper class function calculate_average with y which is y.calculate_average(self)
### then i make another variable with name Status anf assing it my uper class function is_passing with y which is y.is_passing
### and print my average and status

```python
def display_student_performance(self):
        for x,y in self.student.items():
            average = y.calculate_average()
            status = y.is_passing()
            print(f"student: {x} average: {average} and pass_fail status: {status}")
```
## 3RD STEP 
### - in my third step i created object of my performace tracker class which i named *performance*
```python
performace = Performance_tracker()
```
### - after that i apply *while loop* to handle my errors by **error handling**
### in my while loop i ask the user to enter a name
```python
name = input("enter student name or type exit to finish:")
```
### - then i apply conditional statement to break the loop
```python
if name.lower() == "exit":
        break
```
### - then i handle my error  in **try block** i add my object to add_student function and add name to the parameters and then apply for loop
### to add a list of subjects
```python
 try:
    performace.add_student(name)
    for x in ['eng','math','urdu']:
```
### - after that i again apply *while loop* and i my loop again apply try block in this block i ask the user to add score of student for each subject
### which will be between 0 to 100
```python
try:
    score= float(input("enter student score for{x} 0 to 100:"))
```
### - then i apply conditional statement to check if the user add score greater the or equal to 0 or greater  or equal to 100 means correctly entered the 
### score then break the loop and if not for that i apply else block which ask the user to enter correct inpu
```python
if 0<= score <=100:
                performace.student[name].add_score(x,score)
                break
else:
    print("please enter valid input")
```
### - in the end i apply *except* block for both my try block in which one will catch value error and second one will catch exception
```python
except ValueError as e:
                    print(e)
    except Exception as e:
        print(e)
```
### - then i call my object with display function and print it
```python
performace.display_student_performance()
print(f"This is class average {performace.calculate_class_average()}")
```



