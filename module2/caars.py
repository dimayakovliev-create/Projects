cars = {
    "Toyota": 2005,
    "Honda": 2010,
    "Chevrolet": 2012,
    "Nissan": 2018,
    "Ford": 2015
}
models = cars.keys()
header = " | ".join(models)
print(header)


some_iterable = ["a", "b", "c"]
for s in some_iterable:
    print(s+"1")

for item in cars.items():
    print(item)

for brand, year in cars.items():
    print(f"{brand:<12} | {year}")
