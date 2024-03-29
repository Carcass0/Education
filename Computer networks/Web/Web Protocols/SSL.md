## Работа Secure Sockets Layer (SSL): рукопожатие

Работа SSL-протокола базируется на нескольких этапах:

1. **Установка соединения.** Клиент отправляет запрос на установку безопасного соединения с сервером. 
2. **Запрос на сертификат.** Сервер отвечает клиенту, отправляя свой цифровой сертификат, который содержит открытый ключ и информацию о сервере.
3. **Проверка сертификата.** Клиент проверяет подлинность сертификата с помощью центра сертификации. 
4. **Key exchange.** Клиент генерирует симметричные ключи шифрования и осуществляет их передачу с помощью открытого ключа сервера.
5. **Шифрование данных.** Сервер расшифровывает симметричные ключи с помощью закрытого ключа и использует для шифрования данных, которые затем отправляет клиенту.
6. **Расшифровка данных.** Клиент использует симметричные ключи для расшифровки данных, полученных от сервера.

