```python
from enum import Enum

# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# functional syntax
Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
```

слева name справа value

`_missing_` method can be used to create custom search logic to access enum members using values that aren't in the enum

_StrEnum_ is the same as _Enum_, but its members are also strings and can be used in most of the same places that a string can be used. The result of any string operation performed on or with a _StrEnum_ member is not part of the enumeration.

```python
from enum import Flag
class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64
```

We’ve changed two things: we’re inherited from `Flag`, and the values are all powers of 2.

Just like the original `Weekday` enum above, we can have a single selection:
```python
first_week_day = Weekday.MONDAY
first_week_day
```

But `Flag` also allows us to combine several members into a single variable:
```python
weekend = Weekday.SATURDAY | Weekday.SUNDAY
weekend
```

You can even iterate over a `Flag` variable:
```python
for day in weekend:
    print(day)
```


Read more: https://docs.python.org/3/howto/enum.html#enum-basic-tutorial