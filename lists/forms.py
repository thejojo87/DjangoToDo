#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Thejojo'


from django import forms
from lists.models import Item

EMPTY_LIST_ERROE = "You can't have an empty list item"


class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text' : forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
        }),
        }
        error_messages = {
            'text' : {'required': EMPTY_LIST_ERROE }
        }

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()

