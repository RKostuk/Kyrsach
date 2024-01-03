import json
import os
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from app.core.config import ConfigInverIndex
from queue import Queue

class InvertedIndexProcessor:
    def __init__(self):
        self.directory = ConfigInverIndex.dir
        self.num_threads = ConfigInverIndex.thread
        self.inverted_index = defaultdict(lambda: {"count": 0, "data": []})

    def check_file_exists(self, file_path):
        return os.path.exists(file_path)

    def process_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file_content:
            content = file_content.read()
            words = re.findall(r'\b\w+\b', content.lower())

            for position, word in enumerate(words):
                if len(word) > 2:
                    self.inverted_index[word]["count"] += 1
                    self.inverted_index[word]["data"].append({
                        "dir": os.path.relpath(os.path.dirname(file_path), self.directory),
                        "file": os.path.basename(file_path),
                        "count": words.count(word),
                        "positions": [pos for pos, w in enumerate(words) if w == word]
                    })

    def process_files(self, file_queue):
        while True:
            file_path = file_queue.get()
            if file_path is None:
                break
            self.process_file(file_path)
            file_queue.task_done()

    def process_directory(self):
        if not self.check_file_exists(self.directory):
            print(f"Директорії {self.directory} не існує.")
            return None

        file_queue = Queue()

        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            files = [os.path.join(root, file) for root, dirs, files in os.walk(self.directory) for file in files]
            for file_path in files:
                file_queue.put(file_path)

            for _ in range(self.num_threads):
                executor.submit(self.process_files, file_queue)

            file_queue.join()

            for _ in range(self.num_threads):
                file_queue.put(None)

    def get_inverted_index(self):
        return self.inverted_index


if __name__ == "__main__":
    index_processor = InvertedIndexProcessor()
    start_time = time.time()
    index_processor.process_directory()
    end_time = time.time()
    inverted_index = index_processor.get_inverted_index()
    print(f"Витрачено часу: {end_time - start_time:.2f} секунд")

    with open("result2.json", "w", encoding="utf-8") as file:
        json.dump(inverted_index, file, ensure_ascii=False, indent=4)