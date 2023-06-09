from django.views import generic
from inertia import render
from django.core.exceptions import ImproperlyConfigured


class InertiaView(generic.View):
    component = None
    extra_context = None
    extra_template_data = None
    
    def get_props(self, **kwargs):
        return self.extra_context or {}
    
    def get_component(self, **kwargs):
        if self.component is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'component' or an implementation of 'get_component()'"
            )
        return self.component
    
    def get_template_data(self, **kwargs):
        return self.extra_template_data or {}
    
    def get(self, request, *args, **kwargs):
        return render(request, self.component, props=self.get_props(), template_data=self.get_template_data())
