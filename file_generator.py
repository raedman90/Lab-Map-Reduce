import random
import os

class FileGenerator:
    def __init__(self, split, N, alphabet, min_size, max_size):
        self.split = split
        self.N = N
        self.alphabet = alphabet
        self.min_size = min_size
        self.max_size = max_size

    def generate_files(self):
        words = [
            ''.join(random.choices(self.alphabet, k=random.randint(self.min_size, self.max_size)))
            for _ in range(self.N)
        ]
        chunk_size = len(words) // self.split
        os.makedirs("text_parts", exist_ok=True)

        for i in range(self.split):
            with open(f"text_parts/part_{i}.txt", "w") as f:
                part = words[i * chunk_size : (i + 1) * chunk_size]
                f.write(' '.join(part))
