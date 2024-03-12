from pyschedu import scheduler
import time

# Define functions to be executed
def function1():
    print("Function 1 executed")

def function2():
    print("Function 2 executed")

def function3():
    print("Function 3 executed")

# Define a function that raises an exception
def raise_exception():
    raise ValueError("This is a test exception")
    
# Section: Example 1 - Basic Usage with Cancelling an Event

# Create a scheduler instance
s = scheduler()

# Schedule events to execute the functions at different times with different priorities
event1_id = s.enter(1, 1, function1)
event2_id = s.enter(3, 2, function2)
event3_id = s.enter(5, 3, function3)

# Cancel event 2
s.cancel(event2_id)

# Start the scheduler in a separate thread
s.start()

# Wait for scheduler to finish executing events
time.sleep(10)

# Stop the scheduler thread
s.stop()

# Section: Example 2 - Additional Scheduling after Cancelled Events

# Schedule additional events after cancelling event 2
s.enter(1, 1, function1)
s.enter(3, 2, function2)
s.enter(5, 3, function3)

# Start the scheduler in a separate thread
s.start()

# Wait for scheduler to finish executing events (blocking execution)
time.sleep(10)

# Stop the scheduler thread
s.stop()

# Section: Example 3 - Non-blocking Execution with Run Method

# Create a scheduler instance for non-blocking execution
s_non_blocking = scheduler()

# Schedule events for non-blocking execution
s_non_blocking.enter(1, 1, function1)
s_non_blocking.enter(3, 2, function2)
s_non_blocking.enter(5, 3, function3)

# Start the scheduler in a separate thread
s_non_blocking.start()

# Run scheduler in non-blocking mode and perform other tasks concurrently
while True:
    next_deadline = s_non_blocking.run(blocking=False)
    if next_deadline is None:
        print("No pending events. Performing other tasks.")
        break
    else:
        print(f"Next event scheduled at {next_deadline} seconds.")
        time.sleep(1)  # Simulate other tasks

# Stop the scheduler thread
s_non_blocking.stop()

# Section: Example 4 - Handling Exceptions in Scheduled Functions

# Create a scheduler instance
s = scheduler()

# Schedule an event with the function that raises an exception
event_id = s.enter(1, 1, raise_exception)

# Start the scheduler in a separate thread
s.start()

# Wait for scheduler to finish executing events
time.sleep(5)

# Stop the scheduler thread
s.stop()

# Section: Example 5 - Handling Exceptions in Scheduled Functions with Logging

# Define a function that raises an exception
def raise_exception():
    raise ValueError("This is a test exception")

# Create a scheduler instance with logging enabled
s = scheduler(enable_logging=True, log_file="scheduler.log")

# Schedule an event with the function that raises an exception to log
event_id = s.enter(1, 1, raise_exception)

# Start the scheduler in a separate thread
s.start()

# Wait for scheduler to finish executing events
time.sleep(5)

# Stop the scheduler thread
s.stop()
