from django import forms
from rainforest.models import Product, Review

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ('name', 'description', 'price_in_cents')

# https://django.cowhite.com/blog/django-form-validation-and-customization-adding-your-own-validation-rules/

  def clean(self):
    data = super().clean()
    description = data.get("description")
    if len(description) < 10 or len(description) > 500:
      self.add_error(
          "description", "Description must be between 10 and 500 characters.")


class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = {'comment'}

  # def clean(self):
  #   data = super().clean()
  #   comment = data.get("comment")
  #   if len(comment) < 10 or len(comment) > 500:
  #     self.add_error("comment", "Review must be between 10 and 500 characters.")
