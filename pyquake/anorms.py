# Copyright (c) 2019 Matthew Earl
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
# 
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
#     NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#     OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
#     USE OR OTHER DEALINGS IN THE SOFTWARE.

import numpy as np

anorms = np.array([
    (-0.525731,  0.000000,  0.850651),
    (-0.442863,  0.238856,  0.864188),
    (-0.295242,  0.000000,  0.955423),
    (-0.309017,  0.500000,  0.809017),
    (-0.162460,  0.262866,  0.951056),
    ( 0.000000,  0.000000,  1.000000),
    ( 0.000000,  0.850651,  0.525731),
    (-0.147621,  0.716567,  0.681718),
    ( 0.147621,  0.716567,  0.681718),
    ( 0.000000,  0.525731,  0.850651),
    ( 0.309017,  0.500000,  0.809017),
    ( 0.525731,  0.000000,  0.850651),
    ( 0.295242,  0.000000,  0.955423),
    ( 0.442863,  0.238856,  0.864188),
    ( 0.162460,  0.262866,  0.951056),
    (-0.681718,  0.147621,  0.716567),
    (-0.809017,  0.309017,  0.500000),
    (-0.587785,  0.425325,  0.688191),
    (-0.850651,  0.525731,  0.000000),
    (-0.864188,  0.442863,  0.238856),
    (-0.716567,  0.681718,  0.147621),
    (-0.688191,  0.587785,  0.425325),
    (-0.500000,  0.809017,  0.309017),
    (-0.238856,  0.864188,  0.442863),
    (-0.425325,  0.688191,  0.587785),
    (-0.716567,  0.681718, -0.147621),
    (-0.500000,  0.809017, -0.309017),
    (-0.525731,  0.850651,  0.000000),
    ( 0.000000,  0.850651, -0.525731),
    (-0.238856,  0.864188, -0.442863),
    ( 0.000000,  0.955423, -0.295242),
    (-0.262866,  0.951056, -0.162460),
    ( 0.000000,  1.000000,  0.000000),
    ( 0.000000,  0.955423,  0.295242),
    (-0.262866,  0.951056,  0.162460),
    ( 0.238856,  0.864188,  0.442863),
    ( 0.262866,  0.951056,  0.162460),
    ( 0.500000,  0.809017,  0.309017),
    ( 0.238856,  0.864188, -0.442863),
    ( 0.262866,  0.951056, -0.162460),
    ( 0.500000,  0.809017, -0.309017),
    ( 0.850651,  0.525731,  0.000000),
    ( 0.716567,  0.681718,  0.147621),
    ( 0.716567,  0.681718, -0.147621),
    ( 0.525731,  0.850651,  0.000000),
    ( 0.425325,  0.688191,  0.587785),
    ( 0.864188,  0.442863,  0.238856),
    ( 0.688191,  0.587785,  0.425325),
    ( 0.809017,  0.309017,  0.500000),
    ( 0.681718,  0.147621,  0.716567),
    ( 0.587785,  0.425325,  0.688191),
    ( 0.955423,  0.295242,  0.000000),
    ( 1.000000,  0.000000,  0.000000),
    ( 0.951056,  0.162460,  0.262866),
    ( 0.850651, -0.525731,  0.000000),
    ( 0.955423, -0.295242,  0.000000),
    ( 0.864188, -0.442863,  0.238856),
    ( 0.951056, -0.162460,  0.262866),
    ( 0.809017, -0.309017,  0.500000),
    ( 0.681718, -0.147621,  0.716567),
    ( 0.850651,  0.000000,  0.525731),
    ( 0.864188,  0.442863, -0.238856),
    ( 0.809017,  0.309017, -0.500000),
    ( 0.951056,  0.162460, -0.262866),
    ( 0.525731,  0.000000, -0.850651),
    ( 0.681718,  0.147621, -0.716567),
    ( 0.681718, -0.147621, -0.716567),
    ( 0.850651,  0.000000, -0.525731),
    ( 0.809017, -0.309017, -0.500000),
    ( 0.864188, -0.442863, -0.238856),
    ( 0.951056, -0.162460, -0.262866),
    ( 0.147621,  0.716567, -0.681718),
    ( 0.309017,  0.500000, -0.809017),
    ( 0.425325,  0.688191, -0.587785),
    ( 0.442863,  0.238856, -0.864188),
    ( 0.587785,  0.425325, -0.688191),
    ( 0.688191,  0.587785, -0.425325),
    (-0.147621,  0.716567, -0.681718),
    (-0.309017,  0.500000, -0.809017),
    ( 0.000000,  0.525731, -0.850651),
    (-0.525731,  0.000000, -0.850651),
    (-0.442863,  0.238856, -0.864188),
    (-0.295242,  0.000000, -0.955423),
    (-0.162460,  0.262866, -0.951056),
    ( 0.000000,  0.000000, -1.000000),
    ( 0.295242,  0.000000, -0.955423),
    ( 0.162460,  0.262866, -0.951056),
    (-0.442863, -0.238856, -0.864188),
    (-0.309017, -0.500000, -0.809017),
    (-0.162460, -0.262866, -0.951056),
    ( 0.000000, -0.850651, -0.525731),
    (-0.147621, -0.716567, -0.681718),
    ( 0.147621, -0.716567, -0.681718),
    ( 0.000000, -0.525731, -0.850651),
    ( 0.309017, -0.500000, -0.809017),
    ( 0.442863, -0.238856, -0.864188),
    ( 0.162460, -0.262866, -0.951056),
    ( 0.238856, -0.864188, -0.442863),
    ( 0.500000, -0.809017, -0.309017),
    ( 0.425325, -0.688191, -0.587785),
    ( 0.716567, -0.681718, -0.147621),
    ( 0.688191, -0.587785, -0.425325),
    ( 0.587785, -0.425325, -0.688191),
    ( 0.000000, -0.955423, -0.295242),
    ( 0.000000, -1.000000,  0.000000),
    ( 0.262866, -0.951056, -0.162460),
    ( 0.000000, -0.850651,  0.525731),
    ( 0.000000, -0.955423,  0.295242),
    ( 0.238856, -0.864188,  0.442863),
    ( 0.262866, -0.951056,  0.162460),
    ( 0.500000, -0.809017,  0.309017),
    ( 0.716567, -0.681718,  0.147621),
    ( 0.525731, -0.850651,  0.000000),
    (-0.238856, -0.864188, -0.442863),
    (-0.500000, -0.809017, -0.309017),
    (-0.262866, -0.951056, -0.162460),
    (-0.850651, -0.525731,  0.000000),
    (-0.716567, -0.681718, -0.147621),
    (-0.716567, -0.681718,  0.147621),
    (-0.525731, -0.850651,  0.000000),
    (-0.500000, -0.809017,  0.309017),
    (-0.238856, -0.864188,  0.442863),
    (-0.262866, -0.951056,  0.162460),
    (-0.864188, -0.442863,  0.238856),
    (-0.809017, -0.309017,  0.500000),
    (-0.688191, -0.587785,  0.425325),
    (-0.681718, -0.147621,  0.716567),
    (-0.442863, -0.238856,  0.864188),
    (-0.587785, -0.425325,  0.688191),
    (-0.309017, -0.500000,  0.809017),
    (-0.147621, -0.716567,  0.681718),
    (-0.425325, -0.688191,  0.587785),
    (-0.162460, -0.262866,  0.951056),
    ( 0.442863, -0.238856,  0.864188),
    ( 0.162460, -0.262866,  0.951056),
    ( 0.309017, -0.500000,  0.809017),
    ( 0.147621, -0.716567,  0.681718),
    ( 0.000000, -0.525731,  0.850651),
    ( 0.425325, -0.688191,  0.587785),
    ( 0.587785, -0.425325,  0.688191),
    ( 0.688191, -0.587785,  0.425325),
    (-0.955423,  0.295242,  0.000000),
    (-0.951056,  0.162460,  0.262866),
    (-1.000000,  0.000000,  0.000000),
    (-0.850651,  0.000000,  0.525731),
    (-0.955423, -0.295242,  0.000000),
    (-0.951056, -0.162460,  0.262866),
    (-0.864188,  0.442863, -0.238856),
    (-0.951056,  0.162460, -0.262866),
    (-0.809017,  0.309017, -0.500000),
    (-0.864188, -0.442863, -0.238856),
    (-0.951056, -0.162460, -0.262866),
    (-0.809017, -0.309017, -0.500000),
    (-0.681718,  0.147621, -0.716567),
    (-0.681718, -0.147621, -0.716567),
    (-0.850651,  0.000000, -0.525731),
    (-0.688191,  0.587785, -0.425325),
    (-0.587785,  0.425325, -0.688191),
    (-0.425325,  0.688191, -0.587785),
    (-0.425325, -0.688191, -0.587785),
    (-0.587785, -0.425325, -0.688191),
    (-0.688191, -0.587785, -0.425325),
])
