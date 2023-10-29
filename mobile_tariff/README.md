# Модель подбора оптимального тарифа

[Проект разработан в jupiter notebook.](https://github.com/data-analyst-mr/data_science_projects/blob/main/mobile_tariff/mobil_tarif.ipynb)<br/>

## Описание проекта:
|   |  |
|---------------|-------------------|
|Заказчик| Оператор мобильной связи.|
|Цель исследования| Создание модели прогнозирования, способной по поведению пользователя определить максимально подходящий ему тариф: «Смарт» или «Ультра».|
|Требования к модели| Значение метрики Accuracy не должно быть менее 0.75.|
|Общий вывод|Рассмотрены следующие модели:<br/>-LogisticRegression;<br/>-DecisionTreeClassifier;<br/>-RandomForestClassifier;<br/>-CatBoostClassifier.<br/><br/>Модель с наибольшим значением ROC_AUC -RandomForestClassifier.<br/>Метрики лучшей модели на тестовой выборке:<br/>-Roc-Auc: 0.748;<br/>-Recall: 0.601;<br/>-F1: 0.654;<br/>-Accuracy: 0.805.<br/><br/>Наиболее важный в плане прогнозирования признак - израсходованный интернет-трафик.|
|Навыки и инструменты|Предобработка данных,<br/>Python,<br/>math,<br/>timeit,<br/>matplotlib,<br/>numpy,<br/>optuna<br/>pandas,<br/>catboost,<br/>optuna,<br/>sklearn.|
|Статус проекта| Завершен|


[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)
