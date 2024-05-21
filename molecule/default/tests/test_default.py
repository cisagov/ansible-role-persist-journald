"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import configparser
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_config(host):
    """Test that systemd-journald is configured as expected."""
    cmd = host.run("systemd-analyze cat-config systemd/journald.conf")
    assert cmd.rc == 0
    config = configparser.ConfigParser(strict=False)
    config.read_string(cmd.stdout)
    assert config["Journal"]["Storage"] == "persistent"
