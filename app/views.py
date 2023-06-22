from flask import render_template, request

from app.models import db, Brand, Product


def index_page():
    query = db.select(Brand).order_by(Brand.name)
    brands = db.session.execute(query).scalars()

    brand_id = request.args.get("brand")
    query = db.select(Product)
    if brand_id:
        query = query.filter_by(brand_id=brand_id)
    query = query.order_by(Product.model)
    products = db.session.execute(query).scalars()

    return render_template("index.html", brands=brands, products=products)


def product_page(product_id):
    product = db.get_or_404(Product, product_id)
    return render_template("product.html", product=product)
