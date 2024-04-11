import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\admin\\Desktop\\IndiaGrowthPrediction\\macrotrends.csv")
pd.options.display.max_rows = 999
print(df)

print("after clean: \n")
#first to clean the data, remove the empty cell
df.dropna(inplace=True)
print(df)

#make sure to change the required data into int/float instead of string
df['Population'] = df['Population Growth Rate'].str.replace(',', '').astype(int)


plt.plot(df['Year'], df['Population'],'o')
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("The Population In India")
plt.show()