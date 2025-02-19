import string
import sys
from file_generator import FileGenerator
from map_reduce_controller import MapReduceController
from map_reduce_grep import MapReduceGrepController

file_gen = FileGenerator(
    split=3,
    N=100,
    alphabet=list(string.ascii_lowercase),
    min_size=2,
    max_size=5
)

file_gen.generate_files()

# Opções do usuário
if len(sys.argv) < 2:
    print("❌ Uso correto: python main.py <modo> [padrão]")
    print("Modos disponíveis: 'wordcount' ou 'grep'")
    sys.exit(1)

mode = sys.argv[1]

if mode == "wordcount":
    print("📝 Executando contagem de palavras...")
    controller = MapReduceController(directory="text_parts")
    result = controller.execute()
    print("\n📄 Contagem de frequência de palavras:")
    for word, count in result.items():
        print(f"{word}: {count}")

elif mode == "grep":
    if len(sys.argv) < 3:
        print("❌ Para usar grep, forneça um padrão. Exemplo: python main.py grep 'foo'")
        sys.exit(1)

    pattern = sys.argv[2]
    print(f"🔍 Executando grep para o padrão: {pattern}")
    controller = MapReduceGrepController(directory="text_parts", pattern=pattern)
    result = controller.execute()
    print("\n📄 Linhas que correspondem ao padrão:")
    print(result)

else:
    print("❌ Modo inválido! Use 'wordcount' ou 'grep'.")
    sys.exit(1)