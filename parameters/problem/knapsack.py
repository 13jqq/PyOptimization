"""
Copyright (C) 2014, 申瑞珉 (Ruimin Shen)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import numpy
import pyoptimization.utility


def random(config):
    path = os.path.join(pyoptimization.utility.get_pyoptimization_path(config), 'Data', 'Knapsack')
    results = []
    packs = 'Random500'
    for objectives in map(int, config.get('knapsack', 'objectives').split()):
        _path = os.path.join(path, packs, str(objectives))
        price = numpy.loadtxt(os.path.join(_path, 'price.csv'), ndmin=2)
        weight = numpy.loadtxt(os.path.join(_path, 'weight.csv'), ndmin=2)
        capacity = [sum(_weight) / 2 for _weight in weight]
        assert (objectives == len(price) == len(weight) == len(capacity))
        assert (price.shape == weight.shape)
        results.append([price, weight, capacity])
    return results
