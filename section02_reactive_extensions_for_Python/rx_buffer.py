# Import key libraries, classes and functions
from rx import Observable
from rx.testing import marbles, TestScheduler

# Function - print the observed values | To be subscribed to
def print_value(value):
    print('{} is the value'.format(value))

# Observable - buffer
print('-- Buffer')
Observable.from_(range(2000)).buffer(
    Observable.interval(1)).subscribe(
    lambda buffer: print('# of items in buffer: {}'.format(len(buffer)))
    )

print('-- Buffer with count')
Observable.from_(range(10)).buffer_with_count(3).subscribe(print_value)

print('-- Buffer with time')
test_scheduler = TestScheduler()
Observable.interval(10, test_scheduler).take_until(
    Observable.timer(30)).buffer_with_time(20).subscribe(print_value)

test_scheduler.start()
