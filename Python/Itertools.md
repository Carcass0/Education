**itertools.count**(start=0, step=1) - бесконечная арифметическая прогрессия с первым членом start и шагом step.

**itertools.cycle**(iterable) - возвращает по одному значению из последовательности, повторенной бесконечное число раз.

**itertools.repeat**(elem, n=Inf) - повторяет elem n раз.

**itertools.accumulate**(iterable) - аккумулирует суммы.

**itertools.chain**(*iterables) - возвращает по одному элементу из первого итератора, потом из второго, до тех пор, пока итераторы не кончатся.

**itertools.combinations**(iterable, r) - комбинации длиной r из iterable без повторяющихся элементов.

**itertools.combinations_with_replacement**(iterable, r) - комбинации длиной r из iterable с повторяющимися элементами.

**itertools.compress**(data, selectors) - (d[0] if s[0]), (d[1] if s[1]), ...

**itertools.takewhile**(func, iterable) - элементы до тех пор, пока func возвращает истину.

**itertools.dropwhile**(func, iterable) - элементы iterable, начиная с первого, для которого func вернула ложь.

**itertools.filterfalse**(func, iterable) - все элементы, для которых func возвращает ложь.

**itertools.groupby**(iterable, key=None) - группирует элементы по значению. Значение получается применением функции key к элементу (если аргумент key не указан, то значением является сам элемент).
Каждый раз, когда изменяется значение, возвращаемое функцией `key`, создаётся новая группа. Поэтому целесообразно сортировать элементы, используя эту же функцию. Таким образом, поведение отличается от поведения `GROUP BY` в `SQL`, группирующей элементы вне зависимости от их порядка.  
Функция выдаёт кортежи из двух элементов.  
Первый элемент: значение, возвращённое функцией `key`.  
Второй элемент: итератор по объектам, попавшим в группу.

**itertools.islice**(iterable, start, stop, step) - итератор, состоящий из среза.

**itertools.permutations**(iterable, r=None) - перестановки длиной r из iterable.

**itertools.product**(*iterables, repeat=1) - аналог вложенных циклов. (+- cartesian product)

**itertools.starmap**(function, iterable) - применяет функцию к каждому элементу 
последовательности (каждый элемент распаковывается).

**itertools.tee**(iterable, n) - кортеж из n итераторов.

**itertools.zip_longest**(*iterables, fillvalue=None) - как встроенная функция zip, но берет самый длинный итератор, а более короткие дополняет fillvalue.

**itertools.batched(iterable, n)** - returns batches of length n