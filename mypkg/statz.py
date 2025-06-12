# AUTHOR Sven Schrodt
# SINCE 2025-06-11
from collections import Counter
from math import sqrt

class StatzAfoot:
    """ Ein wenig Spielerei mit Statistik ohne weitere Libs (außer collections und math.sqrt 😎)
        - afoot („zu Fuß“ halt)
    
    """
    @staticmethod
    def mode(lst:list) ->list:
        """ Berechnet den Modus 
        Args:
            lst (list): Liste mit Zahlen, deren Modus/Modi ermittelt werden soll

        Returns:
            _type_: Liste von Werten, die am häufigsten in dta vorkommen
        """
        ctd = Counter(lst)
        max_id = max(ctd.values())
        return [k for (k, v) in ctd.items() if v == max_id]
    
    @staticmethod
    def med(lst:list) ->float:
        """ Median berechnen

        Args:
            lst (list): Liste mit Zahlen, deren Median ermittelt werden soll

        Returns:
            _type_: Median (auch: Zentralwert)
        """
        lst.sort() # sortiere die Werte
        mid = len(lst) // 2 # finde die Mitte (absolut, oder erstes Element, falls gerade Anzahl an Elementen)
        if len(lst) % 2 == 0: # gerade Anzahl an Elementen
            return sum(lst[mid-1:mid+1]) / 2 # slice für die Mitte - wenn gerade Anzahl an Elementen
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
            dta (list): Liste von Werten

        Returns:
            dict: {'val_1': rl_frq_1, ... 'val_n': rl_frq_n'}
        """
        l = len(dta) # Länge nur 1 x berechnen
        return {k:round(v/l, 2) for (k,v) in Counter(dta).items()}
    
    @staticmethod
    def std_dev(lst: list)->float:
        """ Berechnet die Standardabweichung (standard deviation)

        Args:
            lst (list): Liste von Werten

        Returns:
            float:  σ (sigma)
        """
        return sqrt(StatzAfoot.var(lst))
    
    @staticmethod
    def var(lst:list) ->float:
        """ Berechnet die Varianz (variance)
 
        Args:
            lst (list): Liste von Werten

        Returns:
            float: σ^2 (sigma^2)
        """
        mean = StatzAfoot.avg(lst) # Mittel nur 1 x berechnen
        return sum((x - mean) ** 2 for x in lst) / (len(lst) - 1)
    
    @staticmethod
    def st_rng(lst:list) ->float:
        """ Berechnet die Spannweite (statistics range)

        Args:
            lst (list): Liste von Werten

        Returns:
            float: R (= x_{max} - x_{min})
        """
        return max(list) - min(lst)
        
    
    
    
