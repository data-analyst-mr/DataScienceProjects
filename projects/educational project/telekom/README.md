# Телеком. Отток клиентов.

[Проект разработан в jupiter notebook.](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/telekom/telekom.ipynb)<br/>

## Описание проекта:
|   |  |
|---------------|-------------------|
|Заказчик| Оператор связи "ТелеДом".|
|Цель исследования| Построить модель прогнозирования оттока клиентов.|
|Описание услуг оператора связи| Оператор предоставляет два основных типа услуг:<br/>-Стационарную телефонную связь. Телефон можно подключить к нескольким линиям одновременно.<br/>Интернет. Подключение бывает двух типов: через телефонную линию DSL (англ. digital subscriber line — "цифровая абонентская линия") или оптоволоконный кабель (англ. fiber optic).<br/><br/>Также абонентам доступен ряд услуг:<br/>-Интернет-безопасность: антивирус (Device Protection) и блокировка опасных сайтов (Online Security);<br/>-Выделенная линия технической поддержки (Tech Support);<br/>-Облачное хранилище файлов для резервного копирования данных (Online Backup);<br/>-Стриминговое телевидение (Streaming TV) и каталог фильмов (Streaming Movies).<br/><br/>За услуги клиенты могут платить ежемесячно или раз в 1–2 года. Доступны различные способы расчёта и возможность получить электронный чек.|
|Требования к модели| Значение метрики ROC-AUC не должна быть менее 0,85 на тестовой выборке.|
|Общий вывод|Рассмотрены следующие модели:<br/>-RandomForestClassifier;<br/>-CatBoostClassifier;<br/>-NeuralNetClassifier.<br/><br/>Наибольшее значение метрики ROC-AUC имеет модель RandomForestClassifier.<br/>Метрики лучшей модели на тестовой выборке:<br/>-ROC-AUC: 0.85;<br/>-Recall: 0.792;<br/>-F1: 0.647;<br/>-Accuracy: 0.770.<br/><br/>Одним из важнейших признаков для данной модели является количество платежей.|
|Навыки и инструменты|python,<br/>datetime,<br/>numpy,<br/>optuna,<br/>pandas,<br/>matplotlib<br/>phik,<br/>seaborn,<br/>timeit,<br/>torch,<br/>catboost,<br/>imblearn,<br/>sklearn,<br/>skorch,<br/>sqlalchemy.|
|Статус проекта| Завершен|


[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)
