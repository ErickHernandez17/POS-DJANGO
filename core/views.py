
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
    template_name = "core/home.html"

    """ def get_context_data(self, **kwargs):
        # Este metodo nos ayuda a pasar contexto al template, se usa para contextos largos o complejos   
        context = super().get_context_data(**kwargs) 
        context["title"] = "My super web playground"
        return context """


    def get(self, request, *args, **kwargs):
        #De igual manera se utiliza para pasar contexto al request pero para contextos simples, como en este caso el de solo mandar el titulo de la pagina
        return render(request, self.template_name, {'title':"Bienvenido a ZYZZPLEMENTS"})


