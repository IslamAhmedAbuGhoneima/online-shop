from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['created', 'updated', 'stripe_id',
                   'paid', 'coupon', 'discount']
