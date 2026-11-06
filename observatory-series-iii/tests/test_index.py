"""Tests for retrospective publication records, not historical model-output scoring."""
import unittest
from tools.verify_evidence_index import check_events, check_hashes, check_observations


class PublicationIndexTests(unittest.TestCase):
    def test_event_coverage(self):
        self.assertEqual(check_events(),20)

    def test_observation_links(self):
        self.assertEqual(check_observations(),7)

    def test_archived_source_hashes(self):
        self.assertEqual(check_hashes(),4)


if __name__=='__main__':unittest.main()
