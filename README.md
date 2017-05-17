# Ansible Elasticstack Kibana
[![Build Status](https://travis-ci.org/remyma/ansible-elasticstack-kibana.svg?branch=master)](https://travis-ci.org/remyma/ansible-elasticstack-kibana)

Install and configure kibana.

## Requirements

* *java* : logstash needs java to run. This role can handle java install for you. But you can also install it on your own.

## Role Variables

| Variable     | Default       | Description    |
| ------------ | ------------- | -------------- |
| kibana_port | 5601 | kibana http port |
| kibana_host | localhost | Specifies the address to which the Kibana server will bind. |
| kibana_base_path | | Enables you to specify a path to mount Kibana at if you are running behind a proxy. |
| kibana_elasticsearch_url | http://localhost:9200 | The URL of the Elasticsearch instance to use for all your queries |
| kibana_logging_dest | stdout | The URL of the Elasticsearch instance to use for all your queries |

## Dependencies

* ansible-elasticstack

## Example Playbook

### Basic install

    - hosts: kibana-servers
      roles:
        - { role: ansible-elasticstack-kibana }

## License

BSD

