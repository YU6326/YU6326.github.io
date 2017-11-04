---
title:      "numpy 矩阵类"
date:       2017-11-4
author:     "YU"
categories: [python]
tags:
    - python
--- 
# NumPy 矩阵类

## Main Object:matrix

class numpy.matrix 是ndarray的子类,操纵矩阵更方便

Return a matrix from an array-like object, or from a stringof data. A matrix is a specialied 2-D array that retains its 2-D nature through operations. It has certain special operators, such as * (matrix multiplication) and ** (matrix power)


data: array_like or string

If data is a string, it is interpreted as a matrix with commas or spaces separating columns, and semicolons separating rows.

dtype: data-type

```python
a=np.matrix('1 2;3 4')
b=np.matrix([[1,2],[3,4]])
```
|attributes |description|
|---------|------------|
A	|Return self as an ndarray object.
A1	|Return self as a flattened ndarray.
H	|Returns the (complex) conjugate transpose of self.
I	|Returns the (multiplicative) inverse of invertible self.
T	|Returns the transpose of the matrix.
base	|Base object if memory is from some other object.
ctypes	|An object to simplify the interaction of the array with the ctypes module.
data	|Python buffer object pointing to the start of the array’s data.
dtype	|Data-type of the array’s elements.
flags	|Information about the memory layout of the array.
flat	|A 1-D iterator over the array.
imag	|The imaginary part of the array.
itemsize	|Length of one array element in bytes.
nbytes	|Total bytes consumed by the elements of the array.
ndim	|Number of array dimensions.
real	|The real part of the array.
shape	|Tuple of array dimensions.
size	|Number of elements in the array.
strides	|Tuple of bytes to step in each dimension when traversing an array.
