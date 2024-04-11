# Чтение файла со стоп-словами и создание списка стоп-слов
with open("stop-slov.txt", 'r') as f:
    stop_words = f.read().split(",")
    stop_words = [word.strip().lower() for word in stop_words]


