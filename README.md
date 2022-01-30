# List of Land Cover datasets in the GEE Catalog

[![update_list](https://github.com/davemlz/ee-land-cover-datasets/actions/workflows/update_list.yml/badge.svg)](https://github.com/davemlz/ee-land-cover-datasets/actions/workflows/update_list.yml)

A list of all the Land Cover (or discrete) datasets in Google Earth Engine.

## Values, Colors and Descriptions

The list of values, colors and descriptions for each Land Cover dataset ([check the list here](https://github.com/davemlz/ee-land-cover-datasets/blob/main/list/ee-land-cover-datasets.json)) is presented in the `ee-land-cover-datasets.json` file.

## Structure

The structure of the list follows this standard:

```python
{
    ...,
    'dataset_id': {
        'band1_name': {
            'color': {
                "value1": "color1",
                ...
            },
            'description': {
                "value1": "description1",
                ...
            }
        },
        'band2_name': {
            'color': {
                "value1": "color1",
                ...
            },
            'description': {
                "value1": "description1",
                ...
            }
        },
        ...
    },
    ...
}
```

The `color` and `description` parameters for each Land Cover band are obtained from the `gee:classes` attribute for each one of the bands in the `eo:bands` key of the Land Cover raster datasets in the [Google Earth Engine STAC](https://earthengine-stac.storage.googleapis.com/catalog/catalog.json).

If a specific band doesn't have the `gee:classes` attribute, it is not included. If no bands of a dataset have the `gee:classes` attribute, the dataset is not included. If a raster dataset doesn't have bands in the `eo:bands` attribute, the dataset is also not included in this list.

## List

Check the full list of [here](https://github.com/davemlz/ee-land-cover-datasets/blob/main/list/ee-land-cover-datasets.json).

## Download Raw Files

You can download or clone the repository:

```
git clone https://github.com/davemlz/ee-land-cover-datasets.git
```

Or you can download the single file here (right-click > Save link as...):

- JSON file: [Raw list](https://raw.githubusercontent.com/davemlz/ee-land-cover-datasets/main/list/ee-land-cover-datasets.json).

## Updates

The list is updated every day from the [Google Earth Engine STAC](https://earthengine-stac.storage.googleapis.com/catalog/catalog.json) by using GitHub Actions.
