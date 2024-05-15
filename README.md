# Запуск:

- Установка зависимостей pip install -r requirements.txt
- Инициализация БД phone_service из файла db.sql
- Запуск парсера schedule.py фоном
- Готово

# Технологии:

- СУБД - PostgreSQL
- ЯП - Python
- Фреймворк - Django
- Тесты - PyTest
- Планировщик задач - schedule

# Сервис погоды

Главная страница доступна по маршруту `/def_number/`:

![image](https://github.com/glitteryskroll/phone_service/assets/55313356/4a4d2cbc-d9cb-484e-9ed9-671b93d38395)
<br/>На главной странице представлен поиск по номеру провайдера.
## API:

- **GET '/def_number'**: веб-страница с формой.
- **POST '/def_number/get_provider', body: formData{number: int} **: запрос для получения данных об провайдере.
## Результат:
![image](https://github.com/glitteryskroll/phone_service/assets/55313356/9f6ae204-2a2b-49aa-8e38-1f183967cec5)
<br/>
![image](https://github.com/glitteryskroll/phone_service/assets/55313356/d9411149-f134-46cf-b9df-e23a917639c4)
<br/>
![image](https://github.com/glitteryskroll/phone_service/assets/55313356/8a72e869-aacb-4fff-9664-bbd5576f3d44)
<br/>
![image](https://github.com/glitteryskroll/phone_service/assets/55313356/9828b596-1f4f-456c-838d-e676ba916089)


