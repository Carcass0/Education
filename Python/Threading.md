**_class_ threading.Thread(_group=None_, _target=None_, _name=None_, _args=()_, _kwargs={}_, _*_, _daemon=None_)**

This constructor should always be called with keyword arguments. Arguments are:

_group_ should be `None`; reserved for future extension when a `ThreadGroup` class is implemented.

_target_ is the callable object to be invoked by the `run()` method. Defaults to `None`, meaning nothing is called.

_name_ is the thread name. By default, a unique name is constructed of the form “Thread-_N_” where _N_ is a small decimal number, or “Thread-_N_ (target)” where “target” is `target.__name__` if the _target_ argument is specified.

_args_ is a list or tuple of arguments for the target invocation. Defaults to `()`.

_kwargs_ is a dictionary of keyword arguments for the target invocation. Defaults to `{}`.

If not `None`, _daemon_ explicitly sets whether the thread is daemonic. If `None` (the default), the daemonic property is inherited from the current thread.

There’s a way to start up a group of threads. It’s called a `ThreadPoolExecutor`, and it’s part of the standard library in [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html).

The easiest way to create it is as a context manager, using the [`with` statement](https://realpython.com/python-with-statement/) to manage the creation and destruction of the pool.

The end of the `with` block causes the `ThreadPoolExecutor` to do a `.join()` on each of the threads in the pool. It is _strongly_ recommended that you use `ThreadPoolExecutor` as a context manager when you can so that you never forget to `.join()` the threads.

```python
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
```
**_class_ concurrent.futures.Executor**
An abstract class that provides methods to execute calls asynchronously. It should not be used directly, but through its concrete subclasses.

**submit(_fn_, _/_, _*args_, _kwargs_)**

Schedules the callable, _fn_, to be executed as `fn(*args, **kwargs)` and returns a [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") object representing the execution of the callable.

**map(_fn_, _*iterables_, _timeout=None_, _chunksize=1_)**

Similar to [`map(fn, *iterables)`](https://docs.python.org/3/library/functions.html#map "map") except:

- the _iterables_ are collected immediately rather than lazily;
    
- _fn_ is executed asynchronously and several calls to _fn_ may be made concurrently.
    

The returned iterator raises a [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError") if [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") is called and the result isn’t available after _timeout_ seconds from the original call to [`Executor.map()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map "concurrent.futures.Executor.map"). _timeout_ can be an int or a float. If _timeout_ is not specified or `None`, there is no limit to the wait time.

If a _fn_ call raises an exception, then that exception will be raised when its value is retrieved from the iterator.

When using [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor"), this method chops _iterables_ into a number of chunks which it submits to the pool as separate tasks. The (approximate) size of these chunks can be specified by setting _chunksize_ to a positive integer. For very long iterables, using a large value for _chunksize_ can significantly improve performance compared to the default size of 1. With [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor"), _chunksize_ has no effect.

A **`Lock`** is an object that acts like a hall pass. Only one thread at a time can have the `Lock`. Any other thread that wants the `Lock` must wait until the owner of the `Lock` gives it up.

The basic functions to do this are `.acquire()` and `.release()`. A thread will call `my_lock.acquire()` to get the lock. If the lock is already held, the calling thread will wait until it is released. There’s an important point here. If one thread gets the lock but never gives it back, your program will be stuck. 

Fortunately, Python’s `Lock` will also operate as a context manager, so you can use it in a `with` statement, and it gets released automatically when the `with` block exits for any reason.

Python threading has a second object, called `RLock`, that is designed for just this situation. It allows a thread to `.acquire()` an `RLock` multiple times before it calls `.release()`. That thread is still required to call `.release()` the same number of times it called `.acquire()`, but it should be doing that anyway.

`threading.Semaphore`. A `Semaphore` is a counter with a few special properties. The first one is that the counting is atomic. This means that there is a guarantee that the operating system will not swap out the thread in the middle of incrementing or decrementing the counter.

The internal counter is incremented when you call `.release()` and decremented when you call `.acquire()`.

The next special property is that if a thread calls `.acquire()` when the counter is zero, that thread will block until a different thread calls `.release()` and increments the counter to one.

Semaphores are frequently used to protect a resource that has a limited capacity. An example would be if you have a pool of connections and want to limit the size of that pool to a specific number.

A `threading.Timer` is a way to schedule a function to be called after a certain amount of time has passed. You create a `Timer` by passing in a number of seconds to wait and a function to call.

You start the `Timer` by calling `.start()`. The function will be called on a new thread at some point after the specified time, but be aware that there is no promise that it will be called exactly at the time you want.

If you want to stop a `Timer` that you’ve already started, you can cancel it by calling `.cancel()`. Calling `.cancel()` after the `Timer` has triggered does nothing and does not produce an exception.

A `Timer` can be used to prompt a user for action after a specific amount of time. If the user does the action before the `Timer` expires, `.cancel()` can be called.

A `threading.Barrier` can be used to keep a fixed number of threads in sync. When creating a `Barrier`, the caller must specify how many threads will be synchronizing on it. Each thread calls `.wait()` on the `Barrier`. They all will remain blocked until the specified number of threads are waiting, and then the are all released at the same time.

Remember that threads are scheduled by the operating system so, even though all of the threads are released simultaneously, they will be scheduled to run one at a time.

One use for a `Barrier` is to allow a pool of threads to initialize themselves. Having the threads wait on a `Barrier` after they are initialized will ensure that none of the threads start running before all of the threads are finished with their initialization.