---
title: Основы Pandas
description:  Введение в Pandas, DataFrame и Series, основные операции, выборка, фильтрация, группировка, агрегирование данных, и роль Pandas в машинном обучении. Дополнительные команды Pandas для ML-разработчика.
published: true
date: 2025-02-25T19:00:00.000Z
tags: ml, selfstudy, pandas, python, анализ данных
editor: markdown
dateCreated: 2025-02-25T19:00:00.000Z
---

# 🐼 Основы Pandas: Ваш надежный инструмент для анализа данных в Python

**Pandas** — это мощная и гибкая библиотека Python, предназначенная для анализа и обработки структурированных (табличных) данных. Она особенно важна в машинном обучении, где данные часто представлены в табличной форме. Pandas предоставляет структуры данных **DataFrame** и **Series**, а также широкий набор инструментов для манипуляции, очистки, анализа и подготовки данных.

## 1. 🧱 Основа Pandas - DataFrame и Series

*   **DataFrame** - это основная структура данных Pandas, представляющая собой **двумерную таблицу** с именованными строками (индексом) и столбцами. **DataFrame** можно представить как набор **Series**, объединенных по общему индексу. Каждый столбец **DataFrame** является объектом **Series**.
*   **Series** - это **одномерная** структура данных, представляющая собой **столбец** или **строку DataFrame**. **Series** также имеет индекс, который может быть как числовым, так и произвольным.

**DataFrame** идеально подходит для работы с табличными данными, такими как:

*   Данные из CSV, Excel, SQL баз данных.
*   Результаты экспериментов и наблюдений.
*   Статистические данные.

### 💻 Пример создания DataFrame из словаря Python:

```python
import pandas as pd

# Создание DataFrame из словаря (Creating a DataFrame from a Python dictionary)
data = {
    'Имя': ['Анна', 'Борис', 'Виктор', 'Дарья'],
    'Возраст': [25, 30, 22, 28],
    'Город': ['Москва', 'Петербург', 'Казань', 'Москва']
}
df = pd.DataFrame(data)
print("DataFrame:\\n", df)
print("Тип DataFrame:", type(df))
```

### 📊 Пример создания Series:

```python
import pandas as pd

# Создание Series из списка (Creating a Series from a list)
ages = pd.Series([25, 30, 22, 28], name='Возраст')
print("\\nSeries:\\n", ages)
print("Тип Series:", type(ages))
```

## 2. 🔑 Ключевые операции с DataFrame

Pandas предоставляет множество функций для работы с DataFrame. Рассмотрим основные операции, которые необходимо изучить ML-разработчику.

### 2.1. 🛠️ Создание DataFrame

*   **Из словарей Python (From Python dictionaries):** `pd.DataFrame(dict)`
*   **Из списков списков (или массивов NumPy) (From lists of lists (or NumPy arrays)):** `pd.DataFrame(data, columns=column_names)`
*   **Чтение из файлов (Reading from files):**
    *   `pd.read_csv('file.csv')` - чтение CSV файлов (очень распространенный формат для ML данных) (reading CSV files (a very common format for ML data))
    *   `pd.read_excel('file.xlsx')` - чтение Excel файлов (reading Excel files)
    *   `pd.read_sql('SQL query', connection)` - чтение из SQL баз данных (reading from SQL databases)
    *   `pd.read_json('file.json')` - чтение JSON файлов (reading JSON files)

#### ✍️ Пример чтения CSV файла (новые команды):

```python
import pandas as pd

# Предположим, что у вас есть файл 'data.csv' в той же директории
# df_csv = pd.read_csv('data.csv')
# print("DataFrame из CSV:\\n", df_csv.head()) # Выведем первые 5 строк
```
*(Для этого примера вам понадобится создать файл 'data.csv' с данными)*

### 2.2. 👀 Просмотр данных (Viewing Data)

*   `.head(n)`: Первые `n` строк (по умолчанию 5) (First `n` rows (default 5)).
*   `.tail(n)`: Последние `n` строк (по умолчанию 5) (Last `n` rows (default 5)).
*   `.info()`: Общая информация о DataFrame (индексы, типы данных, количество не-пустых значений, использование памяти). **Критически важно для понимания структуры данных и поиска пропущенных значений.** (General information about the DataFrame (indices, data types, number of non-empty values, memory usage). **Critically important for understanding data structure and finding missing values.**)
*   `.describe()`: Описательные статистики для **числовых** столбцов (среднее, стандартное отклонение, минимум, максимум, квартили). Полезно для **первичного анализа распределения признаков**. (Descriptive statistics for **numeric** columns (mean, standard deviation, minimum, maximum, quartiles). Useful for **primary analysis of feature distribution**.)
*   `.sample(n)`: Случайная выборка `n` строк. Полезно для **быстрого просмотра случайных записей**. (Random sample of `n` rows. Useful for **quickly viewing random records**.)
*   `.shape`: Возвращает **форму** DataFrame в виде кортежа `(строки, столбцы)`. (Returns the **shape** of the DataFrame as a tuple `(rows, columns)`.)
*   `.columns`: Возвращает **список названий столбцов**. (Returns the **list of column names**.)
*   `.index`: Возвращает **индекс DataFrame**. (Returns the **DataFrame index**.)

#### ✍️ Пример команд просмотра:

```python
import pandas as pd

data = {'col1': [1, 2, 3, 4, 5], 'col2': ['a', 'b', 'c', 'd', 'e'], 'col3': [1.1, 2.2, 3.3, 4.4, 5.5]}
df = pd.DataFrame(data)

print("Первые 2 строки (df.head(2)):\\n", df.head(2))
print("\\nИнформация о DataFrame (df.info()):")
df.info()
print("\\nОписательные статистики (df.describe()):\\n", df.describe())
```

### 2.3. 🗂️ Выборка данных (индексация и slicing) (Data Selection (indexing and slicing))

*   **Выбор столбцов (Column Selection):**
    *   `df['название_столбца']` - возвращает **Series** (`df['column_name']` - returns **Series**)
    *   `df[['столбец1', 'столбец2']]` - возвращает **DataFrame** с выбранными столбцами (`df[['column1', 'column2']]` - returns **DataFrame** with selected columns)
*   **Выбор строк и столбцов по лейблам (`.loc`) (Row and column selection by labels (`.loc`)):**
    *   `.loc[row_labels, column_labels]` - позволяет выбирать данные по **названиям строк и столбцов**. (`.loc[row_labels, column_labels]` - allows you to select data by **row and column names**.)
    *   `df.loc[0:2, 'col1':'col2']` - slicing по лейблам (включает конец интервала!) (label-based slicing (includes the end of the interval!))
*   **Выбор строк и столбцов по позициям (`.iloc`) (Row and column selection by position (`.iloc`)):**
    *   `.iloc[row_indices, column_indices]` - позволяет выбирать данные по **целочисленным индексам строк и столбцов**. (`.iloc[row_indices, column_indices]` - allows you to select data by **integer indices of rows and columns**.)
    *   `df.iloc[0:2, 0:2]` - slicing по индексам (не включает конец интервала, как в Python slicing) (index-based slicing (does not include the end of the interval, like in Python slicing))

#### ✍️ Примеры выборки данных:

```python
import pandas as pd

data = {'col1': [1, 2, 3, 4, 5], 'col2': ['a', 'b', 'c', 'd', 'e'], 'col3': [1.1, 2.2, 3.3, 4.4, 5.5]}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4', 'row5']) # Зададим индекс (Set index)

# Выбор столбца 'col1' как Series (Selecting column 'col1' as Series)
col1_series = df['col1']
print("Столбец 'col1' (Series):\\n", col1_series)

# Выбор столбцов 'col1' и 'col3' как DataFrame (Selecting columns 'col1' and 'col3' as DataFrame)
subset_df = df[['col1', 'col3']]
print("\\nПодмножество столбцов (DataFrame):\\n", subset_df)

# Выбор строк 'row1' и 'row3' и столбцов 'col1' и 'col2' по лейблам (Selecting rows 'row1' and 'row3' and columns 'col1' and 'col2' by labels)
subset_loc = df.loc[['row1', 'row3'], ['col1', 'col2']]
print("\\nВыборка по лейблам (.loc):\\n", subset_loc)

# Выбор первых двух строк и первых двух столбцов по индексам (Selecting the first two rows and the first two columns by indices)
subset_iloc = df.iloc[0:2, 0:2]
print("\\nВыборка по индексам (.iloc):\\n", subset_iloc)
```

### 2.4. 🧽 Фильтрация данных (boolean indexing) (Data Filtering (boolean indexing))

*   `df[условие]` - отбор строк, удовлетворяющих **булевому условию**. `условие` должно быть Series булевых значений, полученным, например, сравнением столбца с каким-либо значением. (`df[condition]` - selecting rows that satisfy a **boolean condition**. `condition` must be a Series of boolean values, obtained, for example, by comparing a column with some value.)
*   **Логические операторы (Logical operators):** `&` (И), `|` (ИЛИ), `~` (НЕ) для комбинирования условий. **Важно использовать `()` для задания приоритета операций.** (`&` (AND), `|` (OR), `~` (NOT) for combining conditions. **It is important to use `()` to set the priority of operations.**)

#### ✍️ Примеры фильтрации:

```python
import pandas as pd

data = {'col1': [10, 20, 5, 15, 25], 'col2': ['a', 'b', 'c', 'b', 'a']}
df = pd.DataFrame(data)

# Фильтрация строк, где 'col1' > 15 (Filtering rows where 'col1' > 15)
filtered_df_greater = df[df['col1'] > 15]
print("Строки, где col1 > 15:\\n", filtered_df_greater)

# Фильтрация строк, где 'col2' == 'b' (Filtering rows where 'col2' == 'b')
filtered_df_equal = df[df['col2'] == 'b']
print("\\nСтроки, где col2 == 'b':\\n", filtered_df_equal)

# Комбинированное условие: ('col1' > 10) И ('col2' == 'a') (Combined condition: ('col1' > 10) AND ('col2' == 'a'))
combined_filter_and = df[(df['col1'] > 10) & (df['col2'] == 'a')]
print("\\nКомбинированная фильтрация (И):\\n", combined_filter_and)

# Комбинированное условие: ('col1' < 10) ИЛИ ('col2' == 'b') (Combined condition: ('col1' < 10) OR ('col2' == 'b'))
combined_filter_or = df[(df['col1'] < 10) | (df['col2'] == 'b')]
print("\\nКомбинированная фильтрация (ИЛИ):\\n", combined_filter_or)
```

### 2.5. ➗ Группировка и агрегирование (Grouping and Aggregation)

*   `.groupby('столбец_группировки')` - создает объект **GroupBy**, который позволяет выполнять операции над группами данных, разделенными по значениям указанного столбца. (`.groupby('grouping_column')` - creates a **GroupBy** object that allows performing operations on groups of data, separated by the values of the specified column.)
*   `.agg(функции_агрегации)` - применяет **агрегирующие функции** к каждой группе. Функции могут быть: (`.agg(aggregation_functions)` - applies **aggregation functions** to each group. Functions can be:)
    *   Строками (названия функций Pandas: `'mean'`, `'sum'`, `'count'`, `'min'`, `'max'`, `'std'`, `'median'`, и т.д.) (Strings (Pandas function names: `'mean'`, `'sum'`, `'count'`, `'min'`, `'max'`, `'std'`, `'median'`, etc.))
    *   Списками строк (применить несколько функций к одному столбцу) (Lists of strings (apply multiple functions to one column))
    *   Словарями (применить разные функции к разным столбцам: `{'столбец1': 'функция1', 'столбец2': ['функция2', 'функция3']}`) (Dictionaries (apply different functions to different columns: `{'column1': 'function1', 'column2': ['function2', 'function3']}`))

#### ✍️ Примеры группировки и агрегирования:

