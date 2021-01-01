from django.core.exceptions import ValidationError

class validate_excersise_answers(object):
    code = 'invalid'
    
    def __init__(self, answer, code = None):
        self.answer=answer
        if code is not None:
            self.code   = code

    def __call__(self, value):
        """
            
        """
        print("value=<{}>".format(value))
        print("answer=<{}>".format(self.answer))
        print("answerstr=<{}>".format(self.answer.answer_string))
        if value.lower() != self.answer.answer_string.lower():
            print("<{}> != <{}>".format(value,self.answer.answer_string))
            explanation=self.answer.explanation_set.filter(wrong_answer__iexact=value).filter(language__name__contains="English")
            #explanation=self.answer.explanation_set.filter(wrong_answer__iexact=value)
            if len(explanation) == 0:
                raise ValidationError("We don't know why, but it is wrong", code=self.code)
            elif len(explanation) > 1:    
                print("length={}".format(len(explanation)))
                print("ERROR: More then two explanations found:" )
                for expl in explanation:
                    print("ERROR:explanation text={}".format(expl.explain_text))  
            else:
                print("explain text={}".format(explanation[0].explain_text))
            raise ValidationError(explanation[0].explain_text, code=self.code)
        