import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Настройка стиля графиков
sns.set(style="whitegrid", font_scale=1.2)
plt.rcParams['figure.figsize'] = (12, 8)

# Загрузка данных
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
columns = [
    "symboling", "normalized_losses", "make", "fuel_type", "aspiration",
    "num_doors", "body_style", "drive_wheels", "engine_location",
    "wheel_base", "length", "width", "height", "curb_weight",
    "engine_type", "num_cylinders", "engine_size", "fuel_system",
    "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
    "city_mpg", "highway_mpg", "price"
]
data = pd.read_csv(url, header=None, names=columns)

data.replace("?", np.nan, inplace=True)
numeric_cols = ["normalized_losses", "bore", "stroke", "horsepower", "peak_rpm", "price"]
data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric)
data.dropna(subset=["price"], inplace=True)

numeric_data = data.select_dtypes(include=[np.number])

corr_matrix = numeric_data.corr()

plt.figure(figsize=(14, 10))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(
    corr_matrix, 
    mask=mask, 
    annot=True, 
    cmap="coolwarm", 
    fmt=".2f", 
    linewidths=0.5,
    vmin=-1, vmax=1, center=0,
    annot_kws={"size": 10}
)
plt.title("Матрица корреляции параметров автомобилей (топ-5 выделены красным шрифтом)", fontsize=18)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

top_5 = corr_matrix["price"].abs().sort_values(ascending=False).index[1:6]
for col in top_5:
    plt.gca().get_xticklabels()[list(corr_matrix.columns).index(col)].set_color("red")
    plt.gca().get_yticklabels()[list(corr_matrix.columns).index(col)].set_color("red")
#plt.show()

print("\nАнализ корреляции с ценой:")
price_corr = corr_matrix["price"].sort_values(ascending=False)
for param, corr in price_corr[1:6].items():
    trend = "↑ Увеличивает цену" if corr > 0 else "↓ Снижает цену"
    print(f"- {param}: {corr:.2f} ({trend})")

print("\nПример интерпретации:")
print("1. Чем больше engine_size (объём двигателя), тем выше цена (сильная положительная корреляция).")
print("2. Высокий highway_mpg (экономичность) связан с более низкой ценой (отрицательная корреляция).")

##Гипотезы
print('Нулевая гипотеза (H₀):'
'Мощность двигателя (horsepower) не влияет на цену автомобиля (корреляция равна нулю).'
'Альтернативная гипотеза (H₁):'
'Мощность двигателя (horsepower) положительно коррелирует с ценой автомобиля (корреляция > 0).')

sns.lmplot(x="horsepower", y="price", data=data, line_kws={"color": "red"})
plt.title("Зависимость цены от мощности двигателя")

plt.show()