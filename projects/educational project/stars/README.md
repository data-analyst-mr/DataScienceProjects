# Прогнозирование температуры звезды

[Проект разработан в jupiter notebook.](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/stars/stars_temperature.ipynb)<br/>

## Описание проекта:
|   |  |
|---------------|-------------------|
|Заказчик| Обсерватория "Небо на ладони".|
|Цель исследования| Построить нейросеть, с помощью которой можно определить температуру на поверхности обнаруженных звёзд.|
|Требования к нейросети| Значение RMSE не должно превышать 4500.|
|Общий вывод|Архитектура базовой нейросети NeuralNetRegressor:<br/><class 'skorch.regressor.NeuralNetRegressor'>[initialized](<br/>  module_=Net(<br/>    (fc1): Linear(in_features=14, out_features=32, bias=True)<br/>    (act1): ReLU()<br/>    (dp1): Dropout(p=0, inplace=False)<br/>    (fc2): Linear(in_features=32, out_features=64, bias=True)<br/>    (act2): ReLU()<br/>    (dp2): Dropout(p=0, inplace=False)<br/>    (fc3): Linear(in_features=64, out_features=1, bias=True)<br/>    (act3): ReLU()<br/>    (flatten): Flatten(start_dim=0, end_dim=-1)<br/>  ),<br/>)<br/><br/>RMSE на обучающей выборке при кросс-валидации - 5204.336.<br/><br/>RMSE на тестовой выборке - 4310.033.|
|Навыки и инструменты|functools,<br/>matplotlib,<br/>numpy,<br/>pandas,<br/>python,<br/>seaborn,<br/>sklearn,<br/>torch.|
|Статус проекта| Завершен|


[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)
