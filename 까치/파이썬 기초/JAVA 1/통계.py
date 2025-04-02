import pandas as pd

df = pd.DataFrame()
df['키'] = [159, 165, 177, 179]

print (df['키'].mean)
print (df['키'].std)