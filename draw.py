import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**4 + x**3 - 6*x**2 + 20*x - 16


# Генеруємо значення x
x = np.linspace(-5, 5, 1000)  # Більше точок для плавного графіка

# Обчислюємо значення y для кожного x
y = f(x)

# Задаємо розмір графіка
# plt.figure(figsize=(6, 4))import numpy as np

# Визначаємо функцію


def f(x):
    return x**4 + x**3 - 6*x**2 + 20*x - 16


# Генеруємо значення x
x = np.linspace(-5, 5, 10000)

# Обчислюємо значення y для кожного x
y = f(x)

# Задаємо розмір графіка
fig, ax = plt.subplots(figsize=(6, 4))

# Створюємо графік
ax.plot(x, y, label=r'$x^4 + x^3 - 6x^2 + 20x - 16$', color='blue')

# Налаштовуємо осі OX та OY
ax.axhline(0, color='black', linewidth=1)  # Ось Ox
ax.axvline(0, color='black', linewidth=1)  # Ось Oy

# Переміщуємо осі до центру
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Прибираємо верхню та праву рамки
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Додаємо стрілки на кінцях осей
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Задаємо діапазон осей
ax.set_xlim([-10, 10])
ax.set_ylim([min(y), max(y)])

# Підписи осей ближче до осей
ax.set_xlabel('x', loc='right')
ax.set_ylabel('f(x)', loc='top')

# Додаємо заголовок
# ax.set_title(
# 'Графік функції $x^4 + x^3 - 6x^2 + 20x - 16$ на інтервалі [-10, 10]')

# Додаємо сітку
# ax.grid(True)

# Додаємо легенду
# ax.legend()

# Зберігаємо графік у файл
plt.savefig('plot.png')

# Відображаємо графік
plt.show()


# Створюємо графік
plt.plot(x, y, label=r'$x^4 + x^3 - 6x^2 + 20x - 16$', color='blue')

# Додаємо осі OX та OY
plt.axhline(0, color='black', linewidth=1)  # Ось Ox
plt.axvline(0, color='black', linewidth=1)  # Ось Oy


# Переміщуємо осі до центру
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Прибираємо верхню та праву рамки
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


# Задаємо діапазон для осі x
# plt.xlim([-10, 10])

# Задаємо діапазон для осі y відповідно до мінімальних та максимальних значень функції
# plt.ylim([min(y), max(y)])

# Додаємо підписи до осей
# plt.xlabel('x')
# plt.ylabel('f(x)')
#
# # plt.legend()
#
# # Зберігаємо графік у файл
# plt.savefig('detailed_plot_with_axes.png')
#
# # Відображаємо графік
# plt.show()
