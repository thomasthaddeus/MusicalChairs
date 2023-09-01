import logging
import re

class LogCombiner:
    def __init__(self, *log_files):
        """
        Initialize the LogCombiner class.

        Args:
            *log_files (str): Paths to the log files to be combined.
        """
        self.log_files = log_files

    def read_log_file(self, filename):
        """
        Read the content of a log file.

        Args:
            filename (str): Path to the log file.

        Returns:
            str: Content of the log file.
        """
        with open(filename, 'r', "utf-8") as file:
            return file.read()

    def get_stats(self, content):
        """
        Get statistics for the log content.

        Args:
            content (str): Content of the log file.

        Returns:
            dict: Dictionary containing statistics.
        """
        lines = content.split("\n")
        num_lines = len(lines)
        num_chars = sum(len(line) for line in lines)
        num_words = sum(len(line.split()) for line in lines)

        return {
            "Number of lines": num_lines,
            "Number of characters": num_chars,
            "Number of words": num_words
        }

    def format_log_file(self, filename, content):
        """
        Format the log file content with the filename centered between dashes and add stats.

        Args:
            filename (str): Name of the log file.
            content (str): Content of the log file.

        Returns:
            str: Formatted log content.
        """
        # Extract the name of the log file without the path and extension
        name = filename.split('/')[-1].split('.')[0]
        header = "# " + name.center(76, '-') + " #"

        stats = self.get_stats(content)
        stats_str = "\n".join([f"{key}: {value}" for key, value in stats.items()])

        return header + "\n" + stats_str + "\n\n" + content + "\n\n\n"

    def combine_logs(self):
        """
        Combine all the log files with the desired formatting.

        Returns:
            str: Combined log content.
        """
        combined_log = "******* Combined Test Run Logs*******\n\n"
        for filename in self.log_files:
            content = self.read_log_file(filename)
            formatted_content = self.format_log_file(filename, content)
            combined_log += formatted_content
        return combined_log

    def write_to_file(self, output_filename):
        """
        Write the combined logs to an output file.

        Args:
            output_filename (str): Name of the output file.
        """
        with open(output_filename, 'w', "utf-8") as file:
            file.write(self.combine_logs())

class StatsHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.stats = {
            "DEBUG": 0,
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0
        }

    def emit(self, record):
        self.stats[record.levelname] += 1

    def get_stats(self):
        return self.stats


def extract_execution_times(log_file_path):
    """
    Extract execution times from a log file.

    Args:
        log_file_path (str): Path to the log file.

    Returns:
        list: List of execution times extracted from the log file.
    """
    execution_times = []
    with open(log_file_path, 'r', "utf-8") as file:
        for line in file:
            match = re.search(r"Execution time: (\d+\.\d+)", line)
            if match:
                execution_times.append(float(match.group(1)))
    return execution_times


# Example usage:
log_combiner = LogCombiner("logs/with_classes.log", "logs/with_heapq.log")
log_combiner.write_to_file("logs/combined.log")

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Add the stats handler to the logger
stats_handler = StatsHandler()
logger.addHandler(stats_handler)

# Example log messages
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

# Example usage:
log_file_path = "app/logs/class.log"
execution_times = extract_execution_times(log_file_path)
avg_time = sum(execution_times) / len(execution_times)

# Print the statistics
print(stats_handler.get_stats())
print(f"Average Execution Time for {log_file_path}: {avg_time:.4f} seconds")
