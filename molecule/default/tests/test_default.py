"""Module containing the tests for the default scenario."""

import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "file,content", [("/etc/systemd/journald.conf", r"^Storage=persistent$")]
)
def test_files(host, file, content):
    """Test that config files were modified as expected."""
    f = host.file(file)

    assert f.exists
    assert f.contains(content)
