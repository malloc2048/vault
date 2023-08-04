import json
from vault import app
from vault import models
from flask import request, render_template, redirect, url_for


# TODO: there is a bug here that the header and data need to be in the same order.
#  That will become cumbersome, so see about fixing that.
#  Unsure right now if it is fixable here or in the html template
@app.route('/category/<category>', methods=['GET'])
def category_display(category):
    attributes, data = models.get_category_data(category)

    # convert the requested filters if present
    args = request.args.to_dict()
    filter_dict = dict()

    if 'filter' in args:
        filter_str = args.get('filter').replace('\'', '\"')
        filter_dict = json.loads(filter_str)

    # filters = {ele: set() for ele in attributes}
    filters = models.get_category_query_fields(category)
    # for row in data:
    #     for item in row:
    #         if item != 'id' and item != 'hash' and row[item]:
    #             filters[item].add(row[item])  # category should exist now

    # filter the results
    # if filter_dict:
    #     data = filter_data(list(filter_dict.values()), data)

    return render_template(
        f'category.html',
        category=category,
        attributes=attributes,
        category_data=data,
        categories=models.category_details(),
        filters=filters,
    )


@app.route('/filter/<category>', methods=['POST'])
def filter_items(category):
    data = request.form.to_dict()

    delete = [key for key in data if data[key] in key]
    for key in delete:
        del data[key]

    if data:
        return redirect(url_for(f'category_display', category=category, filter=data))
    else:
        return redirect(url_for(f'category_display', category=category))


@app.route('/save/<category>', methods=['POST'])
def add_category_item(category):
    data = request.form.to_dict()
    models.add_category_item(category, data)
    models.save(category)

    return redirect(url_for(f'category_display', category=category))
