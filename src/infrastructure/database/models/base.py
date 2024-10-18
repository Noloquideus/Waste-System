from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join(f'{col.name}={getattr(self, col.name, None)!r}'
                               for col in self.__table__.columns)
        return f'<{class_name}({attributes})>'

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join(f'{col.name}={getattr(self, col.name)}'
                               for col in self.__table__.columns
                               if getattr(self, col.name) is not None)
        return f'{class_name}({attributes})'

