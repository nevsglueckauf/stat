# Textmanipulationsstuff
# AUTHOR Sven Schrodt
# SINCE 2025-06-11

class Texitfy:
    """ Klasse zur Textbearbeitung

        - Diverses Quoting 
    """
    
    @staticmethod
    def quote(wrd:str) -> str:
        return "'" + wrd + "'"
  
    @staticmethod
    def quote_typo(wrd:str) -> str:
        return '„' + wrd + '“'
    
##print(Texitfy.quote('Sven'))