import pandas as pd

model_history = pd.DataFrame([epoch_l, model_w1_l, model_w2_l, error_l])

model_history = model_history.T.rename(columns = {0: "Epochs", 1: "Weight 1", 2: "Weight 2", 3: "Error"} )

"""

Epochs	Weight 1	Weight 2	Error
0	1	7.9808	-1.1044	[21.78]
1	2	7.841408	-1.862344	[158.1228]
2	3	6.829422	-7.365017	[1147.971528]
3	4	-0.517596	-47.314427	[8334.27329328]
4	5	-53.856945	-337.347137	[60506.824109212816]
5	6	-441.100619	-2442.984616	[439279.54303288506]
6	7	-3252.489694	-17729.912714	[3189169.4824187453]
7	8	-23663.174382	-128713.010702	[23153370.442360092]
8	9	-171844.745213	-934450.302096	[168093469.41153425]
9	10	-1247642.949447	-6784103.037617	[1220358587.9277387]
"""
