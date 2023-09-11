from django import template

register = template.Library()
#добавили в файл словарь со списком кодов валют и их символов, который используем в функции.
CURRENCIES_SYMBOLS = {
    "rub": "руб",
    "usd": "$",
}


@register.filter()
def currency(value, code="rub"):
    """
    value: значение, к которому нужно применить фильтр
    code: код валюты
    """
    postfix = CURRENCIES_SYMBOLS[code]

    return f"{value} {postfix}"
