from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from orders.forms import OrderForm


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
