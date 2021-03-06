class Singleton(object):
    __instance = None

    def __new__(cls):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        return Singleton.__instance

    def __init__(self):
        print('Singleton.__init__')


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    assert s1 is s2

    s1.ans = 42

    assert s2.ans == s1.ans
    print('Assertions passed.')
