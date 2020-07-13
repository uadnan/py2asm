import threading

_state = threading.local()


class LeafBlock:
    def __init__(self, should_register=True):
        if should_register:
            _state.active_block.append(self)
        super().__init__()

    def render(self):
        raise NotImplementedError()


class BlockBase:
    def __init__(self):
        self.children = []

        self.parent = getattr(_state, 'active_block', None)
        if self.parent is None:
            self.root = self
        else:
            self.root = self.parent.root
            self.parent.append(self)

    def __enter__(self):
        _state.active_block = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _state.active_block = self.parent

    def append(self, child):
        self.children.append(child)


class Block(BlockBase):
    template = '{children}'

    def __init__(self):
        super().__init__()

        if self.parent is None:
            self.indent = 0
        else:
            self.indent = self.parent.indent + 1

    def render(self):
        return self.template.format(children=self.render_children())

    def render_children(self):
        lines = '\n'.join(c.render() for c in self.children).split('\n')
        return '\n'.join(
            ('    ' * self.indent) + line
            for line in lines
        )
