def calculate_totals(cart):
    subtotal = sum(item['price'] * item['quantity'] for item in cart)
    gst_total = sum((item['price'] * item['quantity']) * (item['gst'] / 100) for item in cart)
    total = subtotal + gst_total
    return subtotal, gst_total, total

def apply_discount(total, discount_percent):
    return total - (total * discount_percent / 100)
