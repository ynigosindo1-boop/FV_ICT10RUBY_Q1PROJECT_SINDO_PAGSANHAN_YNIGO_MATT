
from pyscript import document, display  

#SKU GENERATOR
def SKUGENERATOR(e):
    categories = document.getElementById("categories").value 
    products = document.getElementById("products").value.strip()
    stockquantity = document.getElementById("Stock_Quantity").value.strip()

    product_value = products[:3].upper()

    stockquantity_value = f"{int(stockquantity):02d}"

    SKUgenerator = (f"{categories[:3]}{product_value}{stockquantity_value}")

    display(f"SKU:{SKUgenerator}", target = "result", append=False)