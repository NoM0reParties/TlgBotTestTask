import peewee

db = peewee.SqliteDatabase('bakery_users.db')


class Condition(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db


class BakeryUser(peewee.Model):
    user_id = peewee.CharField()
    condition = peewee.ForeignKeyField(Condition, related_name='cond')

    class Meta:
        database = db


class ShowcaseModel(peewee.Model):
    name = peewee.CharField()
    picture_path = peewee.CharField()
    description = peewee.CharField()

    class Meta:
        database = db


class SectionModel(peewee.Model):
    name = peewee.CharField()
    picture_path = peewee.CharField()
    description = peewee.CharField()
    showcase = peewee.ForeignKeyField(ShowcaseModel)

    class Meta:
        database = db


class GoodsModel(peewee.Model):
    name = peewee.CharField()
    picture_path = peewee.CharField()
    description = peewee.CharField()
    section = peewee.ForeignKeyField(SectionModel)

    class Meta:
        database = db

