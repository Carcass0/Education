**_class_ multiprocessing.Process(_group=None_, _target=None_, _name=None_, _args=()_, _kwargs={}_, _*_, _daemon=None_)**

Process objects represent activity that is run in a separate process. The `Process` class has equivalents of all the methods of [[Threading | threading.Thread]].

The constructor should always be called with keyword arguments. _group_ should always be `None`; it exists solely for compatibility with [[Threading | threading.Thread]]. _target_ is the callable object to be invoked by the `run()` method. It defaults to `None`, meaning nothing is called. _name_ is the process name. _args_ is the argument tuple for the target invocation. _kwargs_ is a dictionary of keyword arguments for the target invocation. If provided, the keyword-only _daemon_ argument sets the process `daemon` flag to `True` or `False`. If `None` (the default), this flag will be inherited from the creating process.

By default, no arguments are passed to _target_. The _args_ argument, which defaults to `()`, can be used to specify a list or tuple of the arguments to pass to _target_.

If a subclass overrides the constructor, it must make sure it invokes the base class constructor (`Process.__init__()`) before doing anything else to the process.

**run()**

Method representing the process’s activity.

You may override this method in a subclass. The standard `run()` method invokes the callable object passed to the object’s constructor as the target argument, if any, with sequential and keyword arguments taken from the _args_ and _kwargs_ arguments, respectively.

Using a list or tuple as the _args_ argument passed to `Process` achieves the same effect.

**start()**

Start the process’s activity.

This must be called at most once per process object. It arranges for the object’s `run()` method to be invoked in a separate process.

join([_timeout_])

If the optional argument _timeout_ is `None` (the default), the method blocks until the process whose `join()` method is called terminates. If _timeout_ is a positive number, it blocks at most _timeout_ seconds. Note that the method returns `None` if its process terminates or if the method times out. Check the process’s `exitcode` to determine if it terminated.

A process can be joined many times.

A process cannot join itself because this would cause a deadlock. It is an error to attempt to join a process before it has been started.

**Shared memory**

Data can be stored in a shared memory map using `Value` or `Array`.

**multiprocessing.Value(_typecode_or_type_, _*args_, _lock=True_)**

Return a `ctypes` object allocated from shared memory. By default the return value is actually a synchronized wrapper for the object. The object itself can be accessed via the _value_ attribute of a `Value`.

_typecode_or_type_ determines the type of the returned object: it is either a ctypes type or a one character typecode of the kind used by the `array` module. _*args_ is passed on to the constructor for the type.

If _lock_ is `True` (the default) then a new recursive lock object is created to synchronize access to the value. If _lock_ is a `Lock` or `RLock` object then that will be used to synchronize access to the value. If _lock_ is `False` then access to the returned object will not be automatically protected by a lock, so it will not necessarily be “process-safe”

Operations like `+=` which involve a read and write are not atomic. So if, for instance, you want to atomically increment a shared value it is insufficient to just do

```python
counter.value += 1
```

Assuming the associated lock is recursive (which it is by default) you can instead do

```python
with counter.get_lock():
    counter.value += 1
```
Note that _lock_ is a keyword-only argument.

**multiprocessing.Array(_typecode_or_type_, _size_or_initializer_, _*_, _lock=True_)**

Return a ctypes array allocated from shared memory. By default the return value is actually a synchronized wrapper for the array.

_typecode_or_type_ determines the type of the elements of the returned array: it is either a ctypes type or a one character typecode of the kind used by the `array` module. If _size_or_initializer_ is an integer, then it determines the length of the array, and the array will be initially zeroed. Otherwise, _size_or_initializer_ is a sequence which is used to initialize the array and whose length determines the length of the array.

If _lock_ is `True` (the default) then a new lock object is created to synchronize access to the value. If _lock_ is a `Lock` or `RLock` object then that will be used to synchronize access to the value. If _lock_ is `False` then access to the returned object will not be automatically protected by a lock, so it will not necessarily be “process-safe”.

Note that _lock_ is a keyword only argument.

Note that an array of `ctypes.c_char` has _value_ and _raw_ attributes which allow one to use it to store and retrieve strings.

