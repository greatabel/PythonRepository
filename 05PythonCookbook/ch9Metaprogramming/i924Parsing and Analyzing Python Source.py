x = 42
print( eval('2 + 3*4 + x') )

exec("for i in range(10): print('i=',i)" )

import ast
ex = ast.parse('2 + 3*4 + x', mode='eval')
print( ast.dump(ex) )

top = ast.parse('for i in range(10): print(i)', mode='exec')
print( top )
print( ast.dump(top) )
exec(compile(top,'<stdin>', 'exec'))

class CodeAnlyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


if __name__ == '__main__':

    code = '''
for i in range(10): 
    print(i)
del i
'''

    top = ast.parse(code, mode='exec')

    c = CodeAnlyzer()
    c.visit(top)
    print('loaded:', c.loaded)
    print('stored:', c.stored)
    print('deleted:', c.deleted)

