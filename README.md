# python-threading
Python Threading and Thread Pool

# About
Simple decorators `threadpool` and `processpool` that makes use of the `ThreadPoolExecutor` and the `ProcessPoolExecutor` bounded by the number of concurrent workers with `BoundedThreadPoolExecutor` and `BoundedProcessPoolExecutor`:

```python
_DEFAULT_POOL = BoundedThreadPoolExecutor(max_workers=5)
_PROCESS_POOL = BoundedProcessPoolExecutor(max_workers=5)
```

# How to use
Import the `threadpool` decorator and apply to your high load task:
```python
from thread_support import threadpool

@threadpool
def my_high_load_task(self):
  res = do_job()
  return res
```

Call the function and the get the results with a synchronous call to `result()`

```python
task = my_high_load_task()
res = task.result()
```

To directly get the thread or process executors import the `BoundedThreadPoolExecutor` and call it specifing the `max_workers` parameters:

```python
from util.bounded_pool_executor import BoundedThreadPoolExecutor
thread_executor = BoundedThreadPoolExecutor(max_workers=5)
```

Do the same for the `BoundedProcessPoolExecutor`:

```python
from util.bounded_pool_executor import BoundedProcessPoolExecutor
process_executor = BoundedProcessPoolExecutor(max_workers=5)
```

# Disclaimer
Source code adapted from different sources.
