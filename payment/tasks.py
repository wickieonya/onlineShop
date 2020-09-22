from io import BytesIO
from celery import task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@task
def payment_completed(order_id):
    """Task to send an e-mail notification when an order is successfully paid for."""
    order = Order.objects.get(id=order_id)
    # create invoice email
    subject = f'IoT AAOS - EE Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your purchase.'
    email = EmailMessage(subject, message, 'admin@iotaaa.com', [order.email])
    # generate pdf
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/base.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # attach pdf
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')

    # send e-mail
    email.send()
