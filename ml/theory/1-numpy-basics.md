# 📚 Основы NumPy для ML 🔢

**NumPy** (Numerical Python) — это библиотека для численных вычислений в Python, которая лежит в основе работы с данными в машинном обучении (ML). Она поддерживает многомерные массивы и матрицы, а также предоставляет функции для их эффективной обработки. В ML NumPy нужен для представления данных (например, признаков и меток) и выполнения математических операций, таких как вычисления в моделях.

## Что такое массивы NumPy? 🤔

В основе NumPy лежит объект **ndarray** — N-мерный массив. Это сетка значений одного типа, к которым можно обращаться по индексам.

**Ключевые особенности:**
- **Однородность:** Все элементы одного типа (например, `float` или `int`), что ускоряет вычисления.
- **Многомерность:** Массивы могут быть 1D (векторы), 2D (матрицы) или N-мерными (тензоры).
- **Фиксированный размер:** Размер задается при создании, что отличает их от списков Python.
- **Эффективность:** Реализация на C делает операции быстрее, чем с обычными списками.

**Пример структуры (аналогия):**
- 1D массив `[1, 2, 3]` — как список покупок.
- 2D массив `[[1, 2], [3, 4]]` — как таблица (строки — объекты, столбцы — их свойства).

## Базовые операции с массивами NumPy ➕➖✖️➗

Установим NumPy (если еще не сделано):  
```
pip install numpy
```
Импортируем библиотеку:  
```
import numpy as np
```

### Создание массивов
```
# 1D массив (вектор) — строка чисел
vector = np.array([1, 2, 3, 4, 5])
print("Вектор:", vector)

# 2D массив (матрица) — таблица чисел
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nМатрица:\n", matrix)
```

### Операции с массивами
```
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Поэлементные операции (каждый элемент обрабатывается отдельно)
print("Сложение:", a + b)          # [5, 7, 9]
print("Умножение:", a * b)         # [4, 10, 18]
print("Скалярное умножение:", a * 2)  # [2, 4, 6]
```

## Введение в векторы и матрицы 📐

В ML:
- **Векторы (1D массивы):** Это точки в пространстве. Например, `[рост, вес]` описывает человека.
- **Матрицы (2D массивы):** Это наборы точек. Например, таблица, где строки — образцы, а столбцы — признаки.

**Пример из ML:** Датасет с тремя людьми:
```
[[170, 70],  # Рост и вес первого человека
 [165, 60],  # второго
 [180, 80]]  # третьего
```


NumPy позволяет выполнять операции линейной алгебры:  
```
# Матричное умножение (np.dot)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Матричное умножение:\n", np.dot(A, B))

# Транспонирование (меняем строки и столбцы)
print("Транспонированная матрица A:\n", A.T)
```

Эти операции нужны, например, в линейной регрессии, где предсказание = признаки × веса.

## Пример применения в ML

Представим данные и сделаем простое вычисление:  
```
# Датасет: 2 человека с ростом и весом
X = np.array([[170, 70], [165, 60]])  # Матрица признаков
weights = np.array([0.5, 0.3])         # Веса модели

# Предсказание (рост * 0.5 + вес * 0.3)
predictions = np.dot(X, weights)
print("Предсказания:", predictions)
```

Здесь `X` — матрица данных, а `np.dot` вычисляет предсказания модели.

## Практические задания
1. Создай 1D массив с числами от 1 до 5 и умножь его на 3. Что получится?
2. Создай 2D массив 2×3 с любыми числами и транспонируй его.
3. Возьми матрицу `[[1, 2], [3, 4]]` и вектор `[5, 6]`. Вычисли их матричное произведение.