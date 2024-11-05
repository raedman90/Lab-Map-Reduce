from collections import defaultdict
import threading
import glob

def map_function(file_path, temp_result):
    with open(file_path, 'r') as f:
        word_counts = defaultdict(int)
        for word in f.read().split():
            word_counts[word] += 1
    with threading.Lock():
        for word, count in word_counts.items():
            temp_result[word].append(count)

def reduce_function(word, counts):
    return word, sum(map(int, counts))

class MapReduceController:
    def __init__(self, directory):
        self.directory = directory
        self.temp_result = defaultdict(list)
        
    def run_map_phase(self):
        threads = []
        for file_path in glob.glob(f"{self.directory}/*.txt"):
            thread = threading.Thread(target=map_function, args=(file_path, self.temp_result))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
    
    def run_reduce_phase(self):
        threads = []
        final_result = {}
        for word, counts in self.temp_result.items():
            thread = threading.Thread(target=lambda w, c: final_result.update({w: reduce_function(w, c)}), args=(word, counts))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        return final_result

    def execute(self):
        print("Running Map phase...")
        self.run_map_phase()
        print("Running Reduce phase...")
        final_result = self.run_reduce_phase()
        return final_result
