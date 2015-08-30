import sys
import os.path
# print('#',os.path.pardir)
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'foo-package'))
    )
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'bar-package'))
    )


# sys.path.extend(['foo-package', 'bar-package'])
import spam.blah
import spam.grok
