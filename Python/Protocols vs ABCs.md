- [[ABCs| **Abstract Base Classes**]]
    
    - Belong to their subclasses. An ABC is not usable by itself, it can only be used by implementing a child class. So because of this, ABCs inherently belong to their subclasses as part of a strict class hierarchy.
    - ABCs are a good mechanism for code reuse, especially for boilerplate code or logic that will not change for any (or most) subclasses. The best strategy here is to have the ABC (i.e. parent class) do most of the work and have the children implement the specifics.
    - Good for real time validation when _creating_ an instance of a child class. ABCs will raise an error on creation if the child does not implement all abstract methods.

- [[Protocols | **Protocols**]]

    
    - Belong where they are used. Protocols are not "implemented" but tell downstream code (i.e. other functions or classes) what the structure of the input object is expected to be. Also we can define multiple protocols for the same kind of object depending on what is needed. This means that Protocols belong where they are used.
    - Good for defining interfaces, especially for 3rd-party libraries when we don't want to tightly couple our code to a specific 3rd party library.
    - Good (really the only way) for specifying flexible generic type bounds.
    - This somewhat goes without saying but Protocols only are useful if using type annotations and cannot be used in any other way (except for runtime_checkable) 

- Use ABCs if you want to reuse code. Inheritance is not always the best method of code reuse but it can be quite useful.
- Use ABCs if you require strict class hierarchy (as in you need to use method resolution order or you need to check `__subclasses__`) in your application.
- Use ABCs if you will need several implementations of a class with several methods.
- Use Protocols for strict type annotations (i.e.only annotate the methods/attributes you need)
- Use Protocols for generic bounds
- Use Protocols for abstract interfaces for 3rd party libraries