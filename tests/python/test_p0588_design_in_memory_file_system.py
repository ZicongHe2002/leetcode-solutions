import random
import unittest

from python.p0588_design_in_memory_file_system import FileSystem


class FlatPathModel:
    def __init__(self):
        self.directories = {'/'}
        self.files = {}

    def mkdir(self, path):
        prefix = ''
        for name in path[1:].split('/'):
            prefix += '/' + name
            self.directories.add(prefix)

    def addContentToFile(self, path, content):
        self.files[path] = self.files.get(path, '') + content

    def readContentFromFile(self, path):
        return self.files[path]

    def ls(self, path):
        if path in self.files:
            return [path.rsplit('/', 1)[1]]
        prefix = path.rstrip('/') + '/'
        names = set()
        for candidate in self.directories | self.files.keys():
            if candidate.startswith(prefix):
                remainder = candidate[len(prefix):]
                if remainder:
                    names.add(remainder.split('/', 1)[0])
        return sorted(names)


def child_path(parent, name):
    return parent.rstrip('/') + '/' + name


class MemoryFileSystemTests(unittest.TestCase):
    def test_hundred_seeded_traces_of_three_hundred_legal_operations(self):
        calls = 0
        for seed in range(100):
            rng = random.Random(seed)
            system, model = FileSystem(), FlatPathModel()
            operations = set()
            for step in range(300):
                files = sorted(model.files)
                directories = sorted(model.directories)
                if step >= 250:
                    action = rng.choice(('readContentFromFile', 'ls')) if files else 'ls'
                else:
                    action = rng.choice(('mkdir', 'addContentToFile', 'readContentFromFile', 'ls'))
                    if action == 'readContentFromFile' and not files:
                        action = 'ls'
                name = chr(97 + step // 26) + chr(97 + step % 26)
                if action == 'mkdir':
                    base = rng.choice([path for path in directories if path.count('/') <= 2])
                    path = child_path(base, 'd' + name)
                    if rng.randrange(2):
                        path = child_path(path, 'n' + name)
                    self.assertNotIn(path, model.directories)
                    arguments = (path,)
                elif action == 'addContentToFile':
                    if files and rng.randrange(2):
                        path = rng.choice(files)
                    else:
                        path = child_path(rng.choice(directories), 'f' + name)
                    content = ''.join(rng.choice('abc') for _ in range(rng.randint(1, 50)))
                    arguments = (path, content)
                elif action == 'readContentFromFile':
                    arguments = (rng.choice(files),)
                else:
                    arguments = (rng.choice(directories + files),)
                self.assertLessEqual(len(arguments[0]), 100)
                expected = getattr(model, action)(*arguments)
                actual = getattr(system, action)(*arguments)
                self.assertEqual(actual, expected, (seed, step, action, arguments))
                operations.add(action)
                calls += 1
            self.assertEqual(operations, {'mkdir', 'ls', 'addContentToFile', 'readContentFromFile'})
        self.assertEqual(calls, 30000)

    def test_roots_listing_isolation_and_maximum_path_append_calls(self):
        system = FileSystem()
        self.assertEqual(system.ls('/'), [])
        self.assertIsNone(system.mkdir('/z/a'))
        system.mkdir('/a')
        self.assertEqual(system.ls('/'), ['a', 'z'])
        system.addContentToFile('/z/a/file', 'abc')
        listing = system.ls('/z/a/file')
        self.assertEqual(listing, ['file'])
        listing.append('fake')
        self.assertEqual(system.ls('/z/a/file'), ['file'])
        directory_listing = system.ls('/z/a')
        directory_listing.clear()
        self.assertEqual(system.ls('/z/a'), ['file'])
        system.addContentToFile('/z/a/file', 'def')
        self.assertEqual(system.readContentFromFile('/z/a/file'), 'abcdef')
        system.mkdir('/a/b')
        system.addContentToFile('/a/b/file', 'xyz')
        self.assertEqual(system.readContentFromFile('/a/b/file'), 'xyz')
        self.assertEqual(system.readContentFromFile('/z/a/file'), 'abcdef')
        self.assertEqual(FileSystem().ls('/'), [])
        bounded = FileSystem()
        directory = '/' + 'a' * 97
        file_path = directory + '/b'
        self.assertEqual(len(file_path), 100)
        bounded.mkdir(directory)
        for _ in range(297):
            bounded.addContentToFile(file_path, 'x' * 50)
        self.assertEqual(bounded.readContentFromFile(file_path), 'x' * (297 * 50))
        self.assertEqual(bounded.ls(file_path), ['b'])


if __name__ == '__main__':
    unittest.main()
