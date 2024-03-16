# pyschedu

**pyschedu** is a Python package that provides a simple scheduler for executing functions at specified times or intervals.
It is inspired by the old sched package and is equiped with various features like multi-threading and locking support.

And yet again, feel free to use, experiment and contribute to make it better since I am a shitty engineer and would really appreciate your contributions.

## Usage

Import the `pyschedu` module and create an instance of the `scheduler` class to start scheduling events.

```python
from pyschedu import scheduler
import time

# Define functions to be executed
def function1():
    print("Function 1 executed")

def function2():
    print("Function 2 executed")

def function3():
    print("Function 3 executed")

# Create a scheduler instance
s = scheduler()

# Schedule events to execute the functions at different times with different priorities
event1_id = s.enter(1, 1, function1)
event2_id = s.enter(3, 2, function2)
event3_id = s.enter(5, 3, function3)

# Start the scheduler in a separate thread
s.start()

# Wait for scheduler to finish executing events
time.sleep(10)

# Stop the scheduler thread
s.stop()
```
## Features
- **Flexible Scheduling**: Schedule events to execute functions at absolute or relative times.
- **Priority Queue**: Prioritize events based on their priority.
- **Multi-threaded Execution**: Execute scheduled events concurrently in a separate thread.
- **Exception Handling**: Handle exceptions raised during event execution.
- **Logging**: Enable logging to track event execution and exceptions.
- **Non-blocking Execution**: Run the scheduler in non-blocking mode for concurrent tasks.

## Examples
Check out the examples for detailed usage scenarios.

## Contributing
Contributions are welcome! Please refer to the contribution guidelines for more details.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
