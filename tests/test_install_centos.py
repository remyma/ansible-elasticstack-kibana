import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('centos')


def test_repos(File):
    f = File('/etc/yum.repos.d/kibana-5.x.repo')

    assert f.exists
