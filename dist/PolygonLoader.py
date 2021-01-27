#!/usr/bin/env python3

import json as Json
from copy import copy
from typing import List

class PolygonLoader:
    """
    Load polygons from a JSON file for using them as markers in Minecraft Overviewer.
    """

    fill = True
    colour = '#FF0000'
    weight = 5
    defaultY = 64
    _loadedData: list

    def __init__(self, id: str):
        self.id = id
        self._loadedData = []

    def load(self, filePath: str) -> None:
        data: list = []

        with open(filePath, 'r') as jsonFile:
            data = Json.load(jsonFile)

        # Add y coordinates if they are missing:
        for entry in data:
            for point in entry['polygon']:
                if 'y' not in point:
                    point['y'] = self.defaultY

        self._loadedData = data

    def getMarker(self) -> dict:
        marker = {
            'name': self.id,
            'filterFunction': lambda poi: self._filterFunction(poi)
        }
        return marker

    def getPois(self) -> List[dict]:
        pois = []

        for index, entry in enumerate(self._loadedData):
            poi = entry['polygon'][0].copy()
            poi['id'] = self.id
            poi['index'] = index
            pois.append(poi)

        return pois

    def _filterFunction(self, poi: dict) -> dict:
        if poi['id'] != self.id:
            return

        entry = self._loadedData[poi['index']]

        result = {
            'text': entry['name'],
            'color': self.colour,
            'weight': self.weight,
            'fill': self.fill,
            'polygon': entry['polygon']
        }

        return result
