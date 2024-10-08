""" 			  		 			     			  	   		   	  			  	
Loss and Accuracy tests.  (c) 2021 Georgia Tech

Copyright 2021, Georgia Institute of Technology (Georgia Tech)
Atlanta, Georgia 30332
All Rights Reserved

Template code for CS 7643 Deep Learning

Georgia Tech asserts copyright ownership of this template and all derivative
works, including solutions to the projects assigned in this course. Students
and other users of this template code are advised not to share it with others
or to make it available on publicly viewable websites including repositories
such as Github, Bitbucket, and Gitlab.  This copyright statement should
not be removed or edited.

Sharing solutions with current or future students of CS 7643 Deep Learning is
prohibited and subject to being investigated as a GT honor code violation.

-----do not edit anything above this line---
"""

import unittest
import numpy as np
from models.softmax_regression import SoftmaxRegression


class TestActivation(unittest.TestCase): # INHERITS FROM
    """ The class containing all test cases for this assignment"""

    def setUp(self):
        """Define the functions to be tested here."""
        self.model = SoftmaxRegression()

    def test_ce_loss(self):
        x = np.array([[0.2, 0.5, 0.3], [0.5, 0.1, 0.4], [0.3, 0.3, 0.4]])
        y = np.array([1, 2, 0])
        # expected_loss = 0.937803
        loss = self.model.cross_entropy_loss(x, y)
        # self.assertAlmostEqual(loss, expected_loss, places=5)

    def test_accuracy(self):
        x = np.array([[0.2, 0.5, 0.3], [0.5, 0.1, 0.4], [0.3, 0.3, 0.4]])
        y = np.array([1, 2, 0])
        # expected_acc = 0.3333
        acc = self.model.compute_accuracy(x, y)
        # self.assertAlmostEqual(acc, expected_acc, places=4)

    # def test_softmax(self):
    #     scores = np.array([[0.2, 0.5, 0.3], [0.5, 0.1, 0.4], [0.3, 0.3, 0.4], [0.5, 0.1, 0.4]])
    #     result = self.model.softmax(scores)
    #     print(result)

