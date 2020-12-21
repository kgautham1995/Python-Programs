from django.views.generic import RedirectView

class fb(RedirectView):
    url="https://www.facebook.com/"
class wa(RedirectView):
    url="https://web.whatsapp.com/"
class tw(RedirectView):
    url="https://www.twitter.com/"