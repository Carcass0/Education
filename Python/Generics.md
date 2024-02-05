Introduced to the typing module in 3.12. Functionally replaces TypeVar and TypeAliases. 
```python
type IntOrStr = int | str

type ListOrSet[T] = list[T] | set[T]
```
