#!/usr/bin/env python3
'''
function myFunction(param) {
  console.log("Running myFunction");
  return param + 1;
}
The function keyword identifies this code as a function.
myFunction is a variable name we can use to refer to the function from elsewhere in our code, written in camel 
case by convention.
The parentheses () after the function name give a space where we can define parameters for our function.
param is the variable name given to our function's parameter; it will be assigned a value when the function is 
invoked and passed an argument.
To define the body of the function, we use curly brackets ({ }).
console.log is a method that will output information to the terminal; remember, this is different from a function's 
return value.
The return keyword is needed when we want our function to return a value when it is called; in this case, 
it will return a value of whatever the param variable is plus one.

const myFunctionReturnValue = myFunction(1);
// => "Running myFunction"
console.log(myFunctionReturnValue);
// => 2

Here, we're calling the function myFunction with an argument of 1. We are then assigning the return value of 
myFunction to a new variable, myFunctionReturnValue.

If we wanted to write a method in Python with similar functionality, here's how it would look:

def my_function(param):
    print("Running my_function")
    return param + 1

# New code goes here!

There are a few key differences in the syntax here:

Use the def keyword to identify this code as a function.
Write the name of the method in snake case (by convention).
Parameters are still defined in parentheses, after the method name.
Instead of curly brackets, begin with a colon after the parentheses.

In Python, we must indent all code that is meant to be executed in my_function.

return statements in Python work very similarly to those in JavaScript, but no semicolon is needed after the return value.
Rather than closing with a curly bracket, any new code can be written at the original indentation level.


EXAMPLES:
JS:
function sayHi(name = "friend") {
  console.log(`Hi there, ${name}!`);
}

sayHi();
// => "Hi there, friend!"
sayHi("Sunny");
// => "Hi there, Sunny!"

PY:
def say_hi(name="Engineer"):
    print(f"Hi there, {name}!")

say_hi()
# => "Hi there, Engineer!"

say_hi("Sunny")
# => "Hi there, Sunny!"

There will be times when you're writing out your code and know that you will need a function later, but you don't 
quite know what to put in there yet. A good practice in Python development is to make use of the pass keyword in 
empty functions until they are ready to be fleshed out.

def my_future_function():
    pass

Because Python uses indentation to determine when a code block starts and ends, it is necessary to put something 
inside of an empty function- comments, sadly, do not count.

Python developers typically opt for pass over return None because it is a statement rather than an expression. 
It does not terminate the function like a return statement would do. You can even put code after your pass and it 
will be executed! A pass statement reminds you that there is work to be done without interfering with your 
development.
'''

def greet_programmer():
     print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

'''
 You should be able to call this function with two arguments and get back its return value:
  const result = halve(4);
  console.log(result);
  => 2

  If the function is called with an argument that isn't a number, it should return null:
  const result = halve("two")
  => null
  '''

def halve(number):
     #if typeof number !== "number":
        return number / 2
    #else:
     #return null
