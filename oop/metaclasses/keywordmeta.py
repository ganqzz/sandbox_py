class KeywordsOnlyMeta(type):

    def __call__(cls, *args, **kwargs):
        if args:
            raise TypeError(
                "Constructor for class {!r} does not accept positional arguments.".format(cls))
        return super().__call__(cls, **kwargs)


class ConstrainedToKeywords(metaclass=KeywordsOnlyMeta):

    def __init__(self, *args, **kwargs):
        print("args =", args)
        print("kwargs =", kwargs)


if __name__ == '__main__':
    c1 = ConstrainedToKeywords(keyword="Yama")
    c2 = ConstrainedToKeywords("Kawa", keyword="Yama")  # NG
