# Определение возраста покупателей

[Проект разработан в jupiter notebook.](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/age_of_buyers/age_of_buyers.ipynb)<br/>

## Описание проекта:
|   |  |
|---------------|-------------------|
|Заказчик | Cетевой супермаркет|
|Цель исследования| Cоздание модели прогнозирования, способной по фотографии определить возраст клиента.|
|Требования к модели| Значение метрики MAE на тестовой выборке не должно превышать 0.8.|
|Общий вывод|Обучена модель из четырех слоев:<br/>ResNet50;<br/>GlobalAveragePooling2D;<br/>Dense;<br/>Dense.<br/><br/>Функция потерь - MSE.<br/>Метрика - МАЕ.<br/>Условие по значению MAE (не более 8) для тестовой выборки достигнуто на 6 эпохе обучения При этом переобучение не наблюдается.<br/>Значение MAE на 6 эпохе - 6.8948.|
|Навыки и инструменты|keras,<br/>numpy,<br/>pandas,<br/>python,<br/>seaborn,<br/>tensorflow.|
|Статус проекта| Завершен|


[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)
