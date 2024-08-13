from p3vaildev import app
from p3vaildev.models import users, nodes
from flask import render_template, redirect, url_for, request


@app.route('/')
def home():
    return render_template(
        'index.html',
        title='Home',
        users=users.users,
        nodes=nodes.nodes,
        node="something"
    )


@app.route('/save/', methods=['POST'])
def add_category_item():
    node = request.form.get("node")
    user = request.form.get("user")

    nodes.claim_node(node, user)

    return redirect(url_for(f'home'))
