# Создаем словарь для перевода
translations = {
    'лёгкий': 'light',
    'праздный': 'idle',
    'среда': 'environment'
}

print("Перевод слова 'лёгкий':", translations['лёгкий'])

translations['вес'] = 'weight'

translations['праздный'] = 'бездействующий'

print("\nОбновленный словарь:")
for rus, eng in translations.items():
    print(f"{rus} - {eng}")