from django.db.models import Q
from pyparsing import nestedExpr
def parse_brackets(val):
    val = '(' + val + ')'
    parsed = nestedExpr('(',')').parseString(val).asList()
    return parsed

def parse_search_phrase(allowed_fields, phrase):
    # assume  allowed fields is list
    # check if allowed fields is iteratable or not
    # TODO exception if inconsistent list need to be handeled 
    if not hasattr(allowed_fields,'__iter__'):
        # you can raise error or return empty query object
        print("empty Filter")
        return Q()

    transformed = parse_brackets(phrase)
    print('transformed', transformed)
    def form_query(allowed_fields, transformed):
        if isinstance(transformed, list):
            for operator in ('OR', 'AND'):
                try:
                    index = transformed.index(operator)
                    print("index of operator",index)
                    break
                except:
                    pass
            else:
                print("operator not found",transformed)
                if isinstance(transformed[0],list):
                    return  form_query(allowed_fields,transformed[0])
                else:
                    if transformed[0] in allowed_fields:
                        # FIXME catch if user input in form (id in [1,2,3,4]) to be done later if time available
                        return Q(**{'__'.join((transformed[0],transformed[1])):transformed[2]})
                    # else:
                    #     # here you can return empty query or raise error not allowed
                    #     return Q()
            try:

                return (Q.__or__ if operator == 'OR' else Q.__and__)(
                        form_query(allowed_fields, transformed[:index]),form_query(allowed_fields, transformed[index + 1:]))
            except:
                return None
        else:

            # check if field allowed or not 
            if transformed[0] in allowed_fields:
                # FIXME catch if user input in form (id in [1,2,3,4]) to be done later if time available
                return Q(**{'__'.join((transformed[0],transformed[1])):transformed[2]})
            # else:
            #     # here you can return empty query or raise error not allowed
            #     return Q()
    return form_query(allowed_fields, transformed)
