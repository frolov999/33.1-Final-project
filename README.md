# Task-33.1_Final_Project
Тестирование формы авторизации сайта Ростелеком по предоставленным требованиям.

В рамках выполнения проекта предстоит протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии по предоставленным [требованиям](https://docs.google.com/document/d/1CF79p-e0BSFQXz4yn7LKZdMLWWu57gKTyMCwMZdys7I/edit?usp=sharing) к сайту.

Объект тестирования: https://b2c.passport.rt.ru


## Задание:
- Протестировать требования;
- Разработать тест-кейсы (не менее 15);
- Провести автоматизированное тестирование продукта (по одному автотесту на каждый тест-кейс); 
- Описать обнаруженные дефекты.

## Выполнение проекта:

1. Протестированы требования;

Ссылка на документ: https://docs.google.com/spreadsheets/d/1Upg0JQX2lQcMhfJw0jVUOcUxQq2kMN8Wfw-RV__y3KM/edit?usp=sharing
   
2. Разработаны  тест-кейсы (более 15);

Ссылка на документ: https://docs.google.com/spreadsheets/d/1HIaCLZP6bdlwvECe8mcy8t7pSe_U9-C9kGQZvHC1wbA/edit?usp=sharing
   
3. Оформлено описание обнаруженных дефектов; 

Ссылка на документ: https://docs.google.com/spreadsheets/d/1gE53gcYgsWyJeKK5YluAUB3cZnHWcG9LOG7rHQOQYI0/edit?usp=sharing

4. Проект выполнен с использованием: PageObject, Selenium и PyTest;

5. В корневой папке находятся файлы settings.py с тестовыми данными, chromedriver.exe, requirements.txt для установки необходимых для тестирования библиотек;

6. В корне проекта в файле conftest.py находится фикстура с функцией открытия и закрытия браузера.

7. Папка tests содержит файлы для запуска автотестов: test_auth_page.py - тесты для страницы авторизация, test_registr_page.py - тесты для страницы регистрация.

Папка pages содержит следующие файлы: locators.py - список локаторов на веб странице, base_page.py - базовая страница, от которой унаследованы все остальные классы, auth_page.py - содержит класс для страницы авторизация, registr_page.py - содержит класс для страницы регистрация.

Перед запуском тестов требуется установить необходимые библиотеки командой:

pip install -r requirements.txt 

Запуск тестов при помощи команд в консоли:

python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py 

python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_registr_page.py 

Сценарии проверок автотестами: Каждый тест внутри проекта содержит описание своего назначения.

Тестовые сценарии страницы авторизация (test_auth_page.py):
Проверка различных элементов страницы на их наличие и название согласно требованию. Проверка табов меню авторизация. При переходе по ссылкам "Забыл пороль" и "Зарегистрироваться" открываются соответствующие страницы. Проверка аутентификации пользователя с валидными и невалидными данными. Тестовые сценарии страницы регистрация (test_registr_page.py):

Проверка различных элементов страницы на их наличие и название согласно требованию. Сценарии регистрации пользователя с валидными данными ("Имя" и "Фамилия" - буквы кириллицы либо тире). Сценарии регистрации пользователя с данными, которы были использованы ранее. Проверки полей ввода валидными и невалидными данными.
