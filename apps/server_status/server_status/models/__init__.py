import os
from .nodes import Nodes
from .users import Users
from server_status.config.app_conf import settings


users = Users()
nodes = Nodes(settings)
