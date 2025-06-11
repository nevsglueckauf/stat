# AUTHOR Sven Schrodt
# SINCE 2025-06-11
from collections import Counter

class StatPy:
    """ Ein wenig Spielerei mit Statistik ohne weitere Libs (außer collections 😎)
    
    """
    @staticmethod
    def clc_mode(lst:list):
        """ Berechnet den Modus 
        Args:
            lst (list): iste mit Zahlen, deren Modus/Modi ermittelt werden soll

        Returns:
            _type_: _description_
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
        """ Berechnet das arithmetische Mittel

        Args:
            lst (list): Liste mit Zahlen, deren Mittel ermittelt werden soll

        Returns:
            float: _description_
        """
        return sum(lst) / len(lst)
    
    @staticmethod
    def rel_freq(dta:list)->dict:
        """ Berechnet die relative Häufigkeit

        Args:
            dta (list): Liste mit Werten 

        Returns:
            dict: {'val_1': rl_frq_1, ... 'val_n': rl_frq_n'}
        """
        l = len(dta) # Länge nur 1 x berechnen
        return {k:round(v/l, 2) for (k,v) in Counter(dta).items()}
    

