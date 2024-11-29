"""Unit tests for test_edreq12.py."""

import unittest
import json
import util
import edreq12 as edreq


class TestEDR(unittest.TestCase):
    __version__ = "testversion"
    util.args = util.parse_args(["--url", "https://example.com/"], __version__)
    util.logger = util.set_up_logging(
        args=util.args, logfile=util.args.log_file, version=__version__
    )

    def test_requrementA5_2(self):
        # Good tests
        jsondata = {}
        with open("testdata/edrisobaric_collection.json", "r", encoding="utf-8") as f:
            jsondata = json.load(f)
        ok, _ = edreq.requrementA5_2(jsondata)
        self.assertTrue(ok)

        # Bad tests
        jsondata = {}
        with open(
            "testdata/edrisobaric_collection_bad_bbox.json", "r", encoding="utf-8"
        ) as f:
            jsondata = json.load(f)
        ok, _ = edreq.requrementA5_2(jsondata)
        self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main()
