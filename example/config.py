#!/usr/bin/env python3

import sys

sys.path.append('../dist')

from PolygonLoader import PolygonLoader

worlds['My World'] = '/home/username/server/world'

polygonLoader = PolygonLoader('Properties')
polygonLoader.load('properties.json')

renders['normalrender'] = {
    'world': 'My World',
    'title': 'Normal Render of My World',
    'manualpois': polygonLoader.getPois(),
    'markers': [
        polygonLoader.getMarker()
    ]
}

outputdir = '/home/username/mcmap'
