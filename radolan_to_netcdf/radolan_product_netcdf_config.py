metadata_per_timestamp = {
    'maxrange': {
        'variable_parameters': {
            'datatype': 'i2',
            'dimensions': ('time'),
        },
        'attributes': {
            'units': 'km',
        },
    },
    'radarlocations': {
        'variable_parameters': {
            'datatype': str,
            'dimensions': ('time'),
        },
        'attributes': {
            'long_name': 'List of radar locations available at time stamp'
        },
    },
}

radolan_product_netcdf_config = {
    'RW': {
        'variables': {
            'rainfall_amount': {
                'variable_parameters': {
                    'datatype': 'i2',
                    'dimensions': ('time', 'y', 'x'),
                    'fill_value': -9999,
                    'zlib': True,
                    'complevel': 5,
                },
                'attributes': {
                    'long_name': 'Hourly rainfall',
                    'standard_name': 'rainfall_amount',
                    'units': 'kg',
                    'scale_factor': 0.1,
                    'add_offset': 0,
                    'coordinates': 'longitudes latitudes',
                    'grid_mapping': 'RADOLAN_grid',
                },
            },
        },
        'metadata_per_timestamp': metadata_per_timestamp,
        'metadata_fixed': {
            'n_lats': 900,
            'n_lons': 900,
        },
    },
    'YW': {
        'variables': {
            'rainfall_amount': {
                'variable_parameters': {
                    'datatype': 'i2',
                    'dimensions': ('time', 'y', 'x'),
                    'fill_value': -9999,
                    'zlib': True,
                    'complevel': 5,
                },
                'attributes': {
                    'long_name': '5-minute rainfall sum',
                    'standard_name': 'rainfall_amount',
                    'units': 'kg',
                    'scale_factor': 0.01,
                    'add_offset': 0,
                    'coordinates': 'longitudes latitudes',
                    'grid_mapping': 'RADOLAN_grid',
                },
            },
        },
        'metadata_per_timestamp': metadata_per_timestamp,
        'metadata_fixed': {
            'n_lats': 1100,
            'n_lons': 900,
        },
    },
}
