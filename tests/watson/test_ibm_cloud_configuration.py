import unittest
import os
from src.watson.ibm_cloud_configuration import IBMCloudConfiguration
from tests.common.constants import TEST_RESOURCES_LOCATION


class TestIBMCloudConfiguration(unittest.TestCase):
    def test_config_updated(self):
        config = IBMCloudConfiguration(config_path=os.path.join(
            TEST_RESOURCES_LOCATION, "ibm_cloud_test.json"))
        self.assertEqual(config.apikey, "apikey123")
        self.assertEqual(config.url, "url987")


if __name__ == '__main__':
    unittest.main()
