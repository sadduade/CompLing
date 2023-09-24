# -*- coding: utf-8 -*-
import re
text = '''
Открытие белых карликов
Первым открытым белым карликом[3] стала звезда 40 Эридана B в тройной системе 40 Эридана, которую ещё в 1785 году Уильям Гершель включил в каталог двойных звёзд[4]. В 1910 году Генри Норрис Расселл обратил внимание на аномально низкую светимость 40 Эридана B при её высокой цветовой температуре, что и послужило впоследствии выделению подобных звёзд в отдельный класс белых карликов.

Вторым и третьим открытыми белыми карликами стали Сириус B и Процион B. В 1844 году директор Кёнигсбергской обсерватории Фридрих Бессель, анализируя данные наблюдений, которые велись с 1755 года, обнаружил, что Сириус, ярчайшая звезда земного неба, и Процион периодически, хотя и весьма слабо, отклоняются от прямолинейной траектории движения по небесной сфере[5]. Бессель пришёл к выводу, что у каждой из них должен быть близкий спутник. Сообщение было встречено скептически, поскольку слабый спутник оставался ненаблюдаемым, а его масса должна была быть достаточно велика — сравнимой с массой Сириуса и Проциона, соответственно.

В январе 1862 года Элвин Грэхэм Кларк, юстируя 18-дюймовый рефрактор, самый большой на то время телескоп в мире (Dearborn Telescope), впоследствии поставленный семейной фирмой Кларков в обсерваторию Чикагского университета, обнаружил в непосредственной близости от Сириуса тусклую звёздочку. Это был спутник Сириуса, Сириус B, предсказанный Бесселем[6]. А в 1896 году американский астроном Д. М. Шеберле открыл Процион B, подтвердив тем самым и второе предсказание Бесселя.

В 1915 году американский астроном Уолтер Сидней Адамс измерил спектр Сириуса B. Из измерений следовало, что его температура не ниже, чем у Сириуса A (по современным данным, температура поверхности Сириуса B составляет 25 000 K, а Сириуса A — 10 000 К), что, с учётом его в 10 000 раз меньшей, чем у Сириуса A, светимости указывает на очень малый радиус и, соответственно, высокую плотность — 106 г/см3 (плотность Сириуса ~0,25 г/см3, плотность Солнца ~1,4 г/см3).

В 1917 году Адриан ван Маанен открыл[7] ещё один белый карлик — звезду ван Маанена в созвездии Рыб.

В 1922 году Виллем Якоб Лейтен предложил называть такие звёзды "белыми карликами"[8].

Парадокс плотности

Диаграмма Герцшпрунга — Расселла
В начале XX века Герцшпрунгом и Расселлом была открыта закономерность в отношении спектрального класса (то есть температуры) и светимости звёзд — диаграмма Герцшпрунга — Расселла (Г—Р диаграмма). Казалось, что всё разнообразие звёзд укладывается в две ветви Г—Р диаграммы — главную последовательность и ветвь красных гигантов. В ходе работ по накоплению статистики распределения звёзд по спектральному классу и светимости Расселл обратился в 1910 году к профессору Эдуарду Пикерингу. Дальнейшие события Расселл описывает так[9]:

Я был у своего друга … профессора Э. Пиккеринга с деловым визитом. С характерной для него добротой он предложил получить спектры всех звёзд, которые Хинкс и я наблюдали … с целью определения их параллаксов. Эта часть казавшейся рутинной работы оказалась весьма плодотворной — она привела к открытию того, что все звёзды очень малой абсолютной величины (то есть низкой светимости) имеют спектральный класс M (то есть очень низкую поверхностную температуру). Как мне помнится, обсуждая этот вопрос, я спросил у Пиккеринга о некоторых других слабых звёздах…, упомянув, в частности, 40 Эридана B. Ведя себя характерным для него образом, он тут же отправил запрос в офис (Гарвардской) обсерватории, и вскоре был получен ответ (я думаю, от миссис Флеминг), что спектр этой звезды — A (то есть высокая поверхностная температура). Даже в те палеозойские времена я знал об этих вещах достаточно, чтобы сразу же осознать, что здесь имеется крайнее несоответствие между тем, что мы тогда назвали бы "возможными" значениями поверхностной яркости и плотности. Я, видимо, не скрыл, что не просто удивлён, а буквально сражён этим исключением из того, что казалось вполне нормальным правилом для характеристик звёзд. Пиккеринг же улыбнулся мне и сказал: "Именно такие исключения и ведут к расширению наших знаний" — и белые карлики вошли в мир исследуемого.

Удивление Расселла вполне понятно: 40 Эридана B относится к относительно близким звёздам, и по наблюдаемому параллаксу можно достаточно точно определить расстояние до неё и, соответственно, светимость. Светимость 40 Эридана B оказалась аномально низкой для её спектрального класса — белые карлики образовали новую область на Г—Р диаграмме. Такое сочетание светимости, массы и температуры было непонятно и не находило объяснения в рамках стандартной модели строения звёзд главной последовательности, разработанной в 1920-х годах Эддингтоном.

Высокая плотность белых карликов оставалась необъяснимой в рамках классической физики и астрономии и нашла объяснение лишь в рамках квантовой механики после появления статистики Ферми — Дирака. В 1926 году Фаулер в статье "О плотной материи"[10] показал, что, в отличие от звёзд главной последовательности, для которых уравнение состояния основывается на модели идеального газа (стандартная модель Эддингтона), для белых карликов плотность и давление вещества определяются свойствами вырожденного электронного газа (ферми-газа)[10].

В 1999—2000 годах галилеевы спутники наблюдала космическая обсерватория "Чандра", в результате чего было обнаружено рентгеновское излучение Европы и Ио. Вероятно, оно появляется при столкновении с их поверхностью быстрых ионов из магнитосферы Юпитера[121].

С декабря 1995 по сентябрь 2003 года систему Юпитера изучал автоматический зонд "Галилео". Из 35 витков аппарата вокруг Юпитера 12 были посвящены изучению Европы (максимальное сближение — 201 км)[122][123]. "Галилео" обследовал спутник довольно детально; были обнаружены новые признаки существования океана. В 2003 году "Галилео" был намеренно уничтожен в атмосфере Юпитера, чтобы в будущем неуправляемый аппарат не упал на Европу и не занёс на спутник земные микроорганизмы.'

Космический аппарат "Новые горизонты" в 2007 году, пролетая около Юпитера на пути к Плутону, сделал новые снимки поверхности Европы.

Аппарат "Юнона", запущенный 5 августа 2011 года НАСА, 29 сентября 2022 года пролетел на расстоянии 352 километров от поверхности Европы. На период 2022—2025 запланировано ещё 2 пролёта спутника.

14 апреля 2023 года состоялся запуск аппарата Jupiter Icy Moons Explorer (JUICE). Прибытие в систему Юпитера ожидается в 2031 году, и уже через год состоятся два пролёта Европы на расстоянии 400—500 километров над поверхностью, в ходе которых планируется осуществить сканирование поверхности, определить минимальную толщину ледяной корки спутника, а также выяснить максимальную глубины океана под ней.'''

a = re.sub(r'\([^)]*\)', '', text)
print(a)