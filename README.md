ldtp3
============

ldtp3 частично смержен из двух проектов: 
- https://github.com/ldtp/ldtp2 
- https://github.com/schuellerf/ldtp2/tree/python3

Также использовалась программа 2to3. 

ldtp3 является аналогом обычного ldtp2, но полностью переделан для 3 версии python. 

В ldtp3 вероятны ошибки. Вручную были исправлены регулярные выражения, строки, использующие вызов python 2-ой версии, вызовы устаревших библиотек и многое другое. Однако не все методы были проверены на работоспособность.

Большая часть функционала описана в официальном туториале ldtp, никаких глобально новых функций в ldtp3 проекте не добавлено (кроме функции getwindowbyaccessible для проекта [dogtail-ldtp](https://github.com/10Legend01/dogtail-ldtp)): \
https://github.com/ldtp/ldtp2/blob/master/doc/ldtp-tutorial.rst

Содержит в себе уникальную функцию для работы с изменённым dogtail: \
https://github.com/10Legend01/dogtail-ldtp

## Метод установки
```shell
sudo python3 setup.py build
sudo python3 setup.py install
```

Также для корректной работы необходимо установить:
- pyatspi (python-atspi)
- python-twisted-web
- python-wnck
- python-gnome

Для этого выполните следующие команды:
```shell
pip3 install twisted

sudo apt install python3-pyatspi
sudo apt install gir1.2-atspi-2.0
sudo apt install gir1.2-wnck-3.0 # Необязательно для запуска ldtp, но не будут доступны все возможности

sudo apt install gnome # необязательно, если две строчки снизу сработали
sudo apt install libglib2.0-bin
sudo gsettings set org.gnome.desktop.interface toolkit-accessibility true

sudo apt install python3-gi-cairo
sudo apt install python3-gi
```
Если какие-то команды не сработали, то некоторые зависимости библиотек были пропущены - apt либо сам подскажет что следует сделать, либо стоит поискать подсказки в интернете.
