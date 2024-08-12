import dataclasses
import os


@dataclasses.dataclass
class AppConfig:
    debug : bool = True
    data_files_directory: str = os.environ.get('DATA_FILES_DIRECTORY', "/home/p3vaildev/vault3")

    gunicorn_reload: bool = True
    gunicorn_accesslog: str = "-"
    gunicorn_bind_port: int = os.environ.get("GUNICORN_PORT", 8001)
    gunicorn_accesslog_format: str = '%(t)s %(h)s "%(r)s" %(s)s "%(a)s"'
    gunicorn_bind_host: str = os.environ.get("GUNICORN_HOST", '0.0.0.0')
    gunicorn_configured_workers: int = os.environ.get("GUNICORN_WORKER_COUNT", 4)
    gunicorn_app_dir: str = os.environ.get('GUNICORN_APP_DIR', '/home/p3vaildev')


settings = AppConfig()
