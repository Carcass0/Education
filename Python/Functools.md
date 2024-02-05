## functools.partial(func, *args, **keywords)
Возвращает partial-объект (по сути, функцию), который при вызове вызывается как функция func, но дополнительно передают туда позиционные аргументы args, и именованные аргументы kwargs. Если другие аргументы передаются при вызове функции, то позиционные добавляются в конец, а именованные расширяют и перезаписывают.
Можно использовать вместо лямбд.
Можно использовать с методами (partialmethod)

```python
from functools import partial
basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010'))
```

### functools.wraps(wrapped, assigned=WRAPPER_ASSIGNEMENTS, updated=WRAPPER_UPDATES)
Декорирует декоратор. Позволяет возвращять имя и докстринг декорированной функции, а не декоратора.

## functools.cache()
Caches a function. If it's called again with the same parameters, pulls the result from cache. Also applicable to properties with cached_property()
## @**functools.total_ordering**
Декоратор класса, в котором задан один или более методов сравнения. Этот декоратор автоматически добавляет все остальные методы. Класс должен определять один из методов __lt__(), __le__(), __gt__(), или __ge__(). Кроме того, он должен определять метод __eq__().

## **functools.reduce**(function, iterable[, initializer]) 
Берёт два первых элемента, применяет к ним функцию, берёт значение и третий элемент, и таким образом сворачивает iterable в одно значение. Например, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) эквивалентно ((((1+2)+3)+4)+5). Если задан initializer, он помещается в начале последовательности.