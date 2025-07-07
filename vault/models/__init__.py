import os
import sys
import json
import logging
from vault.models.model import Model
from vault.config.app_conf import settings

models_map = dict()
models_file_directory = f'{os.path.abspath(os.path.dirname(__file__))}'


def configure_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

vault_logger = configure_logging()


def get_category_data(category):
    category_model = models_map.get(category)

    if category_model:
        display_fields = category_model.display_fields
        data = category_model.query()
        return display_fields, data
    return [], []

def get_category_query_fields(category):
    category_model = models_map.get(category)

    if category_model:
        return category_model.query_fields
    return []


def get_category_counts() -> dict:
    counts = dict()
    for m in models_map.keys():
        counts.update(models_map[m].len())
    return counts

def category_details(details: bool = False) -> list:
    if details:
        cat_details = list()

        for m in models_map.keys():
            cat_details.append({
                'name': m,
                'description': models_map[m].display_name
            })

        return cat_details

    else:
        return list(models_map.keys())

def add_category_item(category: str, data: dict):
    category_model = models_map.get(category)
    if category_model:
        category_model.add(data)

def save(category: str):
    display_fields, data = get_category_data(category)

    with open(f'{settings.data_files_directory}/{category}.jsonl', 'w') as data_file:
        for entry in data:
            json.dump({'model_ver': 1, 'category': category, 'data': entry}, data_file)
            data_file.write('\n')

def load_categories():
    try:
        with open(settings.categories_file, 'r') as categories_file:
            categories = json.load(categories_file)
    except FileNotFoundError:
        vault_logger.error(f'unable to find categories.json file in {settings.data_files_directory}')

    for category in categories:
        models_map.setdefault(category, Model(
            display_name=categories[category]['display_name'],
            display_fields=categories[category]['display_fields'],
            query_fields=categories[category]['query_fields'],
            mutation_fields=categories[category]['mutation_fields']
        ))

def load_category_file(category_data_file: str):
    vault_logger.info(f'loading data file {category_data_file}')

    with open(category_data_file, 'r') as data_file:
        for line in data_file:
            data = json.loads(line)

            if data.get('category'):
                if models_map.get(data.get('category')):
                    models_map.get(data.get('category')).add(data.get('data'))

def load_data_files():
    # load the supported categories from categories.json, this must be done before the data files are loaded
    load_categories()

    data_files = os.listdir(settings.data_files_directory)
    for data_file_name in data_files:
        # only care about jsonl files, assume all others are not relevant
        if data_file_name.endswith('jsonl'):
            load_category_file(os.path.join(settings.data_files_directory, data_file_name))

def reload_data_files():
    models_map.clear()
    load_data_files()

def get_category_list():
    print(models_map.keys())
    return []
