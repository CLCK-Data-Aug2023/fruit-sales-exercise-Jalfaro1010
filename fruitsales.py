# add your code here
# Importing Pandas
import pandas as pd

# DataFrame
df = pd.DataFrame({"Apples": [35, 41], 
                   "Bananas": [21, 34]},
                  
index=(["2017 Sales", "2018 Sales"]))

# Saving DataFrame to CSV File
df.to_csv("Fruit.csv")






