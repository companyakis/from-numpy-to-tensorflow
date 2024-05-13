def weight_inits(min_val, max_val, number_of_input_features, number_of_hidden_layer_nodes):

  """
  model weight initializer function

  this function returns model weights

  """

  np.random.seed(101)

  final_node_weights = np.random.randint(low = [min_val], high = [max_val], size = (number_of_input_features, number_of_hidden_layer_nodes))

  return final_node_weights
