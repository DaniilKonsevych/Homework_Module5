import re

def checking_generator():
    checking = []

    def generator_numbers(text: str):
        number = re.search(r"\d+\.\d+", text).group()
        while number in checking:
            text = text.replace(number, "")
            number = re.search(r'\d+\.\d+', text).group()
        else:
            checking.append(number)
            yield float(number)
    
    return generator_numbers

generator_numbers = checking_generator()

def sum_profit(text: str, func: callable):
    profits = []
    for i in re.findall(r'\d+\.\d+', text):
        profits.append(next(func(text)))
    return sum(profits)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45  324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
