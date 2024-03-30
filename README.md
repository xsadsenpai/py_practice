## Самостоятельная работа №3

### Задание №1
- Текст задания

Напишите программу, которая преобразует 1 в 31.
Для выполнения поставленной задачи необходимо обязательно и
только один раз использовать:
• Цикл for
• *= 5
• += 1
Никаких других действий или циклов использовать нельзя

- Оформленный код

```python
result = 1
for _ in range(5):
    result = result * 5 + 1
print(result)
```

- Скрины консоли
  ![img_3_1.png](https://github.com/xsadsenpai/py_practice/blob/lab3/pic/img_3_1.png)

- Развернутый вывод

Этот код также использует цикл for, операторы *= и += для преобразования числа 1 в 31. Оператор *= умножает текущее значение на 5, а затем прибавляется 1, и так происходит 5 раз.
