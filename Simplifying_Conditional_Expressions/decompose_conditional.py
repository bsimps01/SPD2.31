# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    print('made alert sound.')
def make_accept_sound():
    print('***')
    print('Toxin Free')
    print('***')
    print('made acceptance sound')

ingredients = 'sodium benzoate'

def finding_toxins():
    if 'sodium nitrate' or 'sodium benzoate' or 'sodium oxide' in ingredients:
        make_alert_sound()
    else:
        make_accept_sound()

finding_toxins()