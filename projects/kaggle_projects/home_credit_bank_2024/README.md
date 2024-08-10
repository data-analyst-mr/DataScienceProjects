# Оценка рисков по выполнению долговых обязательств

[Проект разработан в jupiter notebook.](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/kaggle_projects/home_credit_bank_2024/home_credit_bank_2024.ipynb)<br/>

## Описание проекта:
|   |  |
|---------------|-------------------|
|Заказчик| Home Credit Bank|
|Цель исследования| Создание модели оценки надежности заемщика|
|Используемые модели| CatBoost, LightGBM|
|Целевая метрика|stability metric = mean(gini) + 88,0 ⋅ min(0, a) − 0,5 ⋅ std(residuals), где<br/> Показатель gini рассчитывается для прогнозов, соответствующих каждому WEEK_NUM:<br/>gini = 2 ⋅ AUC − 1<br/>Линейная регрессия, а ⋅ х + b, проходит через недельные показатели gini, a falling_rate рассчитывается как min(0, а)|
|Общий вывод| Значение целевой метрики на тестовой выборке - 0.6131.<br/> Значение целевой метрики на приватных данных - 0.5151.|
|Навыки и инструменты|catboost,<br/>category_encoders,<br/>glob,<br/>hyperopt,<br/>lightgbm,<br/>numpy,<br/>pandas,<br/>pathlib,<br/>phik,<br/>polars,<br/>sklearn.|
|Статус проекта| Завершен|


[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)
