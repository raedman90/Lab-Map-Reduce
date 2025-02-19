import re
import threading
import glob

def map_function(file_path, pattern, temp_result):
    with open(file_path, 'r') as f:
        for line in f:
            if re.search(pattern, line):
                with threading.Lock():
                    temp_result.append(line.strip())

def reduce_function(results):
    return "\n".join(results)

class MapReduceGrepController:
    def __init__(self, directory, pattern):
        self.directory = directory
        self.pattern = pattern
        self.temp_result = []

    def run_map_phase(self):
        threads = []
        for file_path in glob.glob(f"{self.directory}/*.txt"):
            thread = threading.Thread(target=map_function, args=(file_path, self.pattern, self.temp_result))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def run_reduce_phase(self):
        return reduce_function(self.temp_result)

    def execute(self):
        print("🔍 Rodando fase Map...")
        self.run_map_phase()
        print("📝 Rodando fase Reduce...")
        return self.run_reduce_phase()
