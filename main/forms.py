from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags 


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock", "rating", "brand"]
        
        
     
    def clean_name(self):
        """Menghilangkan tag HTML dari field 'name' (was clean_title)."""
        name = self.cleaned_data["name"]
        return strip_tags(name)
        
    def clean_description(self):
        """Menghilangkan tag HTML dari field 'description' (was clean_content)."""
        description = self.cleaned_data["description"]
        return strip_tags(description)