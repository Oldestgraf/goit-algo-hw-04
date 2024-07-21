## Продуктивність алгоритмів сортування

Цей проект вимірює та порівнює продуктивність трьох різних алгоритмів сортування: сортування вставкою, сортування злиттям та вбудований метод сортування Python. Результати базуються на сортуванні масивів з 1000 випадково згенерованих цілих чисел.

### Алгоритми

#### Сортування Вставкою

Сортування вставкою - це простий алгоритм сортування, який створює кінцевий відсортований масив по одному елементу за раз. Він набагато менш ефективний на великих списках порівняно з більш просунутими алгоритмами, такими як швидке сортування, сортування купою або сортування злиттям.

#### Сортування Злиттям
Сортування злиттям - це ефективний, стабільний і заснований на порівняннях алгоритм сортування. Більшість реалізацій забезпечують стабільне сортування, що означає, що реалізація зберігає порядок введення однакових елементів у відсортованому результаті.

#### Вбудоване Сортування
Вбудований метод сортування Python, sort(), є високо оптимізованою реалізацією Timsort, який походить від сортування злиттям і сортування вставкою.

### Результати Продуктивності
Продуктивність кожного алгоритму сортування вимірювалася за допомогою модуля timeit. Час виконання для кожного алгоритму був записаний протягом 10 повторень сортування 10 масивів по 1000 елементів кожен.

#### Результати
Час сортування вставкою: 0.3826453 секунд
Час сортування злиттям: 0.0109302 секунд
Час вбудованого сортування: 0.0003207 секунд

### Висновки
Вбудований метод сортування Python (sort()) є найефективнішим серед трьох.
Він використовує Timsort, який має часову складність O(n log n) і високо оптимізований для реальних даних.
Він перевершує як сортування вставкою, так і сортування злиттям з точки зору швидкості та ефективності.
Загалом, для великих наборів даних або коли критична продуктивність, рекомендовано використовувати вбудований метод сортування Python через його чудову продуктивність та ефективність.