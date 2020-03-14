# Import key libraries, classes and functions
from rx import Observable

# Case 01 - Observe a List
# Function - print the observed values
def print_value(value):
    print('{} is the value'.format(value))

# Function - Create the observable and subscribe to the print value function
# Covert list to observable
# used the subscribe function to print the value
Observable.from_(['abc', 'def','ghi']).subscribe(print_value)

# Case 02 - Observe a callback
def say_hello(name, callback):
    callback('hello {}!'.format(name))

# Factor programming
# A factory is an object for creating other objects
hello = Observable.from_callback(say_hello) # a factory to create new observable
hello('Rudolf').subscribe(print_value) # actually creates an observable
hello('observable').subscribe(print_value) # creates an observalbe

# Case 03 - Observable from list
Observable.from_list([1,2,3]).subscribe(print_value)

# Case 04 - Observable from different objects in time
Observable.of(1,2,3,4,'A','B','C').subscribe(print_value)
