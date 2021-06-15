# Вас привествует detection_bot

## Описание

В данный телеграм бот встроена обученная модель, которая позволяет определять объекты на изображении. Принцип работы
простой: телеграм боту отправляется изображение, затем после нескольких секунд ожидания бот отвечает тем же
изображением, но уже с выделенными объектами на нём.

## Установка
```
$ git init
$ git clone https://github.com/Domochevskyy/practice_telegram_bot.git
$ cd practice_telegram_bot
$ pip install -r requiremenst.txt
```
А также в каталог проекта нужно добавить саму модель нейронной сети, которую можно скачать вот тут:
```
https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5
```


