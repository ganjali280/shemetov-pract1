import numpy as np

data_steps = np.array([
    8200, 11500, 9400, 7100, 10800, 8600, 12900, 45000, 9900, 9100,
    7600, 11300, 8300, 9700, 10400, 8900, 12100, 6800, 10200, 9200,
    200, 450, 8100, 11600, 7900, 9600, 10700, 8700, 12200, 6900
])

A = np.array([
    8000, 12000, 9500, 7000, 11000, 8500, 13000, 6000, 10000, 9000,
    7500, 11500, 8200, 9800, 10500
])

mean_val = np.mean(data_steps)
median_val = np.median(data_steps)
std_val = np.std(data_steps)
var_val = np.var(data_steps)
max_val = np.max(data_steps)
min_val = np.min(data_steps)
ptp_val = np.ptp(data_steps)

p25, p50, p75, p90, p99 = np.percentile(data_steps, [25, 50, 75, 90, 99])
q1 = np.percentile(data_steps, 25)
q3 = np.percentile(data_steps, 75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = data_steps[(data_steps < lower_bound) | (data_steps > upper_bound)]

print("\nРЕЗУЛЬТАТЫ ЗАДАНИЯ 1")
print(f"Среднее значение:               {mean_val}")
print(f"Медиана (50-й перцентиль):      {median_val}")
print(f"Стандартное отклонение:         {std_val}")
print(f"Дисперсия:                      {var_val}")
print(f"Максимальное значение:          {max_val}")
print(f"Минимальное значение:           {min_val}")
print(f"Размах данных:                  {ptp_val}")
print(f"25-й перцентиль (Q1):           {p25}")
print(f"50-й перцентиль (Q2):           {p50}")
print(f"75-й перцентиль (Q3):           {p75}")
print(f"90-й перцентиль:                {p90}")
print(f"99-й перцентиль:                {p99}")
print(f"Первый квартиль (Q1):           {q1}")
print(f"Третий квартиль (Q3):           {q3}")
print(f"Межквартильный размах (IQR):    {iqr}")
print(f"Допустимый интервал:            [{lower_bound}, {upper_bound}]")
print(f"Обнаруженные выбросы:           {outliers.tolist()}")

matrix_A = A.reshape(3, 5)
matrix_shape = matrix_A.shape
matrix_size = matrix_A.size
row_sums = matrix_A.sum(axis=1)
col_sums = matrix_A.sum(axis=0)
matrix_transposed = matrix_A.T

mean_A = np.mean(matrix_A)
std_A = np.std(matrix_A)
var_A = np.var(matrix_A)
q1_A, q2_A, q3_A = np.percentile(matrix_A, [25, 50, 75])

print("\nРЕЗУЛЬТАТЫ ЗАДАНИЯ 2 (Матрица A)")
print(f"Матрица 3x5:\n {matrix_A}")
print(f"Размерность: {matrix_shape}")
print(f"Общее количество элементов: {matrix_size}")
print(f"Сумма по строкам: {row_sums.tolist()}")
print(f"Сумма по столбцам: {col_sums.tolist()}")
print(f"Транспонированная матрица (5x3):\n {matrix_transposed}")
print(f"Среднее по элементам матрицы:       {mean_A}")
print(f"Стандартное отклонение матрицы:     {std_A}")
print(f"Дисперсия матрицы:                  {var_A}")
print(f"Квартили матрицы (Q1, Q2, Q3):      {q1_A}, {q2_A}, {q3_A}")

days_under_8000 = np.sum(data_steps < 8000)

print("\nИНДИВИДУАЛЬНЫЕ ВОПРОСЫ ВАРИАНТА 2")
print(f"Количество дней с шагами менее 8000: {days_under_8000}")
print(f"Значения шагов в эти дни:            {data_steps[data_steps < 8000].tolist()}")