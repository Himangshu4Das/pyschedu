import logging
import heapq
from collections import namedtuple
from itertools import count
import threading
import time

__all__ = ["scheduler"]

# Define a custom log format
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Define a handler for writing logs to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter(LOG_FORMAT)
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)

Event = namedtuple('Event', 'time, priority, sequence, action, argument, kwargs')

_sentinel = object()

class scheduler:
    def __init__(self, timefunc=time.monotonic, delayfunc=time.sleep, enable_logging=False, log_file=None):
        """Initialize a new instance, passing the time and delay functions."""
        self._queue = []
        self._lock = threading.RLock()
        self.timefunc = timefunc
        self.delayfunc = delayfunc
        self._sequence_generator = count()
        self._event_finished = threading.Event()
        self._event_finished.set()
        self._event_ids = {}
        self.enable_logging = enable_logging
        self.log_file = log_file

        # If logging is enabled, configure logging to save logs to a file
        if self.enable_logging:
            if self.log_file:
                file_handler = logging.FileHandler(self.log_file)
                file_handler.setLevel(logging.DEBUG)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
            else:
                logger.warning("Log file path is not provided. Logs will only be printed to console.")

    def _thread_run(self):
        while not self.empty():
            self.run(blocking=True)

    def enterabs(self, time, priority, action, argument=(), kwargs=_sentinel):
        """Enter a new event in the queue at an absolute time.

        Returns an ID for the event which can be used to remove it,
        if necessary.

        """
        if kwargs is _sentinel:
            kwargs = {}

        with self._lock:
            event = Event(time, priority, next(self._sequence_generator),
                          action, argument, kwargs)
            heapq.heappush(self._queue, event)
            self._event_ids[id(event)] = len(self._queue) - 1
        return id(event)

    def enter(self, delay, priority, action, argument=(), kwargs=_sentinel):
        """A variant that specifies the time as a relative time."""
        time = self.timefunc() + delay
        return self.enterabs(time, priority, action, argument, kwargs)

    def cancel(self, event_id):
        """Remove an event from the queue."""
        with self._lock:
            if event_id not in self._event_ids:
                raise ValueError("Event ID not found")
            index = self._event_ids.pop(event_id)
            if index == len(self._queue) - 1:
                heapq.heappop(self._queue)
            else:
                self._queue[index] = self._queue[-1]
                self._queue.pop()
                self._event_ids[id(self._queue[index])] = index
                heapq._siftup(self._queue, index)
                heapq._siftdown(self._queue, 0, index)

    def empty(self):
        """Check whether the queue is empty."""
        with self._lock:
            return not self._queue

    def run(self, blocking=True):
        """Execute events until the queue is empty."""
        lock = self._lock
        q = self._queue
        delayfunc = self.delayfunc
        timefunc = self.timefunc
        pop = heapq.heappop

        with lock:
            if not q:
                if not blocking:
                    return None
                else:
                    return

            (time, priority, sequence, action,
             argument, kwargs) = q[0]
            now = timefunc()
            if time > now:
                delay = True
            else:
                delay = False
                pop(q)

        if delay:
            if not blocking:
                return time - now
            delayfunc(time - now)
        else:
            try:
                action(*argument, **kwargs)
            except Exception as e:
                if self.enable_logging:
                    logger.error(f"Exception occurred during event execution: {e}", exc_info=True)  # Log the exception
                delayfunc(0)
                return

            delayfunc(0)

        return None if not q else q[0][0] - timefunc()

    def start(self):
        """Start the scheduler in a separate thread."""
        self._event_finished.clear()
        threading.Thread(target=self._thread_run, daemon=True).start()

    def stop(self):
        """Stop the scheduler thread."""
        self._event_finished.set()

    @property
    def queue(self):
        """An ordered list of upcoming events."""
        with self._lock:
            events = self._queue[:]
        return list(map(heapq.heappop, [events] * len(events)))
    
    def reschedule(self, event_id, new_time):
        """Reschedule an event with the specified event ID to a new time."""
        with self._lock:
            if event_id not in self._event_ids:
                raise ValueError("Event ID not found")
            index = self._event_ids[event_id]
            event = self._queue[index]
            new_event = Event(new_time, event.priority, event.sequence,
                              event.action, event.argument, event.kwargs)
            self._queue[index] = new_event
            heapq._siftup(self._queue, index)  # Re-heapify the queue