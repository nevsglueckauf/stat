# AUTHOR Sven Schrodt
# SINCE 2025-06-11
from collections import Counter
from math import sqrt

class StatzAfoot:
    """ Ein wenig Spielerei mit Statistik ohne weitere Libs (außer collections und math.sqrt 😎)
        - afoot („zu Fuß“ halt)
    
    """
    @staticmethod
    def mode(lst:list):
        """ Berechnet den Modus 
        Args:
            lst (list): Liste mit Zahlen, deren Modus/Modi ermittelt werden soll

        Returns:
            _type_: _description_
            
        FIXME Test auf mehrfache modi! 
        """
        ctd = Counter(lst)
        
        max = 0
        max_idx = 0
        for i, v in ctd.items():
            if v > max:
                max = v
                max_id = i
        return max_id
    
    @staticmethod
    def med(lst:list) ->float:
        """ Median berechnen

        Args:
            lst (list): Liste mit Zahlen, deren Median ermittelt werden soll

        Returns:
            _type_: Median (auch: Zentralwert
        """
        lst.sort()
        mid = len(lst) // 2
        if len(lst) % 2 == 0: # gerade Anzahl an Elementen
            return sum(lst[mid-1:mid+1]) / 2
        else: # ungerade Anzahl an Elementen
            return lst[mid]
        
        
    @staticmethod
    def avg(lst:list) ->float:
        """ Berechnet das arithmetische Mittel (average, arithmetic mean)

        Args:
            lst (list): Liste mit Zahlen, deren Mittel ermittelt werden soll

        Returns:
            float: _description_
        """
        return sum(lst) / len(lst)
    
    @staticmethod
    def rel_freq(dta:list)->dict:
        """ Berechnet die relative Häufigkeit (relative frequency)

        Args:
            dta (list): Liste mit Werten 

        Returns:
            dict: {'val_1': rl_frq_1, ... 'val_n': rl_frq_n'}
        """
        l = len(dta) # Länge nur 1 x berechnen
        return {k:round(v/l, 2) for (k,v) in Counter(dta).items()}
    
    @staticmethod
    def std_dev(lst: list)->float:
        """ Berechnet die Standardabweichung (standard deviation)

        Args:
            lst (list): Liste mit Werten

        Returns:
            float:  σ (sigma)
        """
        return sqrt(StatzAfoot.var(lst))
    
    @staticmethod
    def var(lst:list) ->float:
        """ Berechnet die Varianz (variance)
 
        Args:
            lst (list): _description_

        Returns:
            float: _description_
        """
        mean = sum(lst) / len(lst)
        return sum((x - mean) ** 2 for x in lst) / (len(lst) - 1)
    
    
    
