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

import re


def reference_point(config, problem):
    if re.match('^DTLZ[23456]I?$', type(problem).__name__):
        return [[0.6] * problem.GetNumberOfObjectives()]
    elif re.match('^WFG\d$', type(problem).__name__):
        return [[0.6] * problem.GetNumberOfObjectives()]
    elif re.match('^UF[1-7]$', type(problem).__name__):
        return [[0.6] * problem.GetNumberOfObjectives()]
    elif re.match('^UF[89]$|^UF10$', type(problem).__name__):
        return [[1] * problem.GetNumberOfObjectives()]


def _norm_weight(weight):
    _sum = sum(weight)
    return [w / _sum for w in weight]


def weight(config, problem):
    if re.match('^DTLZ[23456]I?$', type(problem).__name__):
        weights = [[0.4] * problem.GetNumberOfObjectives()]
    elif re.match('^WFG\d$', type(problem).__name__):
        weights = [[0.6] * problem.GetNumberOfObjectives()]
    elif re.match('^UF[1-7]$', type(problem).__name__):
        weights = [[0.6] * problem.GetNumberOfObjectives()]
    elif re.match('^UF[89]$|^UF10$', type(problem).__name__):
        weights = [[1] * problem.GetNumberOfObjectives()]
    return [_norm_weight(weight) for weight in weights]


def threshold(config, problem):
    return [0.4]
