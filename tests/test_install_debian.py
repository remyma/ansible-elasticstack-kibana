import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('debian')


def test_repos(File):
    f = File('/etc/apt/sources.list.d/elastic-5.x.list')

    assert f.exists
