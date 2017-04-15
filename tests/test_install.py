import testinfra.utils.ansible_runner

from testinfra import modules

Service = modules.Service.as_fixture()
Command = modules.Command.as_fixture()

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_kibana_running(Service):
    kibana = Service("kibana")
    assert kibana.is_enabled
    assert kibana.is_running


def test_java_installed(Command):
    java_version_cmd = Command(
        "java -version 2>&1 | grep version | awk '{print $3}' | sed 's/\"//g'"
    )
    assert java_version_cmd.stdout >= '1.8'
