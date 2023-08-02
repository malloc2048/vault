from vault import app
from flask import render_template, redirect, url_for
from vault.models import category_details, get_category_counts, reload_data_files


@app.route('/')
def home():
    return render_template(
        'index.html',
        title='Home',
        categories=category_details(),
        counts=get_category_counts()
    )

@app.route('/reload/<page>', methods=['POST'])
def reload(page):
    endpoint, category = page.split('%')

    reload_data_files()

    if category:
        return redirect(url_for(endpoint, category=category))
    else:
        return redirect(url_for(endpoint))
