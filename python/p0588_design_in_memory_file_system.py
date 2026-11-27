class _Directory:
    def __init__(self):
        self.children = {}


class _File:
    def __init__(self):
        self.chunks = []


def _parts(path):
    return path[1:].split('/') if path != '/' else []


class FileSystem:
    def __init__(self):
        self.root = _Directory()

    def _resolve(self, path):
        node = self.root
        for name in _parts(path):
            node = node.children[name]
        return node

    def ls(self, path):
        node = self._resolve(path)
        if isinstance(node, _File):
            return [path.rsplit('/', 1)[1]]
        return sorted(node.children)

    def mkdir(self, path):
        node = self.root
        for name in _parts(path):
            if name not in node.children:
                node.children[name] = _Directory()
            node = node.children[name]

    def addContentToFile(self, filePath, content):
        parent_path, name = filePath.rsplit('/', 1)
        parent = self._resolve(parent_path or '/')
        if name not in parent.children:
            parent.children[name] = _File()
        parent.children[name].chunks.append(content)

    def readContentFromFile(self, filePath):
        return ''.join(self._resolve(filePath).chunks)
