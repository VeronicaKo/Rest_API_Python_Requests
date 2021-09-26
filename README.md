# О чем проект
Демонстрация работы с бесплатным API сайта https://petstore.swagger.io/#/

На данном сайте предоставлены различные задания для тренировки Мануальных тестировщиков.
Я автоматизировала выполнение данных заданий, используя *Python*, *Pytest* и *Request*.

Для работы нужен Python не ниже версии 3.5

# Для запуска тестов не через IDE: 
- клонировать этот проект
- перейти в папку с проектом
- создать и активировать виртуальное окружение:
  ```cmd 
    mkdir envir
    cd envir
    python -m venv rest_env
    rest_env/Scripts/activate.bat
  ```
- установить библиотеки для python (выполнять из корня проекта):
  ```python 
    pip install -r requirements.txt
- запустить тесты из одного файла можно командой (выполнять из корня проекта):
  ```python   
    pytest -v <project_dir>/tests/test_user.py 
  ```
- в конце работы деактивировать виртуальное окружение командой: 
  ```cmd
    deactivate
  ```

<br>


# What is the project about
Demonstration of working with the free site API https://petstore.swagger.io/#/

This site provides various tasks for training Manual testers.
I automated the execution of these tasks using *Python*, *Pytest* and *Request*.

To work, you need Python at least version 3.5

# To run tests without an IDE:
- clone this project
- go to the project folder
- create and activate a virtual environment:
```cmd
  mkdir envir
  cd envir
  python -m venv rest_env
  rest_env/Scripts/activate.bat
```
- install libraries for python (run from the project root):
```python
    pip install -r requirements.txt
```
- run tests from a single file with the command (run from the project root):
```python
    py test -v <project_dir>/tests/test_user.py
```
- at the end of the work, deactivate the virtual environment with the command:
```cmd
    deactivate
```