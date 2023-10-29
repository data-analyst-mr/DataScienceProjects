# Прогнозирование температуры звезды

[Проект разработан в jupiter notebook.](https://github.com/data-analyst-mr/data_science_projects/blob/main/stars/stars_temperature.ipynb)<br/>

## Описание проекта:
|   |  |
|---------------|-------------------|
|Заказчик| Обсерватория "Небо на ладони".|
|Цель исследования| Построить нейросеть, с помощью которой можно определить температуру на поверхности обнаруженных звёзд.|
|Требования к нейросети| Значение RMSE не должно превышать 4500.|
|Общий вывод|Рассмотрены следующие модели:<br/>-LogisticRegression;<br/>-DecisionTreeClassifier;<br/>-RandomForestClassifier;<br/>-CatBoostClassifier.<br/><br/>Модель с наибольшим значением ROC_AUC -RandomForestClassifier.<br/>Метрики лучшей модели на тестовой выборке:<br/>-Roc-Auc: 0.748;<br/>-Recall: 0.601;<br/>-F1: 0.654;<br/>-Accuracy: 0.805.<br/><br/>Наиболее важный в плане прогнозирования признак - израсходованный интернет-трафик.|
|Навыки и инструменты|Предобработка данных,<br/>Python,<br/>numpy,<br/>pandas,<br/>seaborn,<br/>matplotlib,<br/>torch<br/>functools,<br/>sklearn.|
|Статус проекта| Завершен|


[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)
