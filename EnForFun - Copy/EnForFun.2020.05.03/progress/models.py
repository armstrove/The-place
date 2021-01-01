from django.db import models
from django.conf import settings
from languageTests.signals import topic_viewed_signal, test_viewed_signal, test_attempt_signal
from django.contrib.contenttypes.models import ContentType
import pprint

User         = settings.AUTH_USER_MODEL
Topic        = settings.TOPIC_MODEL
LanguageTest = settings.LANGUAGE_TEST_MODEL

class TopicProgress(models.Model):
    user          = models.ForeignKey(User, on_delete='CASCADE') # user instance instance.id
    topic         = models.ForeignKey(Topic, on_delete='CASCADE')
    finished      = models.BooleanField(default=False)
    started       = models.BooleanField(default=False)
    visited_times = models.IntegerField(default=0)
    
    #class Meta:
    #    unique_together = ('topic', 'user',)  
    
    def __str__(self):
        #print("topic=<{}>".format(self.topic))
        return "{}-{}".format(self.user, self.topic)
#    def display_topics(self):
#        return ', '.join(topics.title for topics in self.topics.all())
#        #return ', '.join(genre.name for genre in self.genre.all()[:3])

class TestProgress(models.Model):  
    user           = models.ForeignKey(User, on_delete='CASCADE') # user instance instance.id
    #topic          = models.ForeignKey(Topic, on_delete='CASCADE')
    language_test  = models.ForeignKey(LanguageTest, on_delete='CASCADE')
    finished       = models.BooleanField(default=False)
    started        = models.BooleanField(default=False)
    visited_times  = models.IntegerField(default=0)     
    failed_times   = models.IntegerField(default=0)
    passed_times   = models.IntegerField(default=0)          
    
#class ProgressProfileManager(models.Model):   
#    
#    def new_or_get(self, request):
#        user = request.user
#        #guest_email_id = request.session.get('guest_email_id')
#        created = False
#        obj = None
#        if user.is_authenticated():
#            obj, created = self.model.objects.get_or_create(
#                            user=user)
#        #elif guest_email_id is not None:
#        #    pass
#            #'guest user checkout; auto reloads payment stuff'
#            #guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
#            #obj, created = self.model.objects.get_or_create(
#            #                                email=guest_email_obj.email)
#        else:
#            pass
#        return obj, created    


#class ProgressProfile(models.Model):
#    user           = models.ForeignKey(User, on_delete='CASCADE') # user instance instance.id
#    topic_progress = models.ForeignKey(TopicProgress, blank=True, null=True, on_delete='CASCADE')
    
#    objects = ProgressProfileManager()
    
#    def __str__(self):
#        return self.user.email    
    
def topic_progress_profile_reciever(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender) # instance.__class__
#    print(sender)
#    print(instance)
#    print(request)
    #print(request.user)
    #print("sender=<{}>".format(sender))
    #print("c_type=<{}>".format(c_type))
    #print("intance=<{}>".format(instance))
    if str(c_type) == 'topic':
        new_topic_progress_obj,created   = TopicProgress.objects.get_or_create(
            user  = request.user,  
            topic = instance,
        )
        new_topic_progress_obj.visited_times+=1
        new_topic_progress_obj.save()
        #pprint.pprint(new_topic_progress_obj)
        #pprint.pprint(dir(new_topic_progress_obj))
        pprint.pprint(new_topic_progress_obj.visited_times)
        #new_progress_profile_obj = ProgressProfile.objects.get_or_create(
        #    user  = request.user,
        #    topic_progress = new_topic_progress_obj,
        #)
    
topic_viewed_signal.connect(topic_progress_profile_reciever)      

def test_viewed_reciever(sender, instance, request, *args, **kwargs):
    print("sender=<{}>".format(sender))
    print("intance=<{}>".format(instance))
    new_test_progress_obj,created = TestProgress.objects.get_or_create(
            user = request.user,
            language_test = instance
    )
    new_test_progress_obj.visited_times+=1
    new_test_progress_obj.save()
    
test_viewed_signal.connect(test_viewed_reciever)


def test_attepted(sender, instance, request, passed, *args, **kwargs):
    new_test_progress_obj,created = TestProgress.objects.get_or_create(
             user = request.user,
             language_test = instance
    )
    print("Passssed = <{}>".format(passed))
    if passed:
        new_test_progress_obj.passed_times+=1
        new_test_progress_obj.finished=True
        new_test_progress_obj.started=False
    else:
        new_test_progress_obj.failed_times+=1
        new_test_progress_obj.started=True
        new_test_progress_obj.finished=False
    new_test_progress_obj.save()    
    
test_attempt_signal.connect(test_attepted)
    