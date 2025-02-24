import doctest


class Radiator:

    def __init__(self, max_temp: float, min_temp: float, current_temp: float, applied: bool):
        """
        Создание и подготовка к работе класса "Обогреватель"

        :param max_temp: максимальная температура
        :param min_temp: температура в выключенном состоянии
        :param current_temp: текущая температура
        :param applied: подключен ли к сети
        Пример:
        >>> radiator = Radiator(80, 20, 25, True)
        """
        if not isinstance (max_temp, (int, float)):
            raise TypeError('Максимальная температура должна быть типа int или float')
        if max_temp < 0:
            raise ValueError('Максимальная температура должна быть больше 0')
        self.max_temp = max_temp
        if not isinstance (min_temp, (int, float)):
            raise TypeError('Минимальная температура должна быть типа int или float')
        if min_temp < 0:
            raise ValueError('Минимальная температура должна быть больше 0')
        self.min_temp = min_temp
        if not isinstance (current_temp, (int, float)):
            raise TypeError('Текущая температура должна быть типа int или float')
        if current_temp > max_temp or current_temp < min_temp:
            raise ValueError('Текущая температура должна быть меньше/равна максимальной температуры и больше/равна минимальной')
        self.current_temp = current_temp
        if not isinstance(applied, bool):
            raise TypeError('Подключение к сети должно быть типа bool')
        self.applied = applied

    def is_working(self) -> bool:
        """
        Функция, которая проверяет, работает ли обогреватель

        :return: Работает ли обогреватель

        Примеры:
        >>> radiator = Radiator(80, 20, 25, True)
        >>> radiator.is_working()
        True
        """
        if self.applied and self.current_temp != self.min_temp:
            return True
        else:
            return False

    def turn_on(self) -> None:
        """
        Включение.
        :raise ValueError: Невозможно включить уже включенный радиатор
        Примеры:
        >>> radiator = Radiator(80, 20, 25, False)
        >>> radiator.turn_on()
        """
        if self.applied:
            raise ValueError('Радиатор уже включен')
        self.applied = True

    def turn_off(self) -> None:
        """
        Выключение.
        :raise ValueError: Невозможно выключить уже выключенный радиатор
        Примеры:
        >>> radiator = Radiator(80, 20, 25, True)
        >>> radiator.turn_off()
        """
        if not self.applied:
            raise ValueError('Радиатор уже выключен')
        self.applied = False
        self.current_temp = self.min_temp

    def heat_up(self, degrees: float) -> None:
        """
        Разогрев радиатора.
        :param degrees: на сколько подогреваем

        :raise ValueError: Нельзя нагреть до температуры больше максимальной
        :raise AssertionError: Нельзя нагреть отключенный от сети радиатор
        Примеры:
        >>> radiator = Radiator(80, 20, 25, True)
        >>> radiator.heat_up(20)
        """
        if not isinstance (degrees, (int, float)):
            raise TypeError('Число градусов, на которое нагреваем, должно быть типа int или float')
        if self.current_temp+degrees > self.max_temp:
            raise ValueError('Нельзя нагреть больше максимальной температуры')
        if not self.is_working():
            raise AssertionError('Радиатор не подключен к сети. Сначала включите радиатор')
        self.current_temp += degrees

    def cool_down(self, degrees: float) -> None:
        """
        Охлаждение радиатора.
        :param degrees: на сколько охлаждаем

        :raise ValueError: Нельзя охладить до температуры меньше минимальной
        :raise AssertionError: Нельзя охладить отключенный от сети радиатор
        Примеры:
        >>> radiator = Radiator(80, 20, 40, True)
        >>> radiator.cool_down(5)
        """
        if not isinstance (degrees, (int, float)):
            raise TypeError('Число градусов, на которое нагреваем, должно быть типа int или float')
        if self.current_temp-degrees < self.min_temp:
            raise ValueError('Нельзя нагреть меньше минимальной температуры')
        if not self.is_working():
            raise AssertionError('Радиатор не подключен к сети. Сначала включите радиатор')
        self.current_temp -= degrees


WIDTH = 200
HEIGHT = 200


class Ball:
    def __init__(self, radius: float, x: float, y: float, color: tuple):
        """
        Создание и подготовка к работе класса "Шарик" в компьютерной игре.
        Координаты на экране отсчитываются от центра

        :param radius: радиус
        :param x: координата x
        :param y: координата у
        :param color: цвет

        Пример:
        >>> ball = Ball(10, 0, 0, (0, 255, 0))
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('Радиус должен быть типа int или float')
        if radius < 0:
            raise ValueError('Радиус должен быть положительным числом')
        self.radius = radius
        if not isinstance(x, (int, float)):
            raise TypeError('Координата х должна быть типа int или float')
        self.x = x
        if not isinstance(y, (int, float)):
            raise TypeError('Координата y должна быть типа int или float')
        self.y = y
        if not isinstance(color, tuple):
            raise TypeError('Цвет должен быть типа tuple')
        self.color = color

    def outOfScreen(self) -> bool:
        """
        Метод проверки, вышел ли шарик за пределы экрана.
        Использует глобальные переменные WIDTH, HEIGHT - ширина и высота окна приложения

        :return: выходит ли за пределы экрана

        Примеры:
        >>> ball = Ball(10, 0, 0, (0, 255, 0))
        >>> ball.outOfScreen()
        False
        """
        global WIDTH, HEIGHT
        if not isinstance(WIDTH, (int, float)):
            raise TypeError('Ширина должна быть типа int или float')
        if WIDTH < 0:
            raise ValueError('Ширина должна быть положительным числом')
        if not isinstance(HEIGHT, (int, float)):
            raise TypeError('Высота должна быть типа int или float')
        if HEIGHT < 0:
            raise ValueError('Высота должна быть положительным числом')
        if self.x + self.radius > WIDTH / 2 or self.x-self.radius < -(WIDTH / 2):
            return True
        elif self.y + self.radius > HEIGHT / 2:
            return True
        else:
            return False

    def move(self, x: float = 0.0, y: float = 0.0) -> None:
        """
        Метод перемещения шарика по экрану.

        :param x: Изменение по оси х
        :param y: Изменение по оси y

        Примеры:
        >>> ball = Ball(10, 0, 0, (0, 255, 0))
        >>> ball.move(10, 10)
        """
        if not isinstance(x, (int, float)):
            raise TypeError('Перемещение х должно быть типа int или float')
        if not isinstance(y, (int, float)):
            raise TypeError('Перемещение y должно быть типа int или float')
        global WIDTH, HEIGHT
        if not self.outOfScreen():
            self.x += x
            self.y += y


class Gearbox:
    def __init__(self, engineTorque: float, engineSpeed: float, gearset: tuple):
        """
        Создание и подготовка к работе класса "Коробка передач автомобиля"

        :param engineTorque: Крутящий момент двигателя
        :param engineSpeed: Скорость вращения вала двигателя
        :param gearset: Передаточные числа передач коробки
        :param current_gear: Текущая передача (по умолчанию 1, передаточное = 0)

        Примеры:
        >>> gearbox1 = Gearbox(300, 1500, (-3.5, 0.0, 3.5, 2.6, 1.0))
        """
        if not isinstance(engineTorque, (int, float)):
            raise TypeError('Крутящий момент должен быть типа int или float')
        if engineTorque < 0:
            raise ValueError('Крутящий момент должен быть больше 0')
        self.engineTorque = engineTorque
        if not isinstance(engineSpeed, (int, float)):
            raise TypeError('Скорость двигателя должна быть типа int или float')
        if engineSpeed < 0:
            raise ValueError('Скорость двигателя должна быть больше 0')
        self.engineSpeed = engineSpeed
        if not isinstance(gearset, tuple):
            raise TypeError('Передаточные числа передач должны быть представлены типом tuple')
        for i in gearset:
            if not isinstance(i, (int, float)):
                raise TypeError('Передаточное число должно быть типа float')
        self.gearset = gearset
        self.current_gear = 1

    def switch_up(self) -> None:
        """
        Переключение передачи "вверх"

        :raise ValueError: Нельзя переключаться выше последней передачи

        Примеры:
        >>> gearbox1 = Gearbox(300, 1500, (-3.5, 0.0, 3.5, 2.6, 1.0))
        >>> gearbox1.switch_up()
        """
        if self.current_gear > 3:
            raise ValueError('Вы - на максимальной передаче')
        self.current_gear += 1

    def switch_down(self) -> None:
        """
        Переключение передачи "вниз"

        :raise ValueError: Нельзя переключаться ниже передачи заднего хода

        Примеры:
        >>> gearbox1 = Gearbox(300, 1500, (-3.5, 0.0, 3.5, 2.6, 1.0))
        >>> gearbox1.switch_down()
        """
        if self.current_gear < 0:
            raise ValueError('Вы - на минимальной передаче')
        self.current_gear -= 1
        
    def neutral(self) -> None:
        """
        Переключение в нейтраль

        Примеры:
        >>> gearbox1 = Gearbox(300, 1500, (-3.5, 0.0, 3.5, 2.6, 1.0))
        >>> gearbox1.neutral()
        """
        self.current_gear = 0

    def calculate_torque(self) -> float:
        """
        Функция подсчета крутящего момента на выходном валу коробки.

        :return: Значение крутящего момента

        Примеры:
        >>> gearbox1 = Gearbox(300, 1500, (-3.5, 0.0, 3.5, 2.6, 1.0))
        >>> gearbox1.calculate_torque()
        0.0
        """
        return self.engineTorque * self.gearset[self.current_gear]

    def calculate_speed(self) -> float:
        """
        Функция подсчета скорости выходного вала.

        :return: значение скорости

        Примеры:
        >>> gearbox1 = Gearbox(300, 1500, (-3.5, 0.0, 3.5, 2.6, 1.0))
        >>> gearbox1.calculate_speed()
        0.0
        """
        try:
            return self.engineSpeed / self.gearset[self.current_gear]
        except ZeroDivisionError:
            return 0.0



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmode()
