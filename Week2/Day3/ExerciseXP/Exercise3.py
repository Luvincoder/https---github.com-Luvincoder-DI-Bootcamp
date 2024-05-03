brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": {"primary": "pink", "secondary": "green"}
    }
}

brand["number_stores"] = 2

print(f"Zara's clients are men, women, children, and home decorators.")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(f"The last international competitor is {brand['international_competitors'][-1]}.")

print("Major clothes colors in the US:", brand["major_color"]["US"])

print("Number of key-value pairs in the dictionary:", len(brand))

print("Keys of the dictionary:", list(brand.keys()))

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print("Value of the key number_stores:", brand["number_stores"])
