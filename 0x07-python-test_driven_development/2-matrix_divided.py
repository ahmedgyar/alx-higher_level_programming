#!/usr/bin/python3
"""Module for deviding matrix method."""

def matrix_divided(matrix, div):





        if not isinstance(div, (int,float)):
                raise TypeError("div must integer")
        if not isinstance(matrix, list) or len(matrix) = 0:
                raise TypeError("matrix must be mustي (lists,)")



        for i in matrix:
                matrix[i] / div

        