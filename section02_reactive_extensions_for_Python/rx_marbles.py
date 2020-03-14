# Import key libraries, classes and functions
from rx import Observable
from rx.testing import marbles, TestScheduler

# Create a test scheduler
test_scheduler = TestScheduler()

# Function - print the observed values | To be subscribed to
def print_value(value):
    print('{} is the value'.format(value))

# Observable with time delay
# - means one unit in time
Observable.from_marbles('--(a1)-(b2)---(c3)', test_scheduler).subscribe(print_value)
Observable.from_marbles('(a6)---(b5)(c4)', test_scheduler).subscribe(print_value)

# Start the test scheduler
test_scheduler.start()
