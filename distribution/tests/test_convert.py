import jadn
import os
import unittest


# TODO: Read and Write JIDL and HTML, Write Markdown, JSON Schema, XSD, CDDL
dir_path = os.path.abspath(os.path.dirname(__file__))
quickstart_schema = {
    'types': [
        ['Person', 'Record', [],
         'JADN equivalent of structure from https://developers.google.com/protocol-buffers', [
             [1, 'name', 'String', [], ''],
             [2, 'id', 'Integer', [], ''],
             [3, 'email', 'String', ['/email', '[0'], '']]]]
    }


class BasicConvert:
    def _convert(self, schema):
        raise NotImplemented(f'The unittest class `{self.__class__.__name__}` should implement _convert')

    def test_0_quickstart(self):
        self._convert(jadn.check(quickstart_schema))

    def test_1_types(self):
        self._convert(jadn.load(os.path.join(dir_path, 'convert_types.jadn')))

    def test_2_jadn(self):
        self._convert(jadn.load(os.path.join(jadn.data_dir(), 'jadn_v1.0_schema.jadn')))

    def test_3_examples(self):
        self._convert(jadn.load(os.path.join(dir_path, 'jadn-v1.0-examples.jadn')))


class HtmlConvert(BasicConvert, unittest.TestCase):
    def _convert(self, schema):
        html_doc = jadn.convert.html_dumps(schema)
        schema_new = jadn.convert.html_loads(html_doc)
        self.assertEqual(jadn.canonicalize(schema), jadn.canonicalize(schema_new))


class JidlConvert(BasicConvert, unittest.TestCase):
    def _convert(self, schema):
        jidl_doc = jadn.convert.jidl_dumps(schema)
        schema_new = jadn.convert.jidl_loads(jidl_doc)
        self.maxDiff = None
        self.assertEqual(jadn.canonicalize(schema), jadn.canonicalize(schema_new))


# TODO: Read formats
class MarkdownConvert(BasicConvert, unittest.TestCase):
    def _convert(self, schema):
        fmt = jadn.convert.ConversionFormats.MarkDown
        markdown_doc = jadn.convert.table_dumps(schema, fmt)
        # schema_new = jadn.convert.table_loads(markdown_doc, fmt)
        # self.maxDiff = None
        # self.assertEqual(jadn.canonicalize(schema), jadn.canonicalize(schema_new))


class CddlConvert(BasicConvert, unittest.TestCase):
    def _convert(self, schema):
        fmt = jadn.convert.ConversionFormats.CDDL
        cddl_doc = jadn.convert.table_dumps(schema, fmt)
        # schema_new = jadn.convert.table_loads(cddl_doc, fmt)
        # self.maxDiff = None
        # self.assertEqual(jadn.canonicalize(schema), jadn.canonicalize(schema_new))


if __name__ == '__main__':
    unittest.main()
