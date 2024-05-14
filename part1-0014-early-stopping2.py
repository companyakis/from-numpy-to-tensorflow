import pandas as pd

model_history = pd.DataFrame([epoch_l, model_w1_l, model_w2_l, error_l])

model_history = model_history.T.rename(columns = {0: "Epochs", 1: "Weight 1", 2: "Weight 2", 3: "Error"} )

"""

    Epochs	Weight 1	Weight 2	Error
0	  1	      7.9808	 -1.1044	  [21.78]
1	  2	      7.841408  -1.862344	[158.1228]
"""
