from django.forms.widgets import Widget
from django.forms.widgets import Input 
from django.template import loader
from django.utils.safestring import mark_safe


class DragnDropWidget(Input):
    template_name = 'languageTests/dragndrop_widget.html'

    def get_context(self, name, value, attrs=None):
        context = super().get_context(name, value, attrs)
        value=context['widget']['value']
        return {'widget': {
            'name': name,
            'value': value,
        }}
        
    #def value_from_datadict(self, data, files, name):
    #    print("data=====<{}>".format(data))
    #    print("files====<{}>".format(files))
    #    print("name=====<{}>".format(name))
    #    return data.get(name)

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)
    
    
    #def render(self, name, value, attrs=None, renderer=None):
    #    """Render the widget as an HTML string."""
    #    context = self.get_context(name, value, attrs)
    #    return self._render(self.template_name, context, renderer)