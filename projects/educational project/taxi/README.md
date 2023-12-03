# Прогнозирование заказов такси

[Проект разработан в jupiter notebook.](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/taxi/taxi.ipynb)<br/>

## Описание проекта:
|   |  |
|---------------|-------------------|
|Заказчик| Компания "Чётенькое такси".|
|Цель исследования| Построить модель прогнозирования количества заказов такси в аэропортах на следующий час.|
|Требования к модели| Значение метрики RMSE на тестовой выборке должно быть не больше 48.|
|Общий вывод|Рассмотрены следующие модели:<br/>-LogisticRegression;<br/>-DecisionTreeClassifier;<br/>-RandomForestClassifier;<br/>-CatBoostClassifier.<br/><br/>Наилучшая модель по метрике RMSE - RandomForestRegressor.<br/>Метрики лучшей модели на тестовой выборке:<br/>-RMSE: 14.161;<br/>-время обучения: 242.1 сек.<br/><br/>Наиболее важные признаки для лучшей модели - значения, отстающее на 24, 48 и 72 часа.|
|Навыки и инструменты|catboost,<br/>imblearn,<br/>math,<br/>matplotlib,<br/>numpy,<br/>optuna,<br/>pandas,<br/>python,<br/>sklearn,<br/>statsmodels,<br/>timeit.|
|Статус проекта| Завершен|


[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)
