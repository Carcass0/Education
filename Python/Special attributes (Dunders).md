
| `__init__` | Initialise object |  |  |
| ---- | ---- | ---- | ---- |
| `__new__` | Create object | def __new__(cls, *args, **kwargs):<br>        instance = super().__new__(cls)<br>        *В этом месте можно настроить экземпляр<br>        return instance<br>Вызывается до init, действует больше на уровне класса<br>Используется при создании классов, наследующих иммутабельные классы |  |
| `__del__` | Destroy object |  |  |
| `__repr__` | Compute “official” string representation / `repr(obj)` | Formal string representation |  |
| `__str__` | Pretty print object / `str(obj)` / `print(obj)` | Informal string representation |  |
| `__bytes__` | `bytes(obj)` | bytestring representation |  |
| `__format__` | Custom string formatting | called by Format() |  |
| `__lt__` | `obj < ...` |  |  |
| `__le__` | `obj <= ...` |  |  |
| `__eq__` | `obj == ...` |  |  |
| `__ne__` | `obj != ...` |  |  |
| `__gt__` | `obj > ...` |  |  |
| `__ge__` | `obj >= ...` |  |  |
| `__hash__` | `hash(obj)` / object as dictionary key |  |  |
| `__bool__` | `bool(obj)` / define Truthy/Falsy value of object |  |  |
| `__getattr__` | Fallback for attribute access |  |  |
| `__getattribute__` | Implement attribute access: `obj.name` |  |  |
| `__setattr__` | Set attribute values: `obj.name = value` |  |  |
| `__delattr__` | Delete attribute: `del obj.name` |  |  |
| `__dir__` | `dir(obj)` |  |  |
| `__get__` | Attribute access in descriptor |  |  |
| `__set__` | Set attribute in descriptor |  |  |
| `__delete__` | Attribute deletion in descriptor |  |  |
| `__init_subclass__` | Initialise subclass |  |  |
| `__set_name__` | Owner class assignment callback |  |  |
| `__instancecheck__` | `isinstance(obj, ...)` |  |  |
| `__subclasscheck__` | `issubclass(obj, ...)` |  |  |
| `__class_getitem__` | Emulate generic types |  |  |
| `__call__` | Emulate callables / `obj(*args, **kwargs)` |  |  |
| `__len__` | `len(obj)` |  |  |
| `__length_hint__` | Estimate length for optimisation purposes |  |  |
| `__getitem__` | Access `obj[key]` |  |  |
| `__setitem__` | `obj[key] = ...` or `obj[]` |  |  |
| `__delitem__` | `del obj[key]` |  |  |
| `__missing__` | Handle missing keys in `dict` subclasses |  |  |
| `__iter__` | `iter(obj)` / `for ... in obj`  | [[Iterators \| iterating over]] |  |
| `__reversed__` | `reverse(obj)` |  |  |
| `__contains__` | `... in obj` (membership test) |  |  |
| `__add__` | `obj + ...` |  |  |
| `__radd__` | `... + obj` |  |  |
| `__iadd__` | `obj += ...` |  |  |
| `__sub__` | `obj - ...` |  |  |
| `__mul__` | `obj * ...` |  |  |
| `__matmul__` | `obj @ ...` |  |  |
| `__truediv__` | `obj / ...` |  |  |
| `__floordiv__` | `obj // ...` |  |  |
| `__mod__` | `obj % ...` |  |  |
| `__divmod__` | `divmod(obj, ...)` |  |  |
| `__pow__` | `obj ** ...` |  |  |
| `__lshift__` | `obj << ...` |  |  |
| `__rshift__` | `obj >> ...` |  |  |
| `__and__` | `obj & ...` |  |  |
| `__xor__` | `obj ^ ...` |  |  |
| `__or__` | `obj \| ...` |  |  |
| `__neg__` | `-obj` (unary) |  |  |
| `__pos__` | `+obj` (unary) |  |  |
| `__abs__` | `abs(obj)` |  |  |
| `__invert__` | `~obj` (unary) |  |  |
| `__complex__` | `complex(obj)` |  |  |
| `__int__` | `int(obj)` |  |  |
| `__float__` | `float(obj)` |  |  |
| `__index__` | Losslessly convert to integer |  |  |
| `__round__` | `round(obj)` |  |  |
| `__trunc__` | `math.trunc(obj)` |  |  |
| `__floor__` | `math.floor(obj)` |  |  |
| `__ceil__` | `math.ceil(obj)` |  |  |
| `__enter__` | `with obj` (enter context manager) |  |  |
| `__exit__` | `with obj` (exit context manager) |  |  |
| `__await__` | Implement awaitable objects |  |  |
| `__aiter__` | `aiter(obj)` |  |  |
| `__anext__` | `anext(obj)` |  |  |
| `__aenter__` | `async with obj` (enter async context manager) |  |  |
| `__aexit__` | `async with obj` (exit async context manager) |  |  |
| `__match_args__` | defines an explicit order for your attributes that can be used in pattern matching |  |  |
| [[Slots \| `__slots__`]] | allows you to explicitly state which instance attributes you expect your object instances to have |  |  |
