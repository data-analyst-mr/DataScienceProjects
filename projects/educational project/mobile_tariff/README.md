# Модель подбора оптимального тарифа

[Проект разработан в jupiter notebook.](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/mobile_tariff/mobil_tarif.ipynb)<br/>

## Описание проекта:
|   |  |
|---------------|-------------------|
|Заказчик| Оператор мобильной связи.|
|Цель исследования| Создание модели прогнозирования, способной по поведению пользователя определить максимально подходящий ему тариф: "Смарт" или "Ультра".|
|Требования к модели| Значение метрики Accuracy не должно быть менее 0.75.|
|Общий вывод|Метрики модели CatBoostClassifier на тестовой выборке:<br/>-Roc-Auc: 0.750;<br/>-Recall: 0.679;<br/>-F1: 0.652;<br/>-Accuracy: 0.777.<br/><br/>Accuracy для выбранной модели (0.777) выше, чем accuracy для "наивного" алгоритма (0.667), модель можно считать адекватной.<br/><br/>Условие заказчика - метрика accuracy не должна быть менее 0.75 - выполнено.<br/><br/>Наиболее важный в плане прогнозирования признак - израсходованный интернет-трафик.|
|Навыки и инструменты|Предобработка данных,<br/>catboost,<br/>math,<br/>matplotlib,<br/>numpy,<br/>optuna,<br/>pandas,<br/>python,<br/>sklearn,<br/>timeit.|
|Статус проекта| Завершен|


[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)


