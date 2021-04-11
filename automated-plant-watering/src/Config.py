import os

import ujson


class Config:

    def __init__(self, config_path):
        with open(config_path, "r") as file:
            self.config = ujson.load(file)

    def get_blynk_auth_token(self):
        return self.config['blynk_auth_token']