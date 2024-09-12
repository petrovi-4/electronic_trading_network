# Торговая сеть электроники
Данный проект является веб-приложением с API интерфейсом и админ-панелью, 
цель которого - управление торговой сетью электроники. 

Сеть представлять собой иерархическую структуру из 3 уровней: 
- завод, 
- розничная сеть, 
- индивидуальный предприниматель. 

В приложении реализован функционал управления компаниями и продуктами, которые они продают.

## Технологии использованные в проекте
- Python 3.12
- Django 5.0.1
- DRF 3.14.0
- PostgreSQL

## Инструкция по развертыванию проекта
**Клонировать репозиторий:**

```
git@github.com:petrovi-4/electronic_trading_network.git
```

**Создать и активировать виртуальное окружение:**

```
python3 -m venv env         (для Unix-систем)
source env/bin/activate     (для Windows-систем)
```
```
python -m venv env          (для Unix-систем)
env/Scripts/activate.bat    (для Windows-систем)
```

**Настройка окружения**

Создайте файл `.env` на основе примера `.env_sample` и заполните его необходимыми данными

```
cp .env_sample .env
```

**Установка зависимостей из файла requirements.txt:**

```
python3 -m pip install --upgrade pip    (для Unix-систем)
python -m pip install --upgrade pip     (для Windows-систем)
```
```
pip install -r requirements.txt
```

**Выполнить миграции:**

```
python3 manage.py migrate   (для Unix-систем) 
python manage.py migrate    (для Windows-систем)
```

**Запуск проекта:**

```
python3 manage.py runserver (для Unix-систем)
python manage.py runserver  (для Windows-систем)
```


### **Документация API:**

```
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```

**Автор**  
[Мартынов Сергей](https://github.com/petrovi-4)

![GitHub User's stars](https://img.shields.io/github/stars/petrovi-4?label=Stars&style=social)
![licence](https://img.shields.io/badge/licence-GPL--3.0-green)