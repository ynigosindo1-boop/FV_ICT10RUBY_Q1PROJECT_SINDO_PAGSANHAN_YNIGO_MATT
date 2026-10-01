from pyscript import display, document

def adding_numbers(e):
    first_number = float(document.getElementById('Food1').value) if document.getElementById('Food1').checked else 0.0
    second_number = float(document.getElementById('Food2').value) if document.getElementById('Food2').checked else 0.0
    third_number = float(document.getElementById('Food3').value) if document.getElementById('Food3').checked else 0.0
    fourth_number = float(document.getElementById('Drink1').value) if document.getElementById('Drink1').checked else 0.0
    fifth_number = float(document.getElementById('Drink2').value) if document.getElementById('Drink2').checked else 0.0

    sum = first_number + second_number + third_number + fourth_number + fifth_number
    subtotal = first_number + second_number + third_number + fourth_number + fifth_number
    display(f"Subtotal: {subtotal}", target='result')


def multiplying_numbers(e):
    first_number = float(document.getElementById('Food1').value) if document.getElementById('Food1').checked else 0.0
    second_number = float(document.getElementById('Food2').value) if document.getElementById('Food2').checked else 0.0
    third_number = float(document.getElementById('Food3').value) if document.getElementById('Food3').checked else 0.0
    fourth_number = float(document.getElementById('Drink1').value) if document.getElementById('Drink1').checked else 0.0
    fifth_number = float(document.getElementById('Drink2').value) if document.getElementById('Drink2').checked else 0.0

    subtotal = first_number + second_number + third_number + fourth_number + fifth_number
    vat = subtotal * 0.12
    total = subtotal + vat

    display(f'VAT(12%): {vat}', target='result')
    display(f'Total: {total}', target='result')


def calculate_total(e):
    adding_numbers(e)
    multiplying_numbers(e)