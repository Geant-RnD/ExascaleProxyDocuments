# Timing Results

## Origin of Results

Generated with TiMemory + Geant4 using cmsExpMT example and macros included in folder

## Analysis

Example:

- Enter into one of directories (`events_10`) means results from 10 events) and untar the data

```shell
    $ cd events_10
    $ tar -xzf data.tar.gz
```

- Generate the full list of processes and particles from all JSON files in `data/`
- Output to `"processes_"` and `"particles_"` prefixed files ending with `cmsExpMT_10evt.txt`

```shell
    $ ../accumulate.py -o cmsExpMT_10evt.txt -i data/*.json
```

- Generate the full list of processes and particles from all JSON files in `data/`
- Output to `"processes_"` and `"particles_"` prefixed files ending with `cmsExpMT_10evt.txt`
- Select `"e-"`, `"e+"`, `"gamma"`, `"pi-"`, and `"pi+"` to be filtered into additional files that will display their accumulated wall/CPU time
- Label the output files of the selected particle types `"em_hadron"`, e.g. `"processes_em_hadron_cmsExpMT_10evt.txt"`

```shell
    $ ../accumulate.py -o cmsExpMT_10evt.txt -i data/*.json -s "e+" "e-" "gamma" "neutron" "pi-" "pi+" -l em_hadron
```
