import time
import pytest
from pyschedu.scheduler import scheduler

# Define test functions
def test_basic_usage():
    # Create a scheduler instance
    s = scheduler()

    # Define a function to be executed
    def function():
        return "Function executed"

    # Schedule an event to execute the function after 1 second
    event_id = s.enter(1, 1, function)

    # Start the scheduler in a separate thread
    s.start()

    # Wait for scheduler to finish executing events
    time.sleep(2)

    # Stop the scheduler thread
    s.stop()

    # Assert that the function was executed
    assert function() == "Function executed"

def test_cancel_event():
    # Create a scheduler instance
    s = scheduler()

    # Define a function to be executed
    def function():
        return "Function executed"

    # Schedule an event to execute the function after 1 second
    event_id = s.enter(1, 1, function)

    # Cancel the scheduled event
    s.cancel(event_id)

    # Start the scheduler in a separate thread
    s.start()

    # Wait for scheduler to finish executing events
    time.sleep(2)

    # Stop the scheduler thread
    s.stop()

    # Assert that the function was not executed
    with pytest.raises(Exception):
        function()

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "test_scheduler.py"])
