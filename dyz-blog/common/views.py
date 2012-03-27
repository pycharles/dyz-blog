import logging
from django.template import RequestContext, loader, Context
from django.shortcuts import render_to_response
from django import forms

from django.conf import settings
if settings.MAILER == 'send_mail':
    from django.core.mail import send_mail

log = logging.getLogger(__name__)

class ContactForm(forms.Form):
	email = forms.EmailField(label = 'Email', required=True)
	message = forms.CharField(label = 'Message', required=True, widget = forms.Textarea)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			template = loader.get_template('contact_message.txt')
			context = Context({'form': data})
			payload = template.render(context)
			log.debug('EMAILING (contact form):  %s' % data['email'])
			send_mail(subject = 'COB Contact Form', message = payload, from_email = settings.DEFAULT_FROM_EMAIL, recipient_list = [settings.SUPPORT_EMAIL_RCPT,])
			return render_to_response('thanks.html', {'form': data}, context_instance = RequestContext(request))
	else:
		form = ContactForm()

	return render_to_response('contact.html',{
		'form': form,
		}, context_instance = RequestContext(request))