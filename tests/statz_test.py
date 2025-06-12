from mypkg.statz import StatPy
import statistics
import unittest


class TestStatPy(unittest.TestCase):
    """ Unit testing StatPy class versus statistics.* """

    def test_median(self):
        
        income = [30000, 5000, 6000, 3000, 4000, 5000, 5000, 8000, 6000]
        median = StatPy.med(income)
        median_stat = statistics.median(income)
        avg = StatPy.avg(income)
        avg_stat = statistics.mean(income)
        mode = StatPy.mode(income)
        mode_stat = statistics.mode(income)
        self.assertEqual(median_stat, median_stat, "Fehler!")
        self.assertEqual(avg_stat, avg_stat, "Fehler!")
        self.assertEqual(mode, mode_stat, "Fehler!")

    def test_stdev_var(self):

        dta = [5.2, 6.6, 4.8, 7.2, 6.2, 6.0]
        self.assertEqual(StatPy.var(dta), statistics.variance(dta), "Fehler!")
        self.assertEqual(StatPy.avg(dta), statistics.mean(dta), "Fehler!")
        self.assertEqual(StatPy.std_dev(dta), statistics.stdev(dta), "Fehler!")
