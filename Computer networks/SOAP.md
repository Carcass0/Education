Simple Object Access Protocol(SOAP) is a network protocol for exchanging structured data between nodes.

It uses XML format to transfer messages. It works on top of application layer protocols like HTTP and SMTP for notations and transmission. SOAP allows processes to communicate throughout platforms, languages and operating systems, since protocols like HTTP are already installed on all platforms.

**Envelope («конверт»).** Это корневой элемент. Определяет XML-документ как сообщение SOAP с помощью пространства имен _xmlns_soap=»http://www.w3.org/2003/05/soap-envelope/»._ Если в определении будет указан другой адрес, сервер вернет ошибку.

**Header («заголовок»).** Включает в себя атрибуты сообщения, связанные с конкретным приложением (аутентификация, проведение платежей и так далее). В заголовке могут использоваться три атрибута, которые указывают, как принимающая сторона должна обрабатывать сообщение, — _mustUnderstand_, _actor_ и _encodingStyle_**.** Значение _mustUnderstand_ — 1 или 0 — говорит принимающему приложению о том, следует ли распознавать заголовок в обязательном или опциональном порядке. Атрибут _actor_ задает конкретную конечную точку для сообщения. Атрибут _encodingStyle_ устанавливает специфическую кодировку для элемента. По умолчанию SOAP-сообщение не имеет определенной кодировки.

**Body («тело»).** Сообщение, которое передает веб-приложение. Может содержать запрос к серверу или ответ от него. Пример сообщения, которое запрашивает стоимость ноутбука в онлайн-магазине:

```
<?xml version="1.0"?> 
<soap:Envelope xmlns_soap="http://www.w3.org/2003/05/soap-envelope/" soap_encodingStyle="http://www.w3.org/2003/05/soap-encoding"> 
<soap:Body> 
<m:GetPrice xmlns_m="https://online-shop.ru/prices">
<m:Item>Dell Vostro 3515-5371</m:Item>
</m:GetPrice>
</soap:Body>
</soap:Envelope>_
```

Пример ответа сервера онлайн-магазина:

```
_<?xml version="1.0"?>
<soap:Envelope xmlns_soap="http://www.w3.org/2003/05/soap-envelope/" soap_encodingStyle="http://www.w3.org/2003/05/soap-encoding"> 
<soap:Body> 
<m:GetPriceResponse xmlns_m="https://online-shop.ru/prices"> <m:Price>37299</m:Price> 
</m:GetPriceResponse> 
</soap:Body> 
</soap:Envelope>_
```

**Fault** **(«ошибка»)**. Опциональный элемент. Передает уведомление об ошибках, если они возникли в ходе обработки сообщения. Может содержать вложенные элементы, которые проясняют причину возникновения ошибки:

- faultcode — код неполадки;
- faultstring — «человекопонятное» описание проблемы;
- faultactor — информация о программном компоненте, который вызвал ошибку;
- detail — дополнительные сведения о месте возникновения неполадки.