import os
from server_status.config.app_conf import settings


bind = f"{settings.gunicorn_bind_host}:{settings.gunicorn_bind_port}"

configured_workers = settings.gunicorn_configured_workers

reload = settings.gunicorn_reload

accesslog = settings.gunicorn_accesslog
access_log_format = settings.gunicorn_access_log_format

chdir = settings.gunicorn_app_dir
