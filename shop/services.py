import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

def buy(name: str, price: int ):
    """
    name    : str - Имя продукта
    price   : int - Цена продукта
    
    Создание продукта, цены и сессии для оплаты конкретного продукта
    """
    
    product = stripe.Product.create(name=name)

    price = stripe.Price.create(
        currency='rub',
        unit_amount=price * 100,
        product_data={'name': name}
    )

    resp = stripe.checkout.Session.create(
      success_url="https://example.com/success",
      line_items=[{"price": price['id'], "quantity": 1}],
      mode="payment",
    )
    return resp
