#!/usr/bin/env python3

from yaml import safe_load
import unittest
from netaddr import IPNetwork, IPAddress, valid_ipv4


class TestYamlMethods(unittest.TestCase):

    def setUp(self):
        with open('metadata.yml', 'r') as f:
            self.metadata = safe_load(f)

    def tearDown(self):
        self.metadata = None

    def test_reference(self):
        self.assertRegex(self.metadata['config_reference'], r'^REF\d{5}$')

    def test_date(self):
        self.assertRegex(str(self.metadata['date']), r'^\d{4}-\d{2}-\d{2}$')

    def test_port(self):
        port = int(self.metadata['service_port'])
        self.assertGreater(port, 0)
        self.assertLessEqual(port, 65535)

    def test_valid_ip(self):
        for ip in self.metadata['source_ip']:
            # test if this is valid ip
            self.assertTrue(valid_ipv4(ip))
            # test if ip is from correct subnet
            self.assertTrue(IPAddress(ip) in IPNetwork('10.0.0.0/8'))

    def test_selection(self):
        self.assertTrue(self.metadata['peer_certificate_check'] in ['require', 'ignore'])

    def test_file_naming_convention(self):
        self.assertRegex(self.metadata['certificate_file'], r'^[a-zA-Z0-9-_]+\.crt$')


if __name__ == '__main__':
    unittest.main()
