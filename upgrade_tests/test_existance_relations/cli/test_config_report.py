"""Upgrade TestSuite for validating Satellite config-report existence and
associations post upgrade

:Requirement: Upgraded Satellite

:CaseAutomation: Automated

:CaseLevel: System

:CaseComponent: CLI

:TestType: nonfunctional

:CaseImportance: High

:Upstream: No
"""
import pytest
from upgrade_tests.helpers.common import dont_run_to_upgrade, existence
from upgrade_tests.helpers.existence import compare_postupgrade, pytest_ids

#Required Data
component = 'config-report'
report_id = compare_postupgrade(component, 'id')
report_host = compare_postupgrade(component, 'host')
last_report = compare_postupgrade(component, 'last report')


# Tests
@pytest.mark.parametrize("pre,post", report_id, ids=pytest_ids(report_id))
def test_positive_organizations_by_id(pre, post):
    """Test all config-reports are existing after upgrade by id's
    :id: upgrade-f16062fb-6d9d-400e-8149-f73ec254792d
    :expectedresults: All config-reports should be retained post upgrade by id's
    """
    assert existence(pre, post)


@pytest.mark.parametrize("pre,post", report_host, ids=pytest_ids(report_host))
def test_positive_organizations_by_host(pre, post):
    """Test all config-reports are existing after upgrade by host
    :id: upgrade-0cd21280-8357-4b85-a849-d326bd408853
    :expectedresults: All config-reports should be retained post upgrade by host
    """
    assert existence(pre, post)


@pytest.mark.parametrize("pre,post", last_report, ids=pytest_ids(last_report))
def test_positive_organizations_by_last_report(pre, post):
    """Test all config-reports are existing after upgrade by last report
    :id: upgrade-22c2f202-0fa0-4d55-beb3-5c6f16403f32
    :expectedresults: All config-reports should be retained post upgrade by last report
    """
    assert existence(pre, post)