"""
remember

we have two hidden layer nodes, so we need weights
"""

# let's create output weights init function

def final_weights(min_val, max_val, number_of_hidden_layer_nodes):

  np.random.seed(1001)

  final_node_weights = np.random.randint(low = [min_val], high = [max_val], size = (number_of_hidden_layer_nodes, ))

  return final_node_weights