```python
import pandas as pd

data = {
    'Категория': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Значение': [10, 20, 15, 25, 12, 18]
}
df = pd.DataFrame(data)

# Группировка по столбцу 'Категория' и вычисление среднего значения (Grouping by the 'Category' column and calculating the mean value)
grouped_mean = df.groupby('Категория')['Значение'].mean() # Series
print("Среднее значение по категориям:\\n", grouped_mean)

# Группировка и применение нескольких агрегаций к столбцу 'Значение' (Grouping and applying multiple aggregations to the 'Value' column)
grouped_agg_single_col = df.groupby('Категория')['Значение'].agg(['mean', 'sum', 'count']) # DataFrame
print("\\nАгрегация нескольких функций к одному столбцу:\\n", grouped_agg_single_col)

# Группировка и применение разных агрегаций к разным столбцам (если бы был еще столбец) (Grouping and applying different aggregations to different columns (if there were another column))
# grouped_agg_multi_col = df.groupby('Категория').agg({'Значение': ['mean', 'max'], 'ДругойСтолбец': 'sum'})
# print("\\nАгрегация разных функций к разным столбцам:\\n", grouped_agg_multi_col)
```

### 2.6. ➕ Создание новых столбцов (Creating New Columns)

*   Новые столбцы можно создавать **на основе существующих** столбцов, применяя различные операции (арифметические, логические, строковые, функции). (New columns can be created **based on existing** columns, applying various operations (arithmetic, logical, string, functions).)
*   `df['новый_столбец'] = ...` - присваивание Series или массива NumPy создаст новый столбец в DataFrame. (`df['new_column'] = ...` - assigning a Series or NumPy array will create a new column in the DataFrame.)

#### ✍️ Примеры создания новых столбцов:

```python
import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

# Создание нового столбца 'col3' как суммы 'col1' и 'col2' (Creating a new column 'col3' as the sum of 'col1' and 'col2')
df['col3'] = df['col1'] + df['col2']
print("DataFrame с новым столбцом 'col3':\\n", df)

# Создание булевого столбца 'is_large' на основе 'col1' (Creating a boolean column 'is_large' based on 'col1')
df['is_large'] = df['col1'] > 2
print("\\nDataFrame с новым булевым столбцом 'is_large':\\n", df)
```

### 2.7. ⚙️ Дополнительные полезные команды Pandas для ML-разработчика (новые команды) (Additional Useful Pandas Commands for ML Developers (new commands))

*   **Обработка пропущенных значений (Handling Missing Values):**
    *   `.isnull()` - возвращает DataFrame булевых значений, True если значение NaN (пропущено). (`.isnull()` - returns a DataFrame of boolean values, True if the value is NaN (missing).)
    *   `.notnull()` -  обратно `.isnull()`. (`.notnull()` - opposite of `.isnull()`.)
    *   `.dropna()` - удаляет строки или столбцы с пропущенными значениями. (`.dropna()` - removes rows or columns with missing values.)
    *   `.fillna(value)` - заполняет пропущенные значения заданным значением (например, средним, медианой, нулем). **Важно выбирать стратегию заполнения в зависимости от природы данных.** (`.fillna(value)` - fills missing values with a specified value (e.g., mean, median, zero). **It is important to choose a filling strategy depending on the nature of the data.**)
*   **Работа с категориальными данными (Working with Categorical Data):**
    *   `.astype('category')` - преобразование столбца в категориальный тип данных (экономит память, ускоряет операции). (`.astype('category')` - converting a column to a categorical data type (saves memory, speeds up operations).)
    *   `.unique()` - возвращает **уникальные значения** в столбце. (`.unique()` - returns **unique values** in a column.)
    *   `.nunique()` - возвращает **количество уникальных значений** в столбце. (`.nunique()` - returns the **number of unique values** in a column.)
    *   `.value_counts()` - подсчитывает **частоту встречаемости** каждого уникального значения в столбце. **Полезно для анализа распределения категорий.** (`.value_counts()` - counts the **frequency of occurrence** of each unique value in a column. **Useful for analyzing the distribution of categories.**)
*   **Сортировка (Sorting):**
    *   `.sort_values(by='столбец', ascending=True)` - сортировка DataFrame по значениям указанного столбца. (`.sort_values(by='column', ascending=True)` - sorting the DataFrame by the values of the specified column.)
    *   `.sort_index(ascending=False)` - сортировка по индексу. (`.sort_index(ascending=False)` - sorting by index.)
