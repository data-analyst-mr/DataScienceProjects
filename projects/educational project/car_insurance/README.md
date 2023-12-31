# Прогнозирование риска возникновения ДТП

[Проект разработан в jupiter notebook.](https://github.com/data-analyst-mr/DataScienceProjects/blob/main/projects/educational%20project/car_insurance/car_insurance.ipynb)<br/>

## Описание проекта:
|   |  |
|---------------|-------------------|
|Заказчик| Каршеринговая компания.|
|Цель исследования| Создание модели оценки риска возникновения ДТП в зависимости от выбранного маршрута движения.|
|Идея решения задачи от заказчика|Создать модель предсказания ДТП (целевое значение — at_fault (виновник) в таблице parties)<br/>-Для модели выбрать тип виновника — только машина (car).<br/>-Выбрать случаи, когда ДТП привело к любым повреждениям транспортного средства, кроме типа SCRATCH (царапина).<br/>-Для моделирования ограничиться данными за 2012 год — они самые свежие.<br/>-Обязательное условие — учесть фактор возраста автомобиля.<br/><br/>На основе модели исследовать основные факторы ДТП.<br/>Понять, помогут ли результаты моделирования и анализ важности факторов ответить на вопросы:<br/>-Возможно ли создать адекватную системы оценки водительского риска при выдаче авто?<br/>-Какие ещё факторы нужно учесть?<br/>-Нужно ли оборудовать автомобиль какими-либо датчиками или камерой?|
|Требования к модели| -|
|Общий вывод|В таблицах приведены данные по ДТП, по ним невозможно предсказать возможно ли избежать инцидента, так как данные по таковым исходам отсутствуют. Если до предоставленным данным предсказывать вероятность ДТП, то она составит 100%. Поскольку целевым признаком выбран at_fault (виновность участника), то результатом прогнозирования будет определение виновника ДТП. Это может быть полезно для контроля над финансовыми издержками, возникающими вследствие ДТП, но не для решения сформулированной в условиях задачи.<br/><br/>Для решения поставленной задачи модель должна эффективно определять положительный класс: нужно выявить максимальное количество потенциальных виновников ДТП. При этом не имеет значения, будут ли ошибки в отношении клиентов, не представляющих угрозу. В связи с этим для оценки качества модели выбрана метрика Recall.<br/><br/>Наилучший результат по данной метрике показала модель RandomForestClassifier.<br/><br/>Метрики модели:<br/>-recall: 0.612;<br/>-F1: 0.621;<br/>-auc_roc: 0.621;<br/>-время обучения (секунд): 36.91;<br/>-время предсказания (секунд): 0.09;|
|Навыки и инструменты|Предобработка данных,<br/>catboost,<br/>datetime,<br/>matplotlib,<br/>numpy,<br/>optuna,<br/>pandas,<br/>python,<br/>seaborn,<br/>sklearn,<br/>sqlalchemy,<br/>timeit.|
|Статус проекта| Завершен|


[Email](mailto:mikhail-shestakov-2022@bk.ru)<br/>
[Telegram](https://t.me/mshestakov1)
