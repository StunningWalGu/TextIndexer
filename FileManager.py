


class TextIndex:

    _inst = None
    def __new__(cls, *args, **kwargs):
        if not cls._inst:
            cls._inst = super().__new__(cls, *args, **kwargs)
        return cls._inst

    def __init__(self, data = None):
        self._data = data

    def __del__(self):
        pass


    def _text_index(self) -> str | None:
        if self._data:
            print("whlie name . nasd\nㅁㄴㄴㅇ")
        else:
            pass
