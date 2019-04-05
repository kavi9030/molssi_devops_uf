"""
string_utils.py
A sample repo for the MolSSI workshop at UF

Misc. string processing functions

"""

def title_case(sentence):

    """
    Convert a string to title case
   

    Parameters
    ----------

    sentence : string
            String to be converted to title case 

    Returns
    ----------	 

    title_case_sentence : string
             String converted to tile case

    """

    title_case_sentence = []
  
    for i in range (len(sentence.split())):
          ttl  = sentence.split()[i][0].upper() + sentence.split()[i][1:]
          title_case_sentence.append(ttl)

    return ' '.join(title_case_sentence)



def ttl_case(sentence):


    # Check that input is a string
    if not isinstance(sentence, str):
        raise TypeError("Invalid input!")

    # Error if empty
    if len(sentence) == 0:
        raise TypeError("Empty input!")

    ret = sentence[0].upper()
    for i in range(1, len(sentence)):
        if sentence[i - 1] == ' ':
            ret += sentence[i].upper()
        else:
            ret += sentence[i].lower()
    return ret



