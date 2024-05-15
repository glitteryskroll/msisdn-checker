# Запуск:

- Установка зависимостей pip install -r requirements.txt
- Инициализация БД phone_service из файла db.sql
- Готово

# Технологии:

- СУБД - PostgreSQL
- ЯП - Python
- Фреймворк - Django
- Тесты - PyTest
- Планировщик задач - schedule

# Сервис погоды

Главная страница доступна по маршруту `/def_number/`:

![image](https://github.com/glitteryskroll/phone_service/assets/55313356/6b139b85-bcbd-40f2-84e4-9d0f69f0d3f8)


На главной странице представлен поиск по номеру провайдера.

## API:

- **GET '/def_number'**: веб-страница с формой.
- **POST '/def_number/get_provider', body: formData{number: int} **: запрос для получения данных об провайдере.
- 
## Результат:
![image](https://github.com/glitteryskroll/phone_service/assets/55313356/9f6ae204-2a2b-49aa-8e38-1f183967cec5)
![image](https://github.com/glitteryskroll/phone_service/assets/55313356/e133f1f4-0f8f-4763-a171-4782a30da3bf)
![image](https://github.com/glitteryskroll/phone_service/assets/55313356/2b3f16f4-23df-4064-aec8-b5a1c56af167)
