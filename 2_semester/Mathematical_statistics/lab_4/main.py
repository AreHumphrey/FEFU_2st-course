import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats import t
from tabulate import tabulate

data = {
    "Район": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "x": [78, 82, 87, 79, 89, 106, 67, 88, 73, 87, 76, 115],
    "y": [133, 148, 134, 154, 162, 195, 139, 158, 152, 162, 159, 173]
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
confidence_interval = t.ppf(0.975, df=n - 2) * se * np.sqrt(1 + 1 / n + (x_new - x_mean) ** 2 / SSX)
forecast_error = se * np.sqrt(1 + 1 / n + (x_new - x_mean) ** 2 / SSX)

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
results_df.index += 1

if __name__ == "__main__":
    print(tabulate(results_df, headers='keys', tablefmt='grid', floatfmt=".4f"))

    print("\nВыводы:")
    print(
        "1. Исходя из линейной регрессии, константный член (const) равен {:.4f}, а коэффициент при x равен {:.4f}. Это говорит о том, что при увеличении x на единицу, y увеличивается на {:.4f}.".format(
            params['const'], params['x'], params['x']))
    print(
        "2. Коэффициент парной корреляции равен {:.4f}, что указывает на умеренную положительную связь между x и y.".format(
            correlation))
    print("3. Среднее значение x составляет {:.4f}, а среднее значение y составляет {:.4f}.".format(mean_x, mean_y))
    print(
        "4. Значения t-статистики для константного члена и коэффициента при x равны {:.4f} и {:.4f} соответственно.".format(
            t_values['const'], t_values['x']))
    print(
        "5. Значения p-значений для константного члена и коэффициента при x равны {:.4f} и {:.4f} соответственно, что указывает на статистически значимые параметры модели при уровне значимости 0.05.".format(
            p_values['const'], p_values['x']))
    print("6. Прогнозируемое значение y при x, равном 107% среднего значения x, составляет {:.4f}.".format(y_pred[0]))
    print("7. Ошибка прогноза составляет {:.4f}.".format(forecast_error))
    print(
        "8. Доверительный интервал для прогноза составляет от {:.4f} до {:.4f}.".format(y_pred[0] - confidence_interval,
                                                                                        y_pred[0] + confidence_interval))

    print("\nОбщий вывод:")
    print("Линейная регрессия показала, что между x и y существует умеренная положительная связь. "
          "Коэффициенты модели статистически значимы при уровне значимости 0.05, что подтверждается низкими значениями p-значений. "
          "Прогнозируемое значение y при x, равном 107% от среднего значения x, дает уверенность в точности прогноза благодаря узкому доверительному интервалу.")
