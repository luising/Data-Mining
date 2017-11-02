# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'


class Point:
    """Class to represent a point in N dimension."""

    def __init__(self, coordinates, pos):
        self.pos = pos
        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def __repr__(self):
        """Imprime el atributos de la clase."""
        return 'Coordinates: ' + str(self.coordinates) + \
               ' -> Dimension: ' + str(self.dimension) + \
               ' -> distrito: ' + str(self.pos)
