# AUTHOR Sven Schrodt
# SINCE 2025-06-10
class MathZwo:
    """ Dinge zu  „zu Fuß“ berechnen """
    
    @staticmethod
    def clc_med(lst:list) ->float:
        """ Median berechnen

        Args:
            lst (list): Liste mit Zahlen, deren Median ermittelt werden soll

        Returns:
            _type_: Median (auch: Zentralwert)
        """
        lst.sort()
        mid = len(lst) // 2
        if len(lst) % 2 == 0: # gerade Anzahl an Elementen
            return sum(lst[mid-1:mid+1]) / 2
        else: # ungerade Anzahl an Elementen
            return lst[mid]
        
        
    @staticmethod
    def clc_avg(lst:list) ->float:
        return sum(lst) / len(lst)
    
