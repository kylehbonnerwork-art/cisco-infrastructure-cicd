import tempfile
import unittest
from pathlib import Path

from scripts.validate_config import validate_config


class TestValidateConfig(unittest.TestCase):

    def validate_text(self, content):
        with tempfile.TemporaryDirectory() as temp_dir:
            config_file = Path(temp_dir) / "router_config.txt"
            config_file.write_text(content, encoding="utf-8")

            return validate_config(config_file)

    def test_valid_configuration(self):
        config = """
hostname C8000V-LAB
interface Loopback100
 description CI-CD-TEST
 ip address 192.0.2.100 255.255.255.255
!
end
"""
        self.assertTrue(self.validate_text(config))

    def test_empty_configuration(self):
        self.assertFalse(self.validate_text(""))

    def test_missing_hostname(self):
        config = """
interface Loopback100
 description CI-CD-TEST
!
"""
        self.assertFalse(self.validate_text(config))

    def test_prohibited_reload_command(self):
        config = """
hostname C8000V-LAB
reload
"""
        self.assertFalse(self.validate_text(config))

    def test_comment_mentioning_reload(self):
        config = """
hostname C8000V-LAB
! Do not use reload during maintenance
"""
        self.assertTrue(self.validate_text(config))


if __name__ == "__main__":
    unittest.main()
