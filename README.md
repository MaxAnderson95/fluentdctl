# fluentdctl

A Python CLI to interact with the Fluentd HTTP RPC API.

## Installation

From PyPi:

`pip install fluentdctl`

From source:

`python setup.py`

## Prerequisites

The fluentd RPC endpoint [must be enabled](https://docs.fluentd.org/deployment/rpc#configuration) in your fluentd endpoint.

If you wish to manage a fluentd instance running on another machine, the binding in the configuration **cannot** be to `127.0.0.1`. It must either be `0.0.0.0` (all addresses) or a specific IP of the machine. Example:

```
<system>
  rpc_endpoint 0.0.0.0:24444
</system>
```

## Usage

To flush the fluentd buffer:

```
fluentdctl flush
```

To stop the fluentd process:

```
fluentdctl stop
```

To flush and then stop the fluentd process:

```
fluentdctl flushthenstop
```

To reload the fluentd process and configuration:

```
fluentdctl reload
```

### Specify a different host or port

The commands above will run against a local instance of fluentd running on the default port of 24444.

However with each command you can optionally specify a different remote host and/or port:

```
fluentdctl flush --host remote-srv-01 --port 12345
```

OR specify them positionally

```
fluentdctl flush remote-srv-01 12345
```

### Verbose output

Finally you can also specify `--verbose` on any command to get additional output.
