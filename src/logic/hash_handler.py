import hashlib
import mmap
import os


def get_256_sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        with mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) as mm:
            h.update(mm)
    return h.hexdigest()


class HashHandler:
    def __init__(self):
        self.root_path = "/app/tmp/"
        self.file_path = "app/tmp/storage/"
        self.file_path_handler = "app/tmp/handlers/"
        self.hashes = {}

    def setup(self):
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)
        if not os.path.exists(self.file_path_handler):
            os.makedirs(self.file_path_handler)

        for file in os.listdir(self.file_path):
            if file not in self.hashes:
                self.hashes[file] = get_256_sum(self.file_path + file)

    def get_hash(self, filename):
        return self.hashes[filename]

    def update_hash(self, filename):
        self.hashes[filename] = get_256_sum(self.file_path + filename)

    def save_hashes(self):
        with open(self.file_path + "hashes.json", "w") as hash_file:
            hash_file.write(str(self.hashes))

hash_handler = HashHandler()