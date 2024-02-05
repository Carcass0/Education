A way to formally incorporate structural subtyping (or "duck" typing) into the python type annotation system.

There are two main, but related, use cases for Protocols. First, they can be used as an interface for classes and functions which can be used downstream in other classes or functions. Secondly, they can be used to set bounds on generic types.

We inherit from typing.Protocol instead of abc.ABC and we don't need to add the @abstractmethod decorators since Protocols are not meant to be "implemented" but simply act as an interface in downstream tasks. Lastly, it is common practice to use ... in the body of methods in a Protocol

Children of a Protocol class do not need to subclass from it, simply implement it< to be considered a valid instance of the class by the typechecker.

[[ABCs]] raise an error when improper classes are created, whereas Protocols do so only when they are used, and only with a static typechecker.