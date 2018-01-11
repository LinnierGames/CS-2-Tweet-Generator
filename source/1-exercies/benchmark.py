from datetime import datetime as date
import sys, os


class Benchmark(object):

    def __init__(self, closure=None):
        """
        :param closure: passing in a function allows you to get an average of executions. Use .fire() when using a
        closure else just use .begin() and .end_and_print_results()
        """
        self._start_stamp = None
        self._end_stamp = None
        self._closure = closure

        self._average = None
        self._iterations = None

    def __str__(self):
        benchmark_value = self.get_benchmark_value
        if benchmark_value is not None:
            if self._closure is not None:
                average = self._average
                iterations = self._iterations
                return "For total of {} iterations, the average was {}s".format(self._iterations, self._average)
            else:
                return "{}; execution duration at {}s".format(self.get_end_time, benchmark_value)
        else:
            return "start and end times are not set"

    @property
    def get_start_time(self):
        if self._start_stamp is not None:
            return str(self._start_stamp)
        else:
            return "start time is not set"

    @property
    def get_end_time(self):
        if self._end_stamp is not None:
            return str(self._end_stamp)
        else:
            return "end time is not set"

    @property
    def get_benchmark_value(self):
        if self._start_stamp is not None and self._end_stamp is not None:
            return self._end_stamp - self._start_stamp
        return None

    def begin(self):
        self._start_stamp = date.now()

    def begin_and_print(self):
        self.begin()
        print self._start_stamp

    def end(self):
        self._end_stamp = date.now()

    def end_and_print_result(self):
        self.end()
        print self

    def fire(self, nBenchmarks):
        """
        print the average of nBenchmarks. All print statements are silent during benchmarking the average
        :param nBenchmarks: how many times to test the self._closure
        """

        # Disable
        def blockPrint():
            sys.stdout = open(os.devnull, 'w')

        # Restore
        def enablePrint():
            sys.stdout = sys.__stdout__
            
        self.begin()
        sum_duration = 0
        for test_number in range(0, nBenchmarks):
            function_to_call = self._closure
            benchmark = Benchmark()
            benchmark.begin()
            blockPrint()
            function_to_call()
            enablePrint()
            benchmark.end()
            sum_duration += benchmark.get_benchmark_value.microseconds/100000.0

        self._average = sum_duration / nBenchmarks
        self._iterations = nBenchmarks
        self.end_and_print_result()