## Server process
Whenever a python program starts, a **server process** is also started. From there on, whenever a new process is needed, the parent process connects to the server and requests it to fork a new process.  
A **server process** can hold Python objects and allows other processes to manipulate them using proxies.  
**multiprocessing** module provides a **Manager** class which controls a server process. Hence, managers provide a way to create data that can be shared between different processes.

**multiprocessing.Manager()**

Returns a started `SyncManager` object which can be used for sharing objects between processes. The returned manager object corresponds to a spawned child process and has methods which will create shared objects and return corresponding proxies.

Manager processes will be shutdown as soon as they are garbage collected or their parent process exits. The manager classes are defined in the `multiprocessing.managers` module:

**_class_ multiprocessing.managers.BaseManager(_address=None_, _authkey=None_, _serializer='pickle'_, _ctx=None_, _*_, _shutdown_timeout=1.0_)]**

Create a BaseManager object.

Once created one should call `start()` or `get_server().serve_forever()` to ensure that the manager object refers to a started manager process.

_address_ is the address on which the manager process listens for new connections. If _address_ is `None` then an arbitrary one is chosen.

_authkey_ is the authentication key which will be used to check the validity of incoming connections to the server process. If _authkey_ is `None` then `current_process().authkey` is used. Otherwise _authkey_ is used and it must be a byte string.

_serializer_ must be `'pickle'` (use `pickle` serialization) or `'xmlrpclib'` (use `xmlrpc.client` serialization).

_ctx_ is a context object, or `None` (use the current context). See the `get_context()` function.

_shutdown_timeout_ is a timeout in seconds used to wait until the process used by the manager completes in the `shutdown()` method. If the shutdown times out, the process is terminated. If terminating the process also times out, the process is killed.

**start([_initializer_[, _initargs_]])**
Start a subprocess to start the manager. If _initializer_ is not `None` then the subprocess will call `initializer(*initargs)` when it starts.

**get_server()**

Returns a `Server` object which represents the actual server under the control of the Manager. The `Server` object supports the `serve_forever()` method:

```python
 from multiprocessing.managers import BaseManager
 manager = BaseManager(address=('', 50000), authkey=b'abc')
 server = manager.get_server()
 server.serve_forever()
```

`Server` additionally has an `address` attribute.

**connect()**

Connect a local manager object to a remote manager process:

```python
from multiprocessing.managers import BaseManager
m = BaseManager(address=('127.0.0.1', 50000), authkey=b'abc')
m.connect()
```

**shutdown()**

Stop the process used by the manager. This is only available if `start()` has been used to start the server process.

This can be called multiple times.

**register(_typeid_[, _callable_[, _proxytype_[, _exposed_[, _method_to_typeid_[, _create_method_]]]]])**
A classmethod which can be used for registering a type or callable with the manager class.

_typeid_ is a “type identifier” which is used to identify a particular type of shared object. This must be a string.

_callable_ is a callable used for creating objects for this type identifier. If a manager instance will be connected to the server using the `connect()` method, or if the _create_method_ argument is `False` then this can be left as `None`.

_proxytype_ is a subclass of `BaseProxy` which is used to create proxies for shared objects with this _typeid_. If `None` then a proxy class is created automatically.

_exposed_ is used to specify a sequence of method names which proxies for this typeid should be allowed to access using `BaseProxy._callmethod()`. (If _exposed_ is `None` then `proxytype._exposed_` is used instead if it exists.) In the case where no exposed list is specified, all “public methods” of the shared object will be accessible. (Here a “public method” means any attribute which has a `__call__()` method and whose name does not begin with `'_'`.)

_method_to_typeid_ is a mapping used to specify the return type of those exposed methods which should return a proxy. It maps method names to typeid strings. (If _method_to_typeid_ is `None` then `proxytype._method_to_typeid_` is used instead if it exists.) If a method’s name is not a key of this mapping or if the mapping is `None` then the object returned by the method will be copied by value.

_create_method_ determines whether a method should be created with name _typeid_ which can be used to tell the server process to create a new shared object and return a proxy for it. By default it is `True`.

`BaseManager` instances also have one read-only property:

**address**

The address used by the manager.

Manager objects support the context management protocol – see Context Manager Types. `__enter__()` starts the server process (if it has not already started) and then returns the manager object. `__exit__()` calls `shutdown()`.

**_class_ multiprocessing.managers.SyncManager**

A subclass of `BaseManager` which can be used for the synchronization of processes. Objects of this type are returned by `multiprocessing.Manager()`.

Its methods create and return Proxy Objects for a number of commonly used data types to be synchronized across processes. This notably includes shared lists and dictionaries.

**Barrier(_parties_[, _action_[, _timeout_]])**

Create a shared [[Threading | threading.Barrier]] object and return a proxy for it.

**BoundedSemaphore([_value_])**

Create a shared [[Threading | threading.BoundedSemaphore]] object and return a proxy for it.

**Condition([_lock_])**
Create a shared [[Threading | threading.Condition]] object and return a proxy for it.

If _lock_ is supplied then it should be a proxy for a [[Threading | threading.Lock]] or [[Threading | threading.RLock]] object

**Event()**

Create a shared [[Threading | threading.Event]] object and return a proxy for it.

**Lock()**

Create a shared [[Threading | threading.Lock]] object and return a proxy for it.

**Namespace()**

Create a shared `Namespace` object and return a proxy for it.

**Queue([_maxsize_])**

Create a shared `queue.Queue` object and return a proxy for it.

**RLock()**

Create a shared [[Threading | threading.RLock]] object and return a proxy for it.

**Semaphore([_value_])**

Create a shared [[Threading | threading.Semaphore]] object and return a proxy for it.

**Array(_typecode_, _sequence_)**

Create an array and return a proxy for it.

**Value(_typecode_, _value_)**

Create an object with a writable `value` attribute and return a proxy for it.

**dict()**

**dict(_mapping_)**

**dict(_sequence_)**

Create a shared `dict` object and return a proxy for it.

**list()**
**list(_sequence_)**

Create a shared `list` object and return a proxy for it.

Shared objects are capable of being nested. For example, a shared container object such as a shared list can contain other shared objects which will all be managed and synchronized by the `SyncManager`.

**_class_ multiprocessing.managers.Namespace**

A type that can register with `SyncManager`.

A namespace object has no public methods, but does have writable attributes. Its representation shows the values of its attributes.

However, when using a proxy for a namespace object, an attribute beginning with `'_'` will be an attribute of the proxy and not an attribute of the referent:

```python
mp_context = multiprocessing.get_context('spawn')
manager = mp_context.Manager()
Global = manager.Namespace()
Global.x = 10
Global.y = 'hello'
Global._z = 12.3    # this is an attribute of the proxy
print(Global)
Namespace(x=10, y='hello')
```

### Pipes and Queues

When using multiple processes, one generally uses message passing for communication between processes and avoids having to use any synchronization primitives like locks.

For passing messages one can use `Pipe()` (for a connection between two processes) or a queue (which allows multiple producers and consumers).

The `Queue`, `SimpleQueue` and `JoinableQueue` types are multi-producer, multi-consumer FIFO queues modelled on the `queue.Queue` class in the standard library.

multiprocessing.Pipe([_duplex_])

Returns a pair `(conn1, conn2)` of `Connection` objects representing the ends of a pipe.

If _duplex_ is `True` (the default) then the pipe is bidirectional. If _duplex_ is `False` then the pipe is unidirectional: `conn1` can only be used for receiving messages and `conn2` can only be used for sending messages.

**_class_ multiprocessing.pool.Pool([_processes_[, _initializer_[, _initargs_[, _maxtasksperchild_[, _context_]]]]])**

A process pool object which controls a pool of worker processes to which jobs can be submitted. It supports asynchronous results with timeouts and callbacks and has a parallel map implementation.

_processes_ is the number of worker processes to use. If _processes_ is `None` then the number returned by `os.cpu_count()` is used.

If _initializer_ is not `None` then each worker process will call `initializer(*initargs)` when it starts.

_maxtasksperchild_ is the number of tasks a worker process can complete before it will exit and be replaced with a fresh worker process, to enable unused resources to be freed. The default _maxtasksperchild_ is `None`, which means worker processes will live as long as the pool.

_context_ can be used to specify the context used for starting the worker processes. Usually a pool is created using the function `multiprocessing.Pool()` or the `Pool()` method of a context object. In both cases _context_ is set appropriately.

Note that the methods of the pool object should only be called by the process which created the pool.

**apply(_func_[, _args_[, _kwds_]]**

Call _func_ with arguments _args_ and keyword arguments _kwds_. It blocks until the result is ready. Given this blocks, `apply_async()` is better suited for performing work in parallel. Additionally, _func_ is only executed in one of the workers of the pool.

**apply_async(_func_[, _args_[, _kwds_[, _callback_[, _error_callback_]]]])**

A variant of the `apply()` method which returns a `AsyncResult` object.

If _callback_ is specified then it should be a callable which accepts a single argument. When the result becomes ready _callback_ is applied to it, that is unless the call failed, in which case the _error_callback_ is applied instead.

If _error_callback_ is specified then it should be a callable which accepts a single argument. If the target function fails, then the _error_callback_ is called with the exception instance.

Callbacks should complete immediately since otherwise the thread which handles the results will get blocked.

**map(_func_, _iterable_[, _chunksize_])**

A parallel equivalent of the `map()` built-in function (it supports only one _iterable_ argument though, for multiple iterables see `starmap()`). It blocks until the result is ready.

This method chops the iterable into a number of chunks which it submits to the process pool as separate tasks. The (approximate) size of these chunks can be specified by setting _chunksize_ to a positive integer.

Note that it may cause high memory usage for very long iterables. Consider using `imap()` or `imap_unordered()` with explicit _chunksize_ option for better efficiency.

map_async(_func_, _iterable_[, _chunksize_[, _callback_[, _error_callback_]]])

A variant of the `map()` method which returns a `AsyncResult` object.

If _callback_ is specified then it should be a callable which accepts a single argument. When the result becomes ready _callback_ is applied to it, that is unless the call failed, in which case the _error_callback_ is applied instead.

If _error_callback_ is specified then it should be a callable which accepts a single argument. If the target function fails, then the _error_callback_ is called with the exception instance.

Callbacks should complete immediately since otherwise the thread which handles the results will get blocked.

**imap(_func_, _iterable_[, _chunksize_])**

A lazier version of `map()`.

The _chunksize_ argument is the same as the one used by the `map()` method. For very long iterables using a large value for _chunksize_ can make the job complete **much** faster than using the default value of `1`.

Also if _chunksize_ is `1` then the `next()` method of the iterator returned by the `imap()` method has an optional _timeout_ parameter: `next(timeout)` will raise `multiprocessing.TimeoutError` if the result cannot be returned within _timeout_ seconds.

**imap_unordered(_func_, _iterable_[, _chunksize_])**

The same as `imap()` except that the ordering of the results from the returned iterator should be considered arbitrary. (Only when there is only one worker process is the order guaranteed to be “correct”.)

**starmap(_func_, _iterable_[, _chunksize_])**

Like `map()` except that the elements of the _iterable_ are expected to be iterables that are unpacked as arguments.

Hence an _iterable_ of `[(1,2), (3, 4)]` results in `[func(1,2), func(3,4)]`.

**starmap_async(_func_, _iterable_[, _chunksize_[, _callback_[, _error_callback_]]])**

A combination of `starmap()` and `map_async()` that iterates over _iterable_ of iterables and calls _func_ with the iterables unpacked. Returns a result object.

**close()**

Prevents any more tasks from being submitted to the pool. Once all the tasks have been completed the worker processes will exit.

**terminate()**

Stops the worker processes immediately without completing outstanding work. When the pool object is garbage collected `terminate()` will be called immediately.

**join()**

Wait for the worker processes to exit. One must call `close()` or `terminate()` before using `join()`.

Pool objects now support the context management protocol – see Context Manager Types. `__enter__()` returns the pool object, and `__exit__()` calls `terminate()`.

**_class_ multiprocessing.pool.AsyncResult**

The class of the result returned by `Pool.apply_async()` and `Pool.map_async()`.

**get([_timeout_])**

Return the result when it arrives. If _timeout_ is not `None` and the result does not arrive within _timeout_ seconds then `multiprocessing.TimeoutError` is raised. If the remote call raised an exception then that exception will be reraised by `get()`.

**wait([_timeout_])**

Wait until the result is available or until _timeout_ seconds pass.

**ready()**

Return whether the call has completed.

**successful()**

Return whether the call completed without raising an exception. Will raise `ValueError` if the result is not ready.