customers = [
    {"name": "Arun", "units": 80},
    {"name": "Priya", "units": 150},
    {"name": "Rahul", "units": 250},
    {"name": "Divya", "units": 320},
]
def calculate(units, rate=5):
    return units*rate
for custom in customers:
    bill=calculate(custom["units"])
    print(custom["name"],"-",bill)
print ("diviya(rate 6)-",320*6) 