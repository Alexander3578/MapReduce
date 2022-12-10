# MapReduce
Course project

# Задача для практики

Взять несколько произведений, построить процесс оценки статистических особенностей стиля написания текста каждому:

    1) средняя длина предложения
    2) количество различных слов среди 1000 подряд идущих слов
    3) среденее количество знаков препинания в предложении
    4) самые длинные предложения и их длина
    
# Docker

Развертывание кластера:

  1) Установим образ из репозитория
  
  2) Переходим в клонированную папку и запускаем кластер
     (docker-compose up -d) 
     Для проверки работоспособности контейнеров
     (docker ps)
    
  3) Скрипты: для решения задачи понадобиться реализация функция Map (mapper.py) и Reduce (reducer.py). Ввод и вывод происходит через стандартные потоки ввода и вывода        (import sys, выводить можно через print).
     Написанные скрипты нужно скопировать в namenode при помощи команды 
     (docker cp)
     
  4) Для запуска нужно войти в контейнер namenode.
     (docker exec -it namenode bash)
     Для выхода
     (exit)
     Далее нужно использовать bash скрипты.
     
     Просмотр содержимого каталога командой.
     (ls) 
     
     Далее создадим директорию input для книг.
     (mkdir input)
     
     Копируем сюда книги.
     (docker cp)

  5) MapReduce обращается к файлам из HDFS, следовательно туда нужно перенести input.
     Создаем в HDFS каталог input:
     (hadoop fs -mkdir -p input)
     
     переносим input
     (hdfs dfs -put ./input/* input)
     
  6) Скачиваем python на все узлы:
     (docker exec -it namenode bash -c "apt update && apt-get install python3 -y")
     (docker exec -it datanode bash -c "apt update && apt-get install python3 -y")
     (docker exec -it resourcemanager bash -c "apt update && apt-get install python3 -y")
     (docker exec -it nodemanager bash -c "apt update && apt-get install python3 -y")
     
  7) Запускаем MapReduce командой:
  
     (hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
     -files mapper4.py, reducer4.py \
     -input input \
     -output output \
     -mapper mapper4.py \
     -reducer reducer4.py)
     
     Соответствующие файлы. jar файл может находиться по другому адресу, найти его можно так:
      (find / -name 'hadoop-streaming*.jar')
      
     При запуске программа может ругаться на наличие директории output, удалить её можно так:     
      (hadoop fs -rmr /user/root/output)
      
     Просмотр результата операции 
      (hadoop fs -cat /user/root/output/part-00000)
      
     Чтобы извлечь в отдельный файл нужно сначала скопировать из HDFS в контейнер, а затем и в локальную файловую систему:
     
      (hadoop fs -cat /user/root/output/part-00000 > result.txt)
      (exit)
      (docker cp namenode:result.txt <LOCAL_PATH>\result.txt)

    Проверить работоспособность на относительно небольших данных можно так:
      (cat input/<FILE.txt> | python3 mapper3.py | python3 reducer3.py)

    Безопасно завершить работу контейнера:
      (docker-compose down)








