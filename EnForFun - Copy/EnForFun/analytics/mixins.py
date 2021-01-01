from .signals import object_viewed_signal
import pprint


class ObjectViewedMixin(object):
    def get_context_data(self, *args, **kwargs):
        context  = super(ObjectViewedMixin,self).get_context_data(*args,**kwargs)
        request  = self.request
        instance = context['object']
        #print("^^CONTEXT^^^^")
        #pprint.pprint(context)
        #print("^^CONTEXT^^^^")
        if instance:
            if self.request.user.is_authenticated:
                object_viewed_signal.send(instance.__class__, instance=instance, request=request)
        return context

