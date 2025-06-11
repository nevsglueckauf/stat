from mypkg.statz import StatPy
import statistics
import unittest

class TestStatPy(unittest.TestCase):
    """ Unit testing StatPy class versus statistics """
    
    def test_median(self):
        income = [30000, 5000, 6000, 3000, 4000, 5000, 5000, 8000, 6000]


        median = StatPy.clc_med(income)
        median_stat = statistics.median(income)
        avg = StatPy.clc_avg(income)
        avg_stat = statistics.mean(income)
        mode = StatPy.clc_mode(income)
        mode_stat = statistics.mode(income)
        self.assertEqual(median_stat, median_stat, 'Fehler!')
        self.assertEqual(avg_stat, avg_stat, 'Fehler!')
        self.assertEqual(mode, mode_stat, 'Fehler!')


