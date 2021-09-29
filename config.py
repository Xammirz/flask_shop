from os.path import join, dirname, realpath
class Config():
    SECRET_KEY = 'FJHiuhdkjfhjGiuGiGUG'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shop.db'
    SQLALCHEMY_TRACK_MODIFICATION = False
    UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'shop/static/img/product/')