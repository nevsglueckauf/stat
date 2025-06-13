# AUTHOR Sven Schrodt
# SINCE 2025-06-10
class MathZwo:
    """ Dinge zu  „zu Fuß“ berechnen """
    
    @staticmethod
    def factorial(n:int) ->int:
        """ Berechnung der Fakultät (factorial)
        
            -$ n!=n⋅(n−1)⋅(n−2)⋅…⋅1$

        Args:
            n (int): _descrZAhl, deren Fakultät berrechnet werden soll

        Returns:
            int: Fakultät von n
        """
        if(n==0) or (n==1):
            return 1
        else:
            return n * MathZwo.factorial(n-1)
