import json

from common import exec_command as _c


def test_version():
    c, o, e = _c(['dcos-riak', '--version'])
    assert c == 0
    assert o.strip() == b'Riak Mesos Framework Version 0.3.1'
    assert e == b''


def test_help():
    c, o, e = _c(['riak-mesos'])
    assert c == 0
    assert e == b''
    c, o, e = _c(['riak-mesos', '--help'])
    assert c == 0
    assert e == b''
    c, o, e = _c(['riak-mesos', 'config', '--help'])
    assert c == 0
    assert e == b''
    assert o.strip() == b'Displays configuration'


def test_config():
    c, o, e = _c(['riak-mesos', 'config', '--json'])
    js = json.loads(o.decode("utf-8").strip())
    assert js['director']['use-public'] is False
    assert c == 0
    assert e == b''


def test_framework_config():
    c, o, e = _c(['riak-mesos', 'framework', 'config', '--json'])
    js = json.loads(o.decode("utf-8").strip())
    assert js['id'] == 'riak'
    assert c == 0
    assert e == b''
