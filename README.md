# О чем проект
Демонстрация работы с бесплатным API сайта https://petstore.swagger.io/#/

На данном сайте предоставлены различные задания для тренировки Мануальных тестировщиков.
Я автоматизировала выполнение данных заданий, используя *Python*, *Pytest* и *Request*.

# Для запуска тестов без IDE: 
- клонировать репозиторий git себе на жесткий диск, в папку "C:\envir"
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

# What is the project about
Demonstration of working with the free site API https://petstore.swagger.io/#/

This site provides various tasks for training Manual testers.
I automated the execution of these tasks using *Python*, *Pytest* and *Request*.

# To run tests without an IDE:
- clone the git repository to your hard disk, in the folder "C:\envir"
- install Python at least version 3.6, during installation, make sure that you have checked the box in the "Add Python 3.x to PATH" section
- run the command line: cmd.exe
- create and activate a virtual environment with the following commands:
  - mkdir envir
  - cd envir
  - python -m venv rest_env
  - rest_env\Scripts\activate.bat

- install libraries for python: pip install -r C:\envir\requirements.txt
- run tests from a single file with the command: pytest -v C:/envir/tests/test_user.py
- run all the tests from the catalog with the command: pytest -v C:/envir/tests/
- run one test from the file: pytest-v C:/envir/tests/ - k test_create_list_of_users_with_given_input_array
- at the end of the work, deactivate the virtual environment: deactivate.bat
