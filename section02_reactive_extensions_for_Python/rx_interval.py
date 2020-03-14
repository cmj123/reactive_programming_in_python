# Import key libraries, classes and functions
from rx import Observable
from rx.testing import marbles, TestScheduler

# Create a test scheduler
test_scheduler = TestScheduler()

# Function - print the observed values | To be subscribed to
def print_value(value):
    print('{} is the value'.format(value))

# Observable - interval
Observable.interval(10, test_scheduler).take_until(Observable.timer(30)).subscribe(print_value)

# Start the test scheduler
test_scheduler.start()
