# base64-experiment

This is an experiment to see if I can find the shortest length base64 string
that uses all 64 base64 characters with only ASCII characters from code 32
(`' '`) through 126 (`'~'`).

It concatenates a set of randomly generated 4-byte base64 chunks that are not
in the concatenated base64 string (if that fails, duplicates are allowed)
until the 64 base64 characters are used.

This is repeated several times, and the shortest base64 string and the
corresponding input string is displayed.

One of the solutions is this:

```
best input:   48: '!  }gggIIT55;qqs!!Gjjb??=~~2$$+;;i::x..4kk,ppnoo'
best output:  64: 'ISAgfWdnZ0lJVDU1O3FxcyEhR2pqYj8/PX5+MiQkKzs7aTo6eC4uNGtrLHBwbm9v'
```

## Running

```
python base64-experiment.py [<num_passes>]
```

where `<num_passes>` is the number of passes to run. If not specified, `1000`
is used. If `<num_passes>` is less than or equal to zero, the script runs
until the "best output" length is 64.
