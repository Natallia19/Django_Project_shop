from django import forms

# Форма для добавления товара в карзину
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

# тут количество выбранного товара


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
