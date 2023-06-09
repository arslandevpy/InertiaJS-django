from . import mixins


class IndexView(mixins.InertiaView):
    component = "Index"
    extra_context = {"name": "World"}
    

class AboutView(mixins.InertiaView):
    component = "About"
    extra_context = {"pageName": "About"}
