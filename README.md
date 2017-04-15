# Ansible Elasticstack Kibana

Install and configure kibana.

## Requirements

* *java* : logstash needs java to run. This role can handle java install for you. But you can also install it on your own.

## Role Variables

| Variable     | Default       | Description    |
| ------------ | ------------- | -------------- |
| kibana_java_install | true | true to install java / false if java is already installed on you own |
| kibana_update_java | false | if true, will update java |
| kibana_major_version | 5.x | Major version of kibana to install |
| kibana_version | 5.2.2 | Version of kibana to install |
| kibana_port | 5601 | kibana http port |
| kibana_host | localhost | Specifies the address to which the Kibana server will bind. |
| kibana_base_path | | Enables you to specify a path to mount Kibana at if you are running behind a proxy. |
| kibana_elasticsearch_url | http://localhost:9200 | The URL of the Elasticsearch instance to use for all your queries |
| kibana_logging_dest | stdout | The URL of the Elasticsearch instance to use for all your queries |

## Example Playbook

### Basic install

    - hosts: kibana-servers
      roles:
        - { role: ansible-elasticstack-kibana }

## License

BSD

