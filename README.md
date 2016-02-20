# Victims.zone information resource

## Tech specs

Runs on python3.4

To make it work:

```bash
source venv/bin/activate

# Start app
python app.py runserver --port {port} --host {host.IP}

# And on work done ust do:
deactivate
```

*During development*

```bash
npm install -g bower
```

*Watch and compile less during development*

```bash
cd assets/
while true;do N=`find -name "*.less" `;inotifywait -qe modify $N ;for f in $N; do lessc -x less/app.less --source-map ../victims/static/css/app.css;done;done
```