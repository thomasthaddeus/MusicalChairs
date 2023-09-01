"""logs_cl.py

This module cleans the log files in the logs directory.

Specifically, it combines all the log files into one file and adds a breakdown of each log file.
"""


class CleanLogs:
    def __init__(self):
        """
        Initialize the CleanLogs class.
        """
        pass

    def combine_logs(self):
        """
        Combine all the log files into one file and add a breakdown of each log
        file.
        """
        log_files = self.get_log_files()
        self.combine_log_files(log_files)
        self.add_log_breakdown(log_files)

    def get_log_files(self):
        """
        Retrieve the log files.

        Returns:
            list: List of log file contents.
        """
        filenames = [
            "logs/with_classes.log",
            "logs/with_heapq.log",
            "logs/with_sort.log",
            "logs/with_zip_sorted.log",
        ]
        return [self.read_log_file(filename) for filename in filenames]

    def read_log_file(self, filename):
        """
        Read the content of a log file.

        Args:
            filename (str): Path to the log file.

        Returns:
            str: Content of the log file.
        """
        with open(filename, "r", "utf-8") as file:
            return file.read()

    def combine_log_files(self, log_files):
        """
        Combine the log files.

        Args:
            log_files (list): List of log file contents.
        """
        with open("logs/combined.log", "w", "utf-8") as combined_log_file:
            for log_file_content in log_files:
                combined_log_file.write(log_file_content)

    def add_log_breakdown(self, log_files):
        """
        Add a breakdown of each log file.

        Args:
            log_files (list): List of log file contents.
        """
        log_file_breakdown = self.get_log_file_breakdown(log_files)
        self.append_log_file_breakdown(log_file_breakdown)

    def append_log_file_breakdown(self, log_file_breakdown):
        """
        Append the log file breakdown to the combined log file.

        Args:
            log_file_breakdown (list): List of log file breakdowns.
        """
        with open("logs/combined.log", "a", "utf-8") as combined_log_file:
            combined_log_file.write("\n\nLog file breakdown:\n\n")
            for breakdown in log_file_breakdown:
                combined_log_file.write(breakdown)

    def get_log_file_breakdown(self, log_files):
        """
        Retrieve the log file breakdown.

        Args:
            log_files (list): List of log file contents.

        Returns:
            list: List of log file breakdowns.
        """

        # For the purpose of this example, I'm assuming a placeholder function.
        # You might want to replace this with the actual implementation.
        def get_breakdown_for_log_file(log_file_content):
            """Example: return the first 100 characters"""
            return log_file_content[:100]

        return [get_breakdown_for_log_file(content) for content in log_files]
