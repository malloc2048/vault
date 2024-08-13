import json
import os.path
from datetime import datetime
from dataclasses import dataclass, asdict


@dataclass
class Node:
    name: str
    url: str
    user: str = "available"
    claimed_time: datetime = datetime.now().strftime("%m-%d-%Y %H:%M:%S")

    def from_dict(self, data: dict):
        self.name = data.get("name")
        self.url = data.get("url")
        self.user = data.get("user")
        self.claimed_time = data.get("claimed_time")


class Nodes:
    def __init__(self, settings):
        self._nodes = {
            "p3vaildev-node1": Node("p3vaildev-node1", "http://portal.10-10-33-11.nip.io"),
            "p3vaildev-node2": Node("p3vaildev-node2", "http://portal.10-10-33-21.nip.io"),
            "p3vaildev-node3": Node("p3vaildev-node3", "http://portal.10-10-33-31.nip.io"),
            "p3vaildev-node4": Node("p3vaildev-node4", "http://portal.10-10-33-41.nip.io"),
            "p3vaildev-node5": Node("p3vaildev-node5", "http://portal.10-10-33-51.nip.io"),
            "p2vaildev-harness1": Node("p2vaildev-harness1", "http://10.10.33.111/graphql/"),
            "p2vaildev-harness2": Node("p2vaildev-harness2", "http://10.10.33.112/graphql/")
        }
        self._node_claims = dict()
        self.settings = settings
        self.load_claims()

    @property
    def nodes(self):
        return list(self._nodes.values())

    def load_claims(self):
        with open(os.path.join(
                self.settings.data_files_directory, self.settings.persist_filename), "r") as persist_file:
            for line in persist_file:
                node = json.loads(line)
                self._nodes[node.get("name")].from_dict(node)

    def claim_node(self, node: str, user: str):
        try:
            self._nodes.get(node, None).user = user
            self._nodes.get(node, None).claimed_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")

            with open(os.path.join(
                    self.settings.data_files_directory, self.settings.persist_filename), "w") as persist_file:

                for node in self.nodes:
                    json.dump(asdict(node), persist_file)
                    persist_file.write("\n")

        except AttributeError as e:
            print(e)