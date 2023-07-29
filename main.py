greetings = {
    "English": "Hello!",
    "French": "Bonjour!",
    "Spanish": "¡Hola!",
    # Додаткові мови можна додати тут
}


def greet(language):
    return greetings.get(language, "Hello!")  # За замовчуванням повертає "Hello!" для невідомих мов


# Приклад використання
print(greet("English"))  # Виведе: Hello!
print(greet("French"))  # Виведе: Bonjour!
print(greet("German"))  # Виведе: Hello! (за замовчуванням)
