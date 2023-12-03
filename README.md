# Репозиторий проектов по Data Science

## Рабочие проекты курса Яндекс.Практикум.

## Описание проектов:
| Номер проекта | Название и ссылка | Заказчик| Цель исследования| Вывод| Стек| Статус|
|---------------|-------------------|------|------------------|-----|-----|-----|
|1             |[Прогнозирование стоимости покупки подержанного автомобиля](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/real_projects/workshop-1) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/real_projects/workshop-1/cars_cost.ipynb) | сервис по продаже подержаных автомобилей с аукциона| разработка и обучение ML-модели прогнозирования стоимости подержанного автомобиля и определение признаков, оказывающих наибольшее влияние на цену.| Используемая модель - CatBoostRegressor.<br/><br/>Значение MAPE на тестовой выборке для лучшей модели: 0.148.<br/><br/>Наибольший вес в стоимости автомобиля имеют признаки:<br/>- make;<br/>- model;<br/>- odometer.| Предобработка данных,<br/>catboost,<br/>dateparser,<br/>imblearn,<br/>math,<br/>matplotlib,<br/>optuna,<br/>phik,<br/>re,<br/>seaborn,<br/>swifter,<br/>sklearn,<br/>timeit.| Завершен|

[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)<br/>
<br/>
<br/>


## Учебные проекты курса Яндекс.Практикум.

## Описание проектов:
| Номер проекта | Название и ссылка | Заказчик| Цель исследования| Вывод| Стек| Статус|
|---------------|-------------------|------|------------------|-----|-----|-----|
|1             |[Определение возраста покупателей](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/age_of_buyers) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/age_of_buyers/age_of_buyers.ipynb) | Cетевой супермаркет| Cоздание модели прогнозирования, способной по фотографии определить возраст клиента.| Обучена модель из четырех слоев:<br/>ResNet50;<br/>GlobalAveragePooling2D;<br/>Dense;<br/>Dense.<br/><br/>Функция потерь - MSE.<br/>Метрика - МАЕ.<br/>Условие по значению MAE (не более 8) для тестовой выборки достигнуто на 6 эпохе обучения При этом переобучение не наблюдается.<br/>Значение MAE на 6 эпохе - 6.8948.| Предобработка данных,<br/>keras,<br/>numpy,<br/>pandas,<br/>python,<br/>seaborn,<br/>tensorflow.| Завершен|
|2             |[Стоимость жилья в Калифорнии](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/california_houses) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/california_houses/california_houses.ipynb)| Агенство недвижимости| Cоздание модели предсказания медианной стоимости дома в жилом массиве.| Модель LinearRegression обучена как на всех признаках, так и только на числовых.<br/><br/>Метрики модели, обученной на всех данных:<br/>-R2: 0.656;<br/>-RMSE: 68223.129;<br/>-MAE: 49725.965;<br/><br/>Метрики модели, обученной на числовых данных:<br/>-R2: 0.646;<br/>-RMSE: 69212.861;<br/>-MAE: 50866.560;<br/><br/>Метрики обоих моделей сопоставимы. При этом значение R2 выше у модели, обученной на всех данных, а RMSE и MAE - у модели, обученной только на числовых значениях.| Предобработка данных,<br/>numpy,<br/>pandas,<br/>pyspark,<br/>python,<br/>scipy.| Завершен|
|3             |[Прогнозирование риска возникновения ДТП](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/car_insurance) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/car_insurance/car_insurance.ipynb) | Каршеринговая компания| Создание модели оценики риска возникновения ДТП в зависимости от выбранного маршрута движения| В таблицах приведены данные по ДТП, по ним невозможно предсказать возможно ли избежать инцидента, так как данные по таковым исходам отсутствуют. Если до предоставленным данным предсказывать вероятность ДТП, то она составит 100%. Поскольку целевым признаком выбран at_fault (виновность участника), то результатом прогнозирования будет определение виновника ДТП. Это может быть полезно для контроля над финансовыми издержками, возникающими вследствие ДТП, но не для решения сформулированной в условиях задачи.<br/><br/>Наилучший результат по данной метрике показала модель RandomForestClassifier.<br/><br/>Метрики модели:<br/>-recall: 0.612618;<br/>-F1: 0.621;<br/>-auc_roc: 0.621;<br/>-время обучения (секунд): 36.91;<br/>-время предсказания (секунд): 0.09;| Предобработка данных,<br/>catboost,<br/>datetime,<br/>matplotlib,<br/>numpy,<br/>optuna,<br/>pandas,<br/>python,<br/>seaborn,<br/>sklearn,<br/>sqlalchemy,<br/>timeit.| Завершен|
|4              |[Cервис по продаже автомобилей с пробегом](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/cost_cars) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/cost_cars/coast_cars.ipynb)| Cервис по продаже автомобилей с пробегом| Создание модели прогнозирования рыночной стоимости автомобиля| Время обучения лучшей модели LGBMRegressor: 0.6 секунд.<br/><br/>На тестовой выборке данная модель показала следующие результаты:<br/>-RMSE: 1597;<br/>-R2: 0.877.<br/>-Время предсказания: 0.01 секунд.<br/><br/>Сравнение данной модели с dummy моделью показало ее адекватность.<br/>| Предобработка данных,<br/>datetime,<br/>lightgbm,<br/>numpy,<br/>pandas,<br/>python,<br/>seaborn,<br/>sklearn,<br/>timeit.| Завершен|
|5             |[Прогнозирование оттока клиентов в сети отелей "Как в гостях"](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/hotel) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/hotel/hotel.ipynb)| Сеть отелей «Как в гостях»| Создание модели прогнозирования отмены бронирования клиентами с целью внедрения для таковых системы списания депозита в случае снятия брони| Метрики модели CatBoostClassifier на тестовой выборке:<br/>-ROC-AUC: 0.745;<br/>-Recall: 0.715;<br/>-F1: 0.691;<br/>-Accuracy: 0.751.<br/><br/>Accuracy для выбранной модели (0.751) выше, чем accuracy для "наивного" алгоритма (0.612), модель можно считать адекватной.<br/><br/>Важнейшими признаками являются:<br/>-previous_cancellations - количество отменённых заказов у клиента;<br/>-country - гражданство постояльца;<br/>-lead_time - количество дней между датой бронирования и датой прибытия.<br/>| Предобработка данных,<br/>catboost,<br/>datetime,<br/>imblearn,<br/>matplotlib,<br/>numpy,<br/>optuna,<br/>pandas,<br/>python,<br/>scipy,<br/>seaborn,<br/>sklearn,<br/>timeit.| Завершен|
|6             |[Модель подбора оптимального тарифа](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/mobile_tariff) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/mobile_tariff/mobil_tarif.ipynb) | Оператор мобильной связи| Создание модели прогнозирования, способной по поведению пользователя определить максимально подходящий ему тариф: "Смарт" или "Ультра"| | Предобработка данных,<br/>catboost,<br/>math,<br/>matplotlib,<br/>numpy,<br/>optuna,<br/>pandas,<br/>python,<br/>sklearn,<br/>timeit.| Завершен|
|7             |[Выбор локации для скважины](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/oil_region) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/oil_region/oil_region.ipynb) | Добывающая компания «ГлавРосГосНефть»| Создание модели прогнозирования для определения региона, в котором добыча принесёт наибольшую прибыль| | Предобработка данных,<br/>matplotlib,<br/>numpy,<br/>pandas,<br/>python,<br/>scipy,<br/>seaborn,<br/>sklearn.| Завершен|
|8             |[Анализ постов на сервисе StackOverflow за 2008 год](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/posts) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/posts/posts.ipynb) | -| Провести анализ использования сервиса Stackoverflow за период с июля по декабрь 2008 года| | Предобработка данных,<br/>matplotlib,<br/>pandas,<br/>python,<br/>seaborn,<br/>SQL,<br/>sqlalchemy.| Завершен|
|9             |[Защита персональных данных клиентов](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/protection_of_personal_data) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/protection_of_personal_data/protection_of_personal_data%20.ipynb) | Страховая компания «Хоть потоп»| Обеспечить защищенность данных| | Предобработка данных,<br/>numpy,<br/>pandas,<br/>python,<br/>scipy,<br/>sklearn.| Завершен|
|10             |[Прогнозирование температуры звезды](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/stars) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/stars/stars_temperature.ipynb) |Обсерватория "Небо на ладони"| Построить нейросеть, с помощью которой можно определить температуру на поверхности обнаруженных звёзд| | Предобработка данных,<br/>functools,<br/>matplotlib,<br/>numpy,<br/>pandas,<br/>python,<br/>seaborn,<br/>sklearn,<br/>torch.| Завершен|
|11             |[Прогнозирование заказов такси](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/taxi) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/taxi/taxi.ipynb) | Компания "Чётенькое такси"| Построить модель прогнозирования количества заказов такси в аэропортах на следующий час| | Предобработка данных,<br/>catboost,<br/>imblearn,<br/>math,<br/>matplotlib,<br/>numpy,<br/>optuna,<br/>pandas,<br/>python,<br/>sklearn,<br/>statsmodels,<br/>timeit.| Завершен|
|12             |[Телеком. Отток клиентов.](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/telekom) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/telekom/telekom.ipynb) | Оператор связи "ТелеДом"| Построить модель прогнозирования оттока клиентов| | Предобработка данных,<br/>Python,<br/>datetime,<br/>numpy,<br/>optuna,<br/>pandas,<br/>matplotlib<br/>phik,<br/>seaborn,<br/>timeit,<br/>torch,<br/>catboost,<br/>imblearn,<br/>sklearn,<br/>skorch,<br/>sqlalchemy.| Завершен|
|13             |[Проект для "Викишоп" с BERT](https://github.com/data-analyst-mr/DataScienceProjects/tree/main/projects/educational%20project/wikishop) / [Ноутбук](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/wikishop/wikishop.ipynb) | Интернет-магазин "Викишоп"| Построить модель распознавания токсичных комментариев| | Предобработка данных,<br/>catboost,<br/>imblearn,<br/>matplotlib,<br/>numpy,<br/>optuna,<br/>pandarallel,<br/>pandas,<br/>python,<br/>re,<br/>sklearn,<br/>timeit,<br/>torch,<br/>tqdm,<br/>transformers,<br/>wordcloud.| Завершен|

[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)
