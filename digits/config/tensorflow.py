# Copyright (c) 2016, NVIDIA CORPORATION.  All rights reserved.
from __future__ import absolute_import
from . import option_list


def test_tf_import():
    """
    Tests if tensorflow can be imported, returns if it went okay and optional error.
    """
    try:
        import tensorflow  # noqa
        return True
    except (ImportError, TypeError):
        return False

tf_enabled = test_tf_import()

if not tf_enabled:
    print('Tensorflow support disabled.')

if tf_enabled:
    option_list['tensorflow'] = {
        'enabled': True,
        'multi_gpu': False,
    }
else:
    option_list['tensorflow'] = {
        'enabled': False,
        'multi_gpu': False,
    }