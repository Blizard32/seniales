# Ejecutor de tests para la librería seniales
import importlib.util
import sys
import os

def run_tests():
    test_dir = os.path.join(os.path.dirname(__file__), "test")
    test_files = [f for f in os.listdir(test_dir) if f.startswith("test_") and f.endswith(".py")]
    
    for test_file in test_files:
        test_path = os.path.join(test_dir, test_file)
        spec = importlib.util.spec_from_file_location("test_module", test_path)
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)
        print(f"Tests completados para {test_file}")

if __name__ == "__main__":
    run_tests()
