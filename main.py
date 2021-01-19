from classes import Item, Person, Cart


def main():
    item = Item("Coca", 12, 1000, 500, 12000)
    item2 = Item("Fanta", 12, 800, 400, 9600)
    item3 = Item("Feijão", 10, 700, 300, 7000)

    person = Person("fulano@gmail.com")
    person1 = Person("fulano2@gmail.com")
    person2 = Person("fulano3@gmail.com")

    list_items = []
    list_people = []

    list_items.append(item)
    list_items.append(item2)
    list_items.append(item3)

    list_people.append(person)
    list_people.append(person1)
    list_people.append(person2)

    # Chamada de métodos
    cart = Cart(list_items, list_people)
    cart.calculate_total()
    price_bp = cart.calculate_price_by_person()
    total = cart.total_price
    result_bp = cart.return_price_by_person()

    print(f"Soma total dos valores: {total/100:.2f}\n")
    print(f"Preço por pessoa: {price_bp/100:.2f}\n")
    print(f"Dicionário: {result_bp}")


main()
