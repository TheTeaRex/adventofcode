#! /usr/bin/python3


from typing import Tuple


class Droplet(object):
    def __init__(self, position: Tuple[int]):
        self.position = position
        self.num_surface = 6