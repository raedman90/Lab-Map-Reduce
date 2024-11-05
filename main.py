import string
from file_generator import FileGenerator
from map_reduce_controller import MapReduceController

file_gen = FileGenerator(
    split=3,
    N=100,
    alphabet=list(string.ascii_lowercase),
    min_size=2,
    max_size=5
)

file_gen.generate_files()

controller = MapReduceController(directory="text_parts")
result = controller.execute()

print("Contagem de frequência de palavras:")
for word, count in result.items():
    print(f"{word}: {count}")
