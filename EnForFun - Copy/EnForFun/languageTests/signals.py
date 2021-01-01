from django.dispatch import Signal

topic_viewed_signal   = Signal(providing_args=['instance', 'request'])

test_viewed_signal    = Signal(providing_args=['instance', 'request'])

test_attempt_signal = Signal(providing_args=['instance', 'request', 'passed'])