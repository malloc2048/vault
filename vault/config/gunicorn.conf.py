import os
from vault.config.app_conf import settings


bind = f"{settings.gunicorn.bind_host}:{settings.gunicorn.bind_port}"

configured_workers = settings.gunicorn.configured_workers

reload = settings.gunicorn.reload

accesslog = settings.gunicorn.accesslog
access_log_format = settings.gunicorn.access_log_format

chdir = settings.app_dir
