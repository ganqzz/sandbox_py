from cars import Economy
from decorators import V6
from decorators import Vinyl
from decorators import Black


def main():
    car = Economy()
    show(car)
    car = V6(car)
    show(car)
    car = Vinyl(car)
    show(car)
    car = Black(car)
    show(car)


def show(car):
    print('Description: {}; cost: ${}'.format(car.description, car.cost))


if __name__ == '__main__':
    main()