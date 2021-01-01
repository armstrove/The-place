from django.core.exceptions import ValidationError
import re

def clean_str_for_comparison(string,case_sensitive):
    output_string=string.strip()
    output_string=re.sub(r"\s+"," ",output_string)
    if not case_sensitive:
       output_string=output_string.lower()
    return output_string

def check_answer(right_answer_str,answer,case_sensitive=False):
    answer=clean_str_for_comparison(answer,case_sensitive)
        


    right_answers=right_answer_str.split("/")
    for right_answer in right_answers:
        right_answer=clean_str_for_comparison(right_answer,case_sensitive)
        print("answer       <{}>".format(answer))
        print("right_answer <{}>".format(right_answer))
        if answer==right_answer:
           print("Same")
           return True 

    return False

class validate_excersise_construct_a_sentence(object):
    code = 'invalid'
    #print("VALIDATOR!!!!!!!!")
    def __init__(self, sentence, code = None):
        self.sentence=sentence
        if code is not None:
            self.code   = code
        
    def __call__(self, value):
        """
            
        """
        print("value=<{}>".format(value))
        print("answer=<{}>".format(self.sentence))
        print("answerstr=<{}>".format(self.sentence))
        if re.match("^\s*$",value):
            print("Empty!!!!!!!!!!!!!!!")            
        if value == self.sentence:
            pass
        else:
            raise ValidationError("'{}' is not correct".format(value), code=self.code) 
        #if re.match("^\s+$",value):
        #    print("Empty!!!")
        #if value.lower() != self.answer. .lower():
        #    print("<{}> != <{}>".format(value,self.answer.answer_string))
        #    explanation=self.answer.explanation_set.filter(wrong_answer__iexact=value).filter(language__name__contains="English")
        #    #explanation=self.answer.explanation_set.filter(wrong_answer__iexact=value)
        #    if len(explanation) == 0:
        #        raise ValidationError("We don't know why, but it is wrong", code=self.code)
        #    elif len(explanation) > 1:    
        #        print("length={}".format(len(explanation)))
        #        print("ERROR: More then two explanations found:" )
        #        for expl in explanation:
        #            print("ERROR:explanation text={}".format(expl.explain_text))  
        #    else:
        #        print("explain text={}".format(explanation[0].explain_text))
        #    raise ValidationError(explanation[0].explain_text, code=self.code)    
           
class validate_excersise(object):
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
        if re.match("^\s*$",value):
            print("Empty!!!")
        if not check_answer(right_answer_str=self.answer.answer_string,answer=value):        
            explanation=self.answer.explanation_set.filter(wrong_answer__iexact=value).filter(language__name__contains="English")
            if len(explanation) == 0:
                if not re.match(r"^\s*$",self.answer.explanation_string):
                    raise ValidationError(self.answer.explanation_string, code=self.code)
                else:    
                    raise ValidationError("We don't know why, but it is wrong", code=self.code)
            elif len(explanation) > 1:    
                print("length={}".format(len(explanation)))
                print("ERROR: More then two explanations found:" )
                for expl in explanation:
                    print("ERROR:explanation text={}".format(expl.explain_text))  
            else:
                print("explain text={}".format(explanation[0].explain_text))
            raise ValidationError(explanation[0].explain_text, code=self.code)


class validate_excersise_choose_the_word(validate_excersise):
    pass

class validate_excersise_type_the_word(validate_excersise):
    pass

class validate_excersise_type_the_sentence(validate_excersise):
    pass

class validate_excersise_type_the_sentence_inline(validate_excersise):
    pass

class validate_excersise_click_the_correct_option(validate_excersise):
    pass
