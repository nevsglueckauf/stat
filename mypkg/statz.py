from collections import Counter

class StatPy:
    """ Ein wenig Spielerei mit Statistik ohne weitere Libs (außer collections 😎)
    
    """
    
    def rel_freq(self, dta:list)->dict:
        """ Berechnet die relative Häufigkeit

        Args:
            dta (list): Liste mit Werten 

        Returns:
            dict: {'val_1': rl_frq_1, ... 'val_n': rl_frq_n'}
        """
        l = len(dta) # Länge nur 1 x berechnen
        return {k:round(v/l, 2) for (k,v) in Counter(dta).items()}