# О чем проект
Демонстрация работы с бесплатным API сайта https://petstore.swagger.io/#/

На данном сайте предоставлены различные задания для тренировки Мануальных тестировщиков.
Я автоматизировала выполнение данных заданий.

# Для запуска тестов без IDE: 
- клонировать репозиторий git себе на жесткий диск, например в папку "C:\envir"
- установить Python не ниже версии 3.6, во время установки убедиться в том, что вы поставили галочку в разделе "Add Python 3.x to PATH"
- запустить командную строку: cmd.exe
- создать и активировать виртуальное окружение командами:
    - mkdir envir
    - cd envir
    - python -m venv rest_env
    - rest_env\Scripts\activate.bat

- установить библиотеки для python:   pip install -r C:\envir\requirements.txt
- запустить тесты из одного файла можно командой: pytest -v C:/envir/tests/test_user.py
- запустить все тесты из каталога можно командой: pytest -v C:/envir/tests/
- запустить один тест из файла: pytest -v C:/envir/tests/ -k test_create_list_of_users_with_given_input_array
- в конце работы деактивировать виртуальное окружение: deactivate.bat
