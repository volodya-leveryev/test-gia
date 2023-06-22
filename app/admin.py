from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.models import db, Brand, Product

admin = Admin()
admin.add_view(ModelView(Brand, db.session))
admin.add_view(ModelView(Product, db.session))
