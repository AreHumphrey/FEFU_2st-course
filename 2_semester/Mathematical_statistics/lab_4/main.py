import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats import t
from tabulate import tabulate

data = {
    "Район": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "x": [78, 82, 87, 78, 78, 106, 67, 82, 73, 87, 76, 115],
    "y": [133, 148, 134, 154, 162, 185, 138, 158, 152, 162, 159, 173]
}

df = pd.DataFrame(data)

X = df["x"]
Y = df["y"]
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()

correlation = np.corrcoef(df["x"], df["y"])[0, 1]
mean_x = np.mean(df["x"])
mean_y = np.mean(df["y"])

params = model.params
t_values = model.tvalues
p_values = model.pvalues

x_new = 1.07 * mean_x
y_pred = model.predict([1, x_new])

se = np.sqrt(model.mse_resid)
n = len(df)
x_mean = np.mean(df["x"])
SSX = np.sum((df["x"] - x_mean) ** 2)
confidence_interval = t.ppf(0.975, df=n-2) * se * np.sqrt(1 + 1/n + (x_new - x_mean) ** 2 / SSX)
forecast_error = se * np.sqrt(1 + 1/n + (x_new - x_mean) ** 2 / SSX)

results = {
    "Метрика": [
        "Линейная регрессия - const",
        "Линейная регрессия - x",
        "Коэффициент парной корреляции",
        "Среднее значение x",
        "Среднее значение y",
        "Т Стьюдента - const",
        "Т Стьюдента - x",
        "P-значение - const",
        "P-значение - x",
        "Прогнозируемый y при 107% среднем значении x",
        "Ошибка прогноза",
        "Доверительный интервал - нижняя граница",
        "Доверительный интервал - верхняя граница"
    ],
    "Значение": [
        params['const'],
        params['x'],
        correlation,
        mean_x,
        mean_y,
        t_values['const'],
        t_values['x'],
        p_values['const'],
        p_values['x'],
        y_pred[0],
        forecast_error,
        y_pred[0] - confidence_interval,
        y_pred[0] + confidence_interval
    ]
}

results_df = pd.DataFrame(results)

if __name__ == "__main__":
    print(tabulate(results_df, headers='keys', tablefmt='grid', floatfmt=".4f"))
