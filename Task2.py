def generator_numbers(text: str):
    for i in text.split():
        try:
            yield float(i)
        except:
            yield 0.0

def sum_profit(text: str, func: callable):
    profits = []
    for str_object in text.split():
        profits.append(next(func(text)))
    return sum(profits)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45  324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
