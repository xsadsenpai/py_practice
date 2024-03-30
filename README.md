## Самостоятельная работа №7

### Задание №1
- Текст задания

Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

- Оформленный код

```python
def count_words(file_name):
    try:
        word_count = {}
        max_count_word = ""
        max_count = 0

        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip(",.!?")
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
                        if word_count[word] > max_count:
                            max_count = word_count[word]
                            max_count_word = word

        total_words = sum(word_count.values())
        unique_words = len(word_count)

        return total_words, unique_words, max_count_word, max_count
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    except Exception as e:
        print("Произошла ошибка:", e)
        return None

file_name = "kontur.txt"

try:
    result = count_words(file_name)
    if result is not None:
        total_words, unique_words, most_common_word, max_count = result
        print("Самое часто встречающееся слово:", most_common_word)
        print("Количество его вхождений:", max_count)
except Exception as e:
    print("Произошла ошибка:", e)
```

- Скрины консоли
  ![img_7_1_1.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_1_1.png)
  ![img_7_1_2.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_1_2.png)
  ![img_7_1_3.png](https://github.com/xsadsenpai/py_practice/blob/lab7/pic/img_7_1_3.png)

- Развернутый вывод

Код подтягивает файл с директории, посчитывает часто встречающие слова и сколько раз оно было использовано.

### Задание №2
- Текст задания



- Оформленный код

```python

```

- Скрины консоли
  ![img_7_2.png](https://github.com/xsadsenpai/py_practice/blob/lab2/pic/img_7_2.png)

- Развернутый вывод

