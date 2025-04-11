import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv("Arthur Morgan.csv")

print("\nПервые 5 строк:")
head = data.head()
print(head)

print("\nПоследние 5 строк:")
tail = data.tail()
print(tail)

print("\nИнформация о данных:")
print(data.info())

print("\nОписательная статистика:")
print(data.describe())

character_counts = data['name'].value_counts().head(10)
print("\nТоп-10 персонажей по количеству реплик:")
print(character_counts)

arthur_dialogue = data[data['name'] == 'Arthur Morgan']
print("\nПример реплик Arthur Morgan:")
print(arthur_dialogue.head(10))

total_lines = character_counts.sum()
percentage = (character_counts / total_lines * 100).round(1)  

print("Топ-10 персонажей по количеству реплик (в %):")
print(percentage)

explode = [0.1 if name == "Arthur Morgan" or name == "John Marston" else 0 for name in character_counts.index]

plt.figure(figsize=(10, 10))
plt.pie(
    character_counts,
    labels=character_counts.index,
    autopct='%1.1f%%',  
    startangle=90,
    explode=explode,      
    shadow=True,        
    colors=plt.cm.Pastel1.colors  
)

plt.title('Распределение реплик среди топ-10 персонажей (%)', pad=20)
plt.axis('equal')  
plt.tight_layout()
plt.show()


character_name = input('Введите имя персонажа, чьи фразы вы хотите посмотреть: ')
character_lines = data[data['name'] == character_name]['line']

top_phrases = Counter(character_lines).most_common(10)
phrases, counts = zip(*top_phrases)  

total = sum(counts)
percentages = [round((count / total) * 100, 1) for count in counts]

print(f"Топ-10 реплик персонажа '{character_name}':")
for phrase, percent in zip(phrases, percentages):
    print(f"{percent}%: {phrase[:50]}...")  

plt.figure(figsize=(12, 12))
plt.pie(
    counts,
    labels=[f"{p}% - {s[:60]}..." for p, s in zip(percentages, phrases)],  
    autopct='',  
    startangle=90,
    colors=plt.cm.tab20.colors,  
    wedgeprops={'edgecolor': 'black', 'linewidth': 0.5},
    textprops={'fontsize': 9}  
)

plt.title(f'Топ-10 реплик {character_name} (доля от всех его фраз)', pad=20)
plt.axis('equal')
plt.tight_layout()
plt.show()
