from p3vaildev.p3vaildev import app
from flask import render_template, redirect, url_for
# from p3vaildev.models import category_details, get_category_counts, reload_data_files


@app.route('/')
def home():
    return render_template(
        'index.html',
        title='Home',
        categories=list(),
        counts=dict()
    )
