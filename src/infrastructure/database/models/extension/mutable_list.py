from sqlalchemy.ext.mutable import Mutable


class MutableList(Mutable, list):
    def append(self, value):
        super().append(value)
        self.changed()

    def pop(self, index=0):
        value = super().pop(index)
        self.changed()
        return value

    @classmethod
    def coerce(cls, key, value):
        if not isinstance(value, MutableList):
            if isinstance(value, list):
                return MutableList(value)
            return Mutable.coerce(key, value)
        else:
            return value

    def __setitem__(self, index, value):
        super().__setitem__(index, value)
        self.changed()

    def __delitem__(self, index):
        super().__delitem__(index)
        self.changed()

    def extend(self, iterable):
        super().extend(iterable)
        self.changed()

    def insert(self, index, value):
        super().insert(index, value)
        self.changed()

    def remove(self, value):
        super().remove(value)
        self.changed()
