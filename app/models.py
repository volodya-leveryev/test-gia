from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product', back_populates="brand")

    def __str__(self):
        return self.name


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id', name="Brand"), nullable=False)
    brand = db.relationship('Brand', back_populates="products")
    model = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text())
    photo_small = db.Column(db.String(50))
    photo_large = db.Column(db.String(50))
