from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)
df = housing.frame.copy()

# 8) info()
print("=== info() ===")
df.info()

# 9) isna().sum()
print("\n=== isna().sum() ===")
print(df.isna().sum())

# 10) loc: HouseAge > 50 и Population > 2500
subset = df.loc[(df['HouseAge'] > 50) & (df['Population'] > 2500)]
print(f"\n=== Найдено {len(subset)} записей с HouseAge>50 и Population>2500 ===")
print(subset.head(20))

# 11) max/min MedHouseVal
print("\n=== Max / Min MedHouseVal ===")
print(df['MedHouseVal'].max(), df['MedHouseVal'].min())

# 12) apply(): средние значения
print("\n=== Средние значения по признакам (кроме MedHouseVal) ===")
means = df.drop(columns=['MedHouseVal']).apply(lambda col: col.mean())
print(means)
