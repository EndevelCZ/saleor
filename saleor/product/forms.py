from django import forms

from ..cart.forms import AddToCartForm
from .models import Bag, BagVariant, Shirt, ShirtVariant, Color


class BagForm(AddToCartForm):

    def get_variant(self, clean_data):
        return BagVariant.objects.get(product__color=self.product.color)


class ShirtForm(AddToCartForm):

    size = forms.ChoiceField(choices=ShirtVariant.SIZE_CHOICES,
                             widget=forms.RadioSelect())

    def get_variant(self, clean_data):
        size = clean_data.get('size')
        return ShirtVariant.objects.get(size=size,
                                        product__color=self.product.color)


def get_form_class_for_product(product):
    if type(product) is Shirt:
        return ShirtForm
    if type(product) is Bag:
        return BagForm
    raise NotImplemented()