""" 			  		 			     			  	   		   	  			  	
Softmax Regression Model.  (c) 2021 Georgia Tech

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

# Do not use packages that are not in standard distribution of python
import numpy as np

from ._base_network import _baseNetwork


class SoftmaxRegression(_baseNetwork):
    def __init__(self, input_size=28 * 28, num_classes=10):
        """
        A single layer softmax regression. The network is composed by:
        a linear layer without bias => (activation) => Softmax
        :param input_size: the input dimension
        :param num_classes: the number of classes in total
        """
        super().__init__(input_size, num_classes)
        self._weight_init()

    def _weight_init(self):
        '''
        initialize weights of the single layer regression network. No bias term included.
        :return: None; self.weights is filled based on method
        - W1: The weight matrix of the linear layer of shape (num_features, hidden_size)
        '''
        np.random.seed(1024)
        self.weights['W1'] = 0.001 * np.random.randn(self.input_size, self.num_classes) 
        print("weight self shape", self.weights['W1'].shape)
        self.gradients['W1'] = np.zeros((self.input_size, self.num_classes))
        print("gradient self shape", self.gradients['W1'].shape)

    def forward(self, X, y, mode='train'):
        """
        Compute loss and gradients using softmax with vectorization.

        :param X: a batch of image (N, 28x28)
        :param y: labels of images in the batch (N,)
        :return:
            loss: the loss associated with the batch
            accuracy: the accuracy of the batch
        """
        loss = None
        gradient = None
        accuracy = None
        #############################################################################
        # TODO:                                                                     #
        #    1) Implement the forward process and compute the Cross-Entropy loss    #
        #    2) Compute the gradient of the loss with respect to the weights        #
        # Hint:                                                                     #
        #   Store your intermediate outputs before ReLU for backwards               #
        #############################################################################
        y_arr = np.zeros((len(y), self.num_classes)) # 64 x 10
        print("y_arr shape:", y_arr.shape)
        print(X.shape)
        y_arr[np.arange(len(y)), y] = 1
        Z = X.dot(self.weights['W1']) # X -> 64, 784 -- w1 -> 784, 10 -> 64, 10
        print(Z.shape)
        Z_re = self.ReLU(Z)
        print("Z_re Shape: ", Z_re.shape)
        prob = self.softmax(Z_re) # answer
        print("prob Shape: ", prob.shape)

        loss = self.cross_entropy_loss(prob, y) # Why loss ? 
        print(loss)

        accuracy = self.compute_accuracy(prob, y)
        print(accuracy)
        gradient = prob - y_arr # https://alexcpn.medium.com/yet-another-backpropagation-article-20ae57aabd1e
        print("gradient shape", gradient.shape)
        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        if mode != 'train':
            return loss, accuracy

        #############################################################################
        # TODO:                                                                     #
        #    1) Implement the backward process:                                     #
        #        1) Compute gradients of each weight by chain rule                  #
        #        2) Store the gradients in self.gradients                           #
        #############################################################################
        if mode == 'train':
                    print(self.gradients["W1"].shape)
                    self.gradients["W1"] = X.T.dot(gradient /len(y) * self.ReLU_dev(Z))
                    # https://alexcpn.github.io/html/NN/ml/8_backpropogation_full/ 
                    # https://medium.com/@ppuneeth73/the-chain-rule-of-calculus-the-backbone-of-deep-learning-backpropagation-9d35affc05e7

        #############################################################################
        #                              END OF YOUR CODE                             #
        #############################################################################
        return loss, accuracy
