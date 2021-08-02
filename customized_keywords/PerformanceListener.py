import csv
import os.path

from os import path

class PerformanceListener(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, filename = 'performance_output.csv'):
        self.ROBOT_LIBRARY_LISTENER = self
        self.filename = filename

    def end_test(self, name, attrs):
        elapsedtime = attrs['elapsedtime']/1000.00
        if not path.exists(self.filename):
            test_file = open(self.filename, 'w')
            test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            test_writer.writerow(['TEST CASE','STATUS','TIME TAKEN','START TIME','END TIME'])
        if elapsedtime > 0.005:
            print "%s => status: %s, elapsed time: %s s" % (name, attrs['status'], elapsedtime)

            with open(self.filename, mode='a') as test_file:
                test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if elapsedtime >= 60:
                    elapsedtime = elapsedtime/60.00
                    test_writer.writerow([name, attrs['status'], str(round(elapsedtime,2)) + ' min', attrs['starttime'], attrs['endtime']])
                else:
                    test_writer.writerow([name, attrs['status'], str(round(elapsedtime,2)) + ' s', attrs['starttime'], attrs['endtime']])
                test_file.close()