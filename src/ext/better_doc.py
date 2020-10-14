"""
    .. better-doc:: cylc.flow.batch_sys_handlers
"""

import pkgutil

from docutils.parsers.rst import Directive
from docutils.statemachine import StringList

from sphinx import addnodes

__version__ = '1.0.0'


def iter_package(namespace):
    package = __import__(namespace)
    for module in pkgutil.iter_modules(package.__path__):
        imp = __import__(namespace)
        yield (
            ('package' if module.ispkg else 'module'),
            imp
        )


def visit_package(package):
    return [
        '',
        f'.. automodule:: {package.name}'
        '',
    ]


def visit_module(module):
    return [
        '',
        f'.. automodule:: {module.name}',
        '   :members:'
        ''
    ]


VISITORS = {
    'package': visit_package,
    'module': visit_module
}


class BetterDocDirective(Directive):
    has_content = False
    option_spec = {}
    required_arguments = 1
    optional_arguments = 0

    def run(self):
        namespace = self.arguments[0]

        content = []
        for typ, item in iter_package(namespace):
            content.extend(
                VISITORS[typ](item)
            )

        node = addnodes.desc_content()
        self.state.nested_parse(
            StringList(content),
            self.content_offset,
            node
        )

        return [node]


def setup(app):
    app.add_directive('better-doc', BetterDocDirective)
    return {'version': __version__, 'parallel_read_safe': True}
