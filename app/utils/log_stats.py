import os
import re
import logging


class LogStats:
    def __init__(self, log_file_path):
        self.log_f_path = log_file_path
        self.exec_times = self.xtrct_exec_times()

    def xtrct_exec_times(self):
        """
        Extract execution times from the log file.
        """
        exec_times = []
        with open(file=self.log_f_path, mode="r", encoding="utf-8") as file:
            for line in file:
                match = re.search(r"Execution time: (\d+\.\d+)", line)
                if match:
                    exec_times.append(float(match.group(1)))
        return exec_times

    def avg_exec_time(self):
        return (
            sum(self.exec_times) / len(self.exec_times)
            if self.exec_times
            else 0
        )

    def max_exec_time(self):
        return max(self.exec_times, default=0)

    def min_exec_time(self):
        return min(self.exec_times, default=0)

    def ttl_exec_time(self):
        return sum(self.exec_times)


class CleanLogs:
    def __init__(self, log_dir="app/logs"):
        self.log_dir = log_dir

    def combine_logs(self):
        cmbd_logp = os.path.join(self.log_dir, "combined.log")
        with open(file=cmbd_logp, mode="w", encoding="utf-8") as cmbd_logf:
            self._write_header(cmbd_logf)
            for log_file in os.listdir(self.log_dir):
                log_path = os.path.join(self.log_dir, log_file)
                if os.path.isfile(log_path) and log_path != cmbd_logp:
                    self._process_individual_log(log_path, cmbd_logf)

    def _write_header(self, file):
        file.write("******* Combined Test Run Logs*******\n\n")

    def _process_individual_log(self, log_path, cmbd_logf):
        stats = LogStats(log_path)
        self._write_log_header(log_path, cmbd_logf)
        self._write_log_content(log_path, cmbd_logf)
        self._write_log_stats(stats, cmbd_logf)

    def _write_log_header(self, log_path, file):
        name = os.path.basename(log_path)
        name = name.split('/')[-1].split('.')[0]
        name = name.append(" TEST RUN #")
        dash_len = (64 - len(name)) // 2
        header = f"# {'-'*dash_len} {name} {'-'*dash_len} #\n"
        file.write(header)
        file.write("\n\n")

    def _write_log_content(self, log_path, file):
        with open(file=log_path, mode="r", encoding="utf-8") as indvl_log:
            file.writelines(indvl_log.readlines())
        file.write("\n\n")

    def _write_log_stats(self, stats, file):
        file.write(
            f"Average Execution Time: {stats.avg_exec_time():.4f} seconds\n"
        )
        file.write(
            f"Max Execution Time: {stats.max_exec_time():.4f} seconds\n"
        )
        file.write(
            f"Min Execution Time: {stats.min_exec_time():.4f} seconds\n"
        )
        file.write(
            f"Total Execution Time: {stats.ttl_exec_time():.4f} seconds\n"
        )
        file.write("\n\n")


# Example usage:
cleaner = CleanLogs()
cleaner.combine_logs()
