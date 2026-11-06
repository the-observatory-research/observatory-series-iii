#!/usr/bin/env python3
"""Validate Series III publication indexes and copied source hashes.

This is a retrospective publication utility, NOT a historical experimental instrument.
"""
from pathlib import Path
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]


def load_csv(relpath):
    with (ROOT / relpath).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))


def check_events():
    rows=load_csv('evidence/events.csv')
    assert len(rows)==20, f'Expected 20 events, found {len(rows)}'
    ids=[row['event_id'] for row in rows]
    assert ids==[f'SIII-E{i:03d}' for i in range(1,21)], 'Event identifiers must be consecutive and ordered'
    for row in rows:
        page=row['compiled_source_pages'].replace('–','-')
        assert re.fullmatch(r'\d+(?:-\d+)?',page), (row['event_id'],page)
        ends=[int(x) for x in page.split('-')]
        assert 1<=ends[0]<=309 and 1<=ends[-1]<=309 and ends[0]<=ends[-1], row
    return len(rows)


def check_observations():
    rows=load_csv('evidence/observations.csv')
    assert len(rows)==7, f'Expected 7 observations, found {len(rows)}'
    ids=[row['observation_id'] for row in rows]
    assert ids==[f'SIII-OBS-{i:03d}' for i in range(1,8)], 'Observation identifiers must be ordered'
    for row in rows:
        linked=re.findall(r'E\d{3}',row['supporting_event_references'])
        assert linked and all(1<=int(x[1:])<=20 for x in linked), row
    return len(rows)


def check_hashes():
    rows=load_csv('provenance/source_hashes.csv')
    assert len(rows)==4
    for row in rows:
        path=ROOT/row['relative_path']
        assert path.is_file(),path
        data=path.read_bytes()
        assert hashlib.sha256(data).hexdigest()==row['sha256'],path
        assert len(data)==int(row['size_bytes']),path
    return len(rows)


def main():
    ne=check_events();no=check_observations();nh=check_hashes()
    print(f'PASS: {ne} event locators, {no} observation categories, {nh} archival source hashes')


if __name__=='__main__':main()
