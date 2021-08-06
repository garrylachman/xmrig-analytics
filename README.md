# XMRig to Google Analytics Reporter

### Howto
Clone the repo or download the zip file.
```
make help
Things3 low-level Python API.
=============================

Available commands:

auto-style                Style the code
clean                     Cleanup
code-count                Count the lines of code
code-lint                 Lint the code
code-style                Test the code style
css-lint                  Lint the CSS code
deps-create               Create the dependencies
deps-install              Install the dependencies
deps-update               Update the dependencies
doc                       Document the code
feedback                  Provide feedback
help                      Print help for each target
html-lint                 Lint the HTML code
js-lint                   Lint the JavaScript code
lint                      Run all linters
run                       Run the code
test                      Test the code
```

First install the deps
```
make deps-install
```

Run
```
make run config.json
```

### Config
```
{
    "ga": {
        "tracking_id": "UA-162892726-1"
    },
    "xmrig": {
        "interval": 10.0,
        "threads": 2,
        "worker_defaults": {
            "key": "123",
            "port": 8088
        },
        "workers": [
            {"hostname": "127.0.0.1", "port": 8088, "name": "worker-1"},
            {"hostname": "127.0.0.1", "port": 8088, "name": "worker-2"}
        ]
    },
    "reporter": {
        "threads": 2,
        "events": [
            {"category": "hashrate", "action":"10s", "value": "hashrate-10s"},
            {"category": "hashrate", "action":"60s", "value": "hashrate-60s"},
            {"category": "hashrate", "action":"15s", "value": "hashrate-15m"},
            {"category": "results", "action":"diff_current", "value": "diff_current"},
            {"category": "results", "action":"shares_good", "value": "shares_good"},
            {"category": "results", "action":"shares_total", "value": "shares_total"},
            {"category": "results", "action":"hashes_total", "value": "hashes_total"}
        ]
    }
}
```

