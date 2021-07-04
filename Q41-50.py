ticker="btc_krw"
TICKER = ticker.upper()
print(TICKER)

ticker1 = TICKER.lower()
print(ticker1)

str = 'hello'
print(str.capitalize())

file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
print(file_name.endswith(("xlsx", "xls")))

file_name="2020_보고서.xlsx"
print(file_name.startswith('2020'))

date = "2020-05-01"
year = date.split("-")[0]
month = date.split("-")[1]
day = date.split("-")[2]
print(year)
print(month)
print(day)

a = "hello world"
a.split()

ticker = "btc_krw"
ticker.split("_")

data = "039490    "
print(data.rstrip())
