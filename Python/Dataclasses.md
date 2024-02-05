@dataclass фактически создаёт класс, для которого определены `__init__`, присваивающий значения атрибутов, а также `__eq__` и `__repr__`.

С помощью параметров декоратор `dataclass` позволяет сгенерировать дополнительный шаблонный код и вообще настроить генерацию кода:
```python
def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
              unsafe_hash=False, frozen=False, match_args=True,
              kw_only=False, slots=False, weakref_slot=False)
```
Рассмотрим базовые параметры:
- init: если равно `True`, то генерируется функция `__init__()`. По умолчанию равно `True`
- repr: если равно `True`, то генерируется функция `__repr__()`, которая возвращает строковое представление объекта. По умолчанию равно `True`
- eq: если равно `True`, то генерируется функция `__eq__()`, которая сравнивает два объекта. По умолчанию равно `True`
- order: если равно `True`, то генерируются функции `__lt__` (операция <), `__le__` (<=), `__gt__` (>), `__ge__` (>=), которые применяются для упорядочивания объектов. По умолчанию равно `False`
- `unsafe_hash`: If `False` (the default), a `__hash__()` method is generated according to how `eq` and `frozen` are set.
- `frozen`: If true (the default is `False`), assigning to fields will generate an exception. This emulates read-only frozen instances. If `__setattr__()` or `__delattr__()` is defined in the class, then `TypeError` is raised.
- `match_args`: If true (the default is `True`), the `__match_args__` tuple will be created from the list of parameters to the generated `__init__()` method (even if `__init__()` is not generated). If false, or if `__match_args__` is already defined in the class, then `__match_args__` will not be generated.
- `kw_only`: If true (the default value is `False`), then all fields will be marked as keyword-only. If a field is marked as keyword-only, then the only effect is that the `__init__()` parameter generated from a keyword-only field must be specified with a keyword when `__init__()` is called. There is no effect on any other aspect of dataclasses.
-  `slots`: If true (the default is `False`), `__slots__` attribute will be generated and new class will be returned instead of the original one. If `__slots__` is already defined in the class, then `TypeError` is raised.
- `weakref_slot`: If true (the default is `False`), add a slot named “__weakref__”, which is required to make an instance weakref-able. It is an error to specify `weakref_slot=True` without also specifying `slots=True`.
Кроме того, те функции, которые создаются по умолчанию, могут быть переопределены.