import hashlib
import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import ci

class DocsifyTests(unittest.TestCase):
    def make(self,text,**changes):
        entry=ci.entries(text)[0]
        data=dict(entries=[entry],readme=text,readmeHash=hashlib.sha256(text.encode()).hexdigest(),catalogSha='a'*40,slice=0,sliceCount=1)
        row=dict(id=entry['id'],action='update',reason='Official docs establish correction.',evidence=[dict(url='https://example.com',observation='Official source')],limitations=[],blockers=[],newName=None,newUrl=None,newDescription=None)
        row.update(changes)
        return data,dict(results=[row])
    def test_rename_keeps_existing_append_order(self):
        data,raw=self.make('## Plugins\n- [Zed](https://z.example) - Plugin.\n- [Middle](https://m.example) - Plugin.\n',newName='Alpha')
        patch=ci.previews(data,raw,'unchanged')[0][0]['patch']
        self.assertIn('+- [Alpha]',patch)
        self.assertNotIn('-- [Middle]',patch)
    def test_enterprise_prefix_preserved(self):
        data,raw=self.make('## Enterprise Usage\n- Netflix - [Polly.js](https://old.example/) - Tool.\n',newUrl='https://new.example/')
        self.assertIn('+- Netflix - [Polly.js](https://new.example/)',ci.previews(data,raw,'unchanged')[0][0]['patch'])
    def test_enterprise_missing_description_preserved(self):
        data,raw=self.make('## Enterprise Usage\n- Qiniu - [pandora](https://old.example/)\n',newUrl='https://new.example/')
        patch=ci.previews(data,raw,'unchanged')[0][0]['patch']
        self.assertIn('+- Qiniu - [pandora](https://new.example/)\n',patch)
    def test_author_reference_survives_url_change(self):
        data,raw=self.make('## Plugins\n- [Tool](https://old.example/) - Plugin ([@author][1]).\n\n[1]: https://github.com/author\n',newUrl='https://new.example/')
        self.assertIn('Plugin ([@author][1]).',ci.previews(data,raw,'unchanged')[0][0]['patch'])
    def test_existing_parenthesized_name_allows_url_update(self):
        data,raw=self.make('## Showcase\n- [google-spreadsheet (npm module)](https://old.example/) - Docs.\n',newUrl='https://new.example/')
        self.assertIn('google-spreadsheet (npm module)',ci.previews(data,raw,'unchanged')[0][0]['patch'])
    def test_cross_section_duplicate_identity_not_merged(self):
        rows=ci.entries('## Showcase\n- [Tool](https://example.com) - Site.\n## Plugins\n- [Tool](https://example.com) - Plugin.\n')
        self.assertEqual(len(rows),2)
        self.assertNotEqual(rows[0]['id'],rows[1]['id'])

if __name__=='__main__':unittest.main()
