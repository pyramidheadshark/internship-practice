# Массивы
## Краткое описание
Массивы - это фундаментальная структура данных, представляющая собой упорядоченную коллекцию элементов, доступ к которым осуществляется по индексу. Ключевые концепции:
- **Индексация:** доступ по позиции элемента, начиная с 0
- **Итерация:** подбор элементов массива
- **Срезы:** извлечение подмассивов с использованием срезов *([start:end:step])*

**Ранжирование по сложности (от простого к сложному):**
1.  [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) (Easy) - Простое использование множеств для проверки вхождения элементов.
2.  [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) (Easy) - Использование двух указателей и сортировки (хотя можно и без явной сортировки).
3.  [Move Zeroes](https://leetcode.com/problems/move-zeroes/) (Easy) - Два указателя для перемещения ненулевых элементов в начало массива.
4.  [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) (Easy) - Два указателя для удаления дубликатов в отсортированном массиве.
5.  [Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) (Easy) - Использование множеств для поиска различий между массивами.
6.  [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) (Easy/Medium) - Использование словарей или сортировки и двух указателей для поиска пересечений.
7.  [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (Easy/Medium) - Два указателя для поиска двух чисел в отсортированном массиве, дающих заданную сумму.
8.  [Find the Prefix Common Array of Two Arrays](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/) (Medium) - Итерирование и подсчет общих префиксов, использование множеств для эффективности.
9.  [Summary Ranges](https://leetcode.com/problems/summary-ranges/) (Medium) - Итерация и группировка последовательных чисел в диапазоны.
10. [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) (Medium) - Моделирование спирального заполнения матрицы, требует аккуратности с индексами.
11. [Rotate Image](https://leetcode.com/problems/rotate-image/) (Medium) - Поворот матрицы на 90 градусов, требует понимания перестановок элементов.
12. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium) - Бинарный поиск для нахождения первого и последнего вхождения элемента.
13. [Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/) (Medium) - Поиск максимального расстояния до ближайшего человека, требует обработки крайних случаев.
14. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium) - Вычисление произведения всех элементов, кроме текущего, за линейное время.
15. [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) (Medium) - Вариация задачи о максимальных последовательных единицах, с возможностью замены одной 0 на 1.
16. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) (Medium) - Расширение задачи, позволяющее заменять до `k` нулей на единицы, скользящее окно.
17. [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) - Сортировка и слияние перекрывающихся интервалов.
18. [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) (Medium) - Поиск пересечений между списками интервалов, два указателя.
19. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (Medium) - Бинарный поиск в отсортированном массиве с поворотом.
20. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Medium) - Бинарный поиск элемента в отсортированном массиве с поворотом.
21. [Partition Labels](https://leetcode.com/problems/partition-labels/) (Medium) - Разбиение строки на части так, чтобы каждая буква встречалась только в одной части, жадный подход.
22. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) - Вычисление количества воды, которое может быть задержано после дождя, два указателя или стек.
23. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) (Hard) - Поиск медианы двух отсортированных массивов, бинарный поиск, требует аккуратности с граничными условиями.
24. [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) (Hard) - Поиск максимальной площади прямоугольника из единиц в бинарной матрице, динамическое программирование или стек.

## Теоретический базис
**Ключевые Концепции:**

    Массив (Список в Python): Упорядоченная коллекция элементов одного типа (в Python - динамический список, может хранить разные типы). Главное - доступ по индексу за O(1).

    Индексация: Доступ к элементу по его позиции (начинается с 0). arr[i].

    Срезы: Извлечение подмассивов. arr[start:end:step].

    Итерация: Перебор элементов. for element in arr:, for i in range(len(arr)):.

    Размер: Количество элементов. len(arr).

    "In-place" операции: Изменение массива без создания нового. Важно для экономии памяти.

**Основные Алгоритмические Подходы для Массивов:**
    Линейный Проход (O(n)):

        Самый простой и часто используемый подход.

        Итерируем через массив от начала до конца (или в обратном направлении).

        Подходит для задач, где нужно:

            Найти элемент (линейный поиск).

            Подсчитать что-то (сумму, количество вхождений).

            Преобразовать каждый элемент по отдельности.

            Примеры задач: Jewels and Stones, Find the Difference of Two Arrays, Consecutive Characters.

    Два Указателя (Two Pointers) (O(n) или O(n log n) с сортировкой):

        Используем два индекса (указателя) для прохода по массиву.

        Когда применять:

            Отсортированный массив: Two Sum II, Squares of a Sorted Array, Remove Duplicates from Sorted Array, Find First and Last Position of Element in Sorted Array, Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array.

            Поиск пар элементов с определенным условием: Сумма, разность, и т.д.

            Сравнение элементов с разных концов массива: Valid Palindrome, Valid Palindrome II.

            Слияние массивов/интервалов: Merge Intervals, Interval List Intersections, Merge Sorted Array.

            Разделение массива на части: Move Zeroes, Remove Duplicates from Sorted Array.

        Типы:

            Сходящиеся указатели: Начинаются с разных концов и двигаются навстречу.

            Быстрый и медленный указатели: Один двигается быстрее другого (например, для удаления дубликатов "in-place").

    Скользящее Окно (Sliding Window) (O(n)):

        Поддерживаем "окно" (подмассив) заданного размера или с изменяемыми границами.

        Когда применять:

            Поиск подмассивов/подстрок с заданными свойствами: Максимальная/минимальная сумма, длина, количество уникальных элементов, и т.д.

            Задачи с "последовательными" элементами: Max Consecutive Ones II, Max Consecutive Ones III, Longest Substring Without Repeating Characters, Longest Substring With At Most K Distinct Characters, Find All Anagrams in a String, Permutation in String.

        Механизм:

            Окно определяется двумя указателями (left, right).

            Расширяем окно (right++), пока условие выполняется.

            Если условие нарушается, сжимаем окно (left++), пока условие не восстановится.

            Обрабатываем окно на каждом шаге (например, вычисляем сумму, длину, обновляем максимум).

    Бинарный Поиск (Binary Search) (O(log n)):

        Только для отсортированных массивов.

        Эффективный поиск элемента или границы.

        Когда применять:

            Поиск элемента в отсортированном массиве: Search in Rotated Sorted Array, Find First and Last Position of Element in Sorted Array, Find Minimum in Rotated Sorted Array.

            Поиск границы/условия: Например, найти первый элемент, удовлетворяющий условию.

    Префиксные Суммы (Prefix Sums) (O(n) для создания, O(1) для запроса суммы подмассива):

        Создаем массив префиксных сумм prefix_sum[i] = sum(arr[0:i+1]).

        Сумма подмассива arr[i:j+1] вычисляется как prefix_sum[j] - prefix_sum[i-1] (или просто prefix_sum[j] если i == 0).

        Когда применять:

            Задачи, где нужно часто вычислять суммы подмассивов: Subarray Sum Equals K, Subarray Sums Divisible by K (не в вашем текущем списке, но полезно знать).

            Задачи, где нужно быстро отвечать на запросы о суммах на диапазонах.

    Матрицы (Двумерные массивы):

        Массив массивов. matrix[row][col].

        Обходы матриц:

            Построчный, постолбцовый.

            Спиральный обход (Spiral Matrix II).

        Операции с матрицами:

            Поворот матрицы (Rotate Image).

            Поиск в матрице.

            Динамическое программирование на матрицах (Maximal Rectangle).

**Python Инструменты:**
    list (список): Основная структура данных для массивов.

        Создание: [], list(), [x for x in ...].

        Индексация, срезы, методы (append, insert, remove, pop, sort, reverse, index, count).

    len(): Длина массива.

    min(), max(), sum(): Минимум, максимум, сумма элементов.

    sorted(), reversed(): Сортировка, разворот (создают новые списки).

    collections.Counter: Подсчет частот элементов.

    collections.deque: Двусторонняя очередь (для эффективного скользящего окна, если нужно быстро удалять элементы с начала)