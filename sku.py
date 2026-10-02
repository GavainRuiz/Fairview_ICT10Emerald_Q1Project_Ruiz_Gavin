from pyscript import document


def GenerateSKU(event):
    category = document.getElementById("Category").value
    product_name = document.getElementById("Product_name").value.strip()
    stock_quantity = document.getElementById("Stock_quantity").value.strip()
    result = document.getElementById("sku_result")

    if not product_name:
        result.innerText = "Enter a product name to generate an SKU."
        return

    if not stock_quantity:
        result.innerText = "Enter a stock quantity to generate an SKU."
        return

    try:
        quantity = int(stock_quantity)
        if quantity < 0:
            raise ValueError
    except ValueError:
        result.innerText = "Stock quantity must be a whole number of zero or more."
        return

    category_code = "".join(character for character in category if character.isalnum())[:3].upper()
    product_code = "".join(character for character in product_name if character.isalnum())[:4].upper()
    sku = f"{category_code}-{product_code}-{quantity}"
    result.innerText = f"SKU: {sku}"
