# Бот для автосортировки анкет в телеграм-боте Дайвинчик
Данные юзербот сделан на основе библиотеки Pyrogram и позволяет лайкать/скипать анкеты по добавленным ключам(имя, описание).
## Установка
1. Скачать python3.
2. Установить зависимости <code>pip install -r requirements.txt</code>.
## Использование
1. Ввести в конфиг свой <code>api_id</code>, <code>api_hash</code> и свои ключи.
2. В консоли ввести номер телефона и код который придет в телеграм/смс.
3. Пить чай наблюдая за сортировкой анкет(нужно открыть сам телеграм).
По умолчанию бот пересылает лайкнутые анкеты в чат "Избранное".
Если Вас это как-то не устраивает, введите в файл конфига id(int) или username(str) чата который Вам нужен. (Для получения id групповых чатов добавьте любого бота для вывода id из поиска).
P.S. Этот юзербот не совершенен, есть много деталей над которыми можно посидеть.