*   **Применение функций к столбцам и DataFrame (Applying Functions to Columns and DataFrame):**
    *   `.apply(function)` - применяет функцию к столбцу (Series) или к DataFrame (по строкам или столбцам). **Очень гибкий инструмент для сложных преобразований.** (`.apply(function)` - applies a function to a column (Series) or to a DataFrame (row-wise or column-wise). **A very flexible tool for complex transformations.**)
    *   `.map(function)` - применяет функцию **поэлементно** к Series. (`.map(function)` - applies a function **element-wise** to a Series.)
    *   `.applymap(function)` - применяет функцию **поэлементно** к DataFrame. (`.applymap(function)` - applies a function **element-wise** to a DataFrame.)
*   **Объединение DataFrame (Joining DataFrame):**
    *   `pd.concat([df1, df2], axis=0)` - объединение DataFrame **по строкам** (axis=0) или **по столбцам** (axis=1). (`pd.concat([df1, df2], axis=0)` - concatenating DataFrames **row-wise** (axis=0) or **column-wise** (axis=1).)
    *   `pd.merge(df1, df2, on='ключевой_столбец', how='inner')` - **слияние** DataFrame по общему столбцу (аналог JOIN в SQL). Разные типы слияния: `'inner'`, `'outer'`, `'left'`, `'right'`. **Критически важно для объединения данных из разных источников.** (`pd.merge(df1, df2, on='key_column', how='inner')` - **merging** DataFrames by a common column (analogous to JOIN in SQL). Different types of merging: `'inner'`, `'outer'`, `'left'`, `'right'`. **Critically important for combining data from different sources.**)

#### ✍️ Пример обработки пропущенных значений:

```python
import pandas as pd
import numpy as np

data = {'col1': [1, 2, np.nan, 4, 5], 'col2': ['a', np.nan, 'c', 'd', 'e']}
df = pd.DataFrame(data)
print("DataFrame с NaN:\\n", df)

print("\\nПроверка на NaN (df.isnull()):\\n", df.isnull())

df_filled_0 = df.fillna(0) # Заполнение NaN нулями (Filling NaN with zeros)
print("\\nЗаполнение NaN нулями (df.fillna(0)) :\\n", df_filled_0)

df_dropped_rows = df.dropna() # Удаление строк с NaN (Removing rows with NaN)
print("\\nУдаление строк с NaN (df.dropna()):\\n", df_dropped_rows)
```

## 3. 🤔 Зачем Pandas нужен в машинном обучении? (Why is Pandas needed in Machine Learning?)

Pandas играет **центральную роль** в процессе машинного обучения, обеспечивая инструменты для работы с данными на всех этапах:

*   **Загрузка и чтение данных (Data Loading and Reading):**  Легко читает данные из различных источников в DataFrame. (Easily reads data from various sources into a DataFrame.)
*   **Предварительная обработка данных (Data Preprocessing):**  Предоставляет мощные инструменты для очистки, преобразования и подготовки данных к обучению моделей. **Качество данных напрямую влияет на качество ML-моделей.** (Provides powerful tools for cleaning, transforming, and preparing data for model training. **Data quality directly affects the quality of ML models.**)
*   **Исследовательский анализ данных (EDA - Exploratory Data Analysis):**  Вместе с библиотеками визуализации позволяет проводить EDA для понимания данных, выявления закономерностей и аномалий. **EDA помогает лучше понять задачу и выбрать подходящие модели и признаки.** (Together with visualization libraries, it allows conducting EDA to understand data, identify patterns and anomalies. **EDA helps to better understand the task and choose suitable models and features.**)
*   **Подготовка признаков (Feature Engineering):**  Упрощает создание новых, более информативных признаков на основе существующих. **Feature Engineering - ключевой фактор успеха во многих ML-проектах.** (Simplifies the creation of new, more informative features based on existing ones. **Feature Engineering is a key factor in the success of many ML projects.**)

## 4. 🔑 Ключевая идея Pandas

**Pandas DataFrame — это универсальный и мощный инструмент для работы с табличными данными в Python.**  Он значительно упрощает и ускоряет процесс анализа, обработки и подготовки данных для машинного обучения.  **Владение Pandas — это абсолютно необходимый навык для любого специалиста в области Data Science и Machine Learning.**