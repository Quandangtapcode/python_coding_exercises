service = {
    "A": "High security",
    "B": "Optimal performance",
    "C": "Integrated cPanel",
    "D": "High security",
    "E": "Support 24/7",
    "F": "Optimal performance"
}
value = list(service.values())
unique_value = [v for v in value if value.count(v) == 1]
Filter_service = {k: v for k, v in service.items() if v in unique_value}
print("Dictionary after being filtered:", Filter_service)