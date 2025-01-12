import requests
import pandas as pd
import matplotlib.pyplot as plt


# 1requests
def fetch_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Полученные данные с сайта:")
        print(data[:5])
    else:
        print(f'Ошибка: {response.status_code}')


# 2 pandas
def analyze_data():

    data = {'Name': ['Tom', 'Jerry', 'Mickey'],
            'Age': [20, 25, 30],
            'Score': [95, 85, 75]}
    df = pd.DataFrame(data)


    print("Анализ данных с помощью pandas:")
    print(df.head())


    print("\nСтатистика по числовым данным:")
    print(df.describe())


# 3 matplotlib
def visualize_data():

    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]


    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График X против Y')
    plt.show()



fetch_data()
analyze_data()
visualize_data()
