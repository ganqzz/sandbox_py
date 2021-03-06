"""
Demonstrate object implementation and custom attributes using a simple 2D vector.
"""


class Vector:
    """Simple 2D vector"""

    def __init__(self, **coords):
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name):
        private_name = '_' + name
        try:
            return self.__dict__[private_name]  # hasattrは使わない（recursive）
        except KeyError:
            raise AttributeError(
                '{!r} object has no attribute {!r}'.format(self.__class__.__name__, name))

    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute {!r}".format(name))

    def __delattr__(self, name):
        raise AttributeError("Can't delete attribute {!r}".format(name))

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__,
                               ', '.join("{k}={v}".format(k=k[1:], v=self.__dict__[k])
                                         for k in sorted(self.__dict__.keys())))


class ColoredVector(Vector):
    """Colored 2D vector"""

    COLOR_INDEXES = ('red', 'green', 'blue')

    def __init__(self, red, green, blue, **coords):
        super().__init__(**coords)
        self.__dict__['color'] = [red, green, blue]

    def __getattr__(self, name):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            return super().__getattr__(name)
        else:
            return self.__dict__['color'][channel]

    def __setattr__(self, name, value):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            super().__setattr__(name, value)
        else:
            self.__dict__['color'][channel] = value

    def __repr__(self):
        keys = set(self.__dict__.keys())
        keys.discard('color')
        coords = ', '.join(
            "{k}={v}".format(k=k[1:], v=self.__dict__[k])
            for k in sorted(keys))

        return "{cls}({red}, {green}, {blue}, {coords})".format(
            cls=self.__class__.__name__,
            red=self.red,
            green=self.green,
            blue=self.blue,
            coords=coords)


if __name__ == '__main__':
    v = Vector(p=9, q=3)
    print(v)
    print(dir(v))
    print(v._p)
    # v.p = 7  # forbidden
    # v._p = 16  # forbidden
    print(v.p)
    print(v._p)
    # print(v.x)  #
    # delattr(v , '_p')  # forbidden

    print()
    cv = ColoredVector(red=23, green=44, blue=238, p=9, q=14)
    print(cv)
