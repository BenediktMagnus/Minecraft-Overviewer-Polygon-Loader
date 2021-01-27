# Minecraft Overviewer Polygon Loader

This allows loading markers in polygonial forms, e.g. for rendering player properties, from a simple JSON format.

The polygons get their own overlay, thus can be enabled and disabled by the viewer.

## Config

```python
from PolygonLoader import PolygonLoader

polygonLoader = PolygonLoader('id')
polygonLoader.load('filename.json')

renders['normalrender'] = {
    'manualpois': polygonLoader.getPois(),
    'markers': [
        polygonLoader.getMarker()
    ]
}
```

### Optional Configuration

```python
polygonLoader.colour = '#FF0000' # The colour the polygons will be filled with.
polygonLoader.weight = 5 # The weight/width of the borders.
polygonLoader.fill = True # If set to false, the polygons will not be filled with colour and only the borders are visible.
polygonLoader.defaultY = 64 # The default Y coordinate for points if none is explicitely given.
```

## JSON Format

```json
[
    {
        "name": "name",
        "polygon": [
            {
                "x": 0,
                "z": 0
            }
        ]
    }
]
```

Additionally, there can be a Y coordinate set for every polygon point.
