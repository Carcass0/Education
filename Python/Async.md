The syntax `async def` introduces either a **native coroutine** or an **asynchronous generator**. The expressions `async with` and `async for` are also valid.

The keyword `await` passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an `await f()` expression in the scope of `g()`, this is how `await` tells the event loop, “Suspend execution of `g()` until whatever I’m waiting on—the result of `f()`—is returned. In the meantime, go let something else run.”

Along with plain `async`/`await`, Python also enables `async for` to iterate over an **asynchronous iterator**. The purpose of an asynchronous iterator is for it to be able to call asynchronous code at each stage when it is iterated over.

A natural extension of this concept is an **asynchronous generator**. Recall that you can use `await`, `return`, or `yield` in a native coroutine. Using `yield` within a coroutine became possible in Python 3.6 (via PEP 525), which introduced asynchronous generators with the purpose of allowing `await` and `yield` to be used in the same coroutine function body.

Last but not least, Python enables **asynchronous comprehension** with `async for`. Like its synchronous cousin, this is largely syntactic sugar.

This is a crucial distinction: **neither asynchronous generators nor comprehensions make the iteration concurrent**. All that they do is provide the look-and-feel of their synchronous counterparts, but with the ability for the loop in question to give up control to the event loop for some other coroutine to run.

The battle over async IO versus multiprocessing is not really a battle at all. In fact, they can be [used in concert](https://youtu.be/0kXaLh8Fz3k?t=10m30s). If you have multiple, fairly uniform CPU-bound tasks (a great example is a [grid search](http://scikit-learn.org/stable/modules/grid_search.html#parallelism) in libraries such as `scikit-learn` or `keras`), multiprocessing should be an obvious choice.

Simply putting `async` before every function is a bad idea if all of the functions use blocking calls. (This can actually slow down your code.) But as mentioned previously, there are places where async IO and multiprocessing can [live in harmony](https://youtu.be/0kXaLh8Fz3k?t=10m30s).

Async IO shines when you have multiple IO-bound tasks where the tasks would otherwise be dominated by blocking IO-bound wait time, such as:

- Network IO, whether your program is the server or the client side
    
- Serverless designs, such as a peer-to-peer, multi-user network like a group chatroom
    
- Read/write operations where you want to mimic a “fire-and-forget” style but worry less about holding a lock on whatever you’re reading and writing to
