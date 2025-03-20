# base64-experiment

This is an experiment to see if I can find the shortest length base64 string
that uses all 64 base64 characters with only ASCII characters from code 32
(`' '`) through 126 (`'~'`).

It concatenates a set of randomly generated 4-byte base64 chunks that are not
in the concatenated base64 string (if that fails, duplicates are allowed)
until the 64 base64 characters are used.

This is repeated several times, and the shortest base64 string and the
corresponding input string is displayed.

So far, the best input and output is this:

```
best input:   51: '5]]>vv*44&TT3pppkkL::.jjlXXh~~\//"..K  [11zOO8;;|??'
best output:  68: 'NV1dPnZ2KjQ0JlRUM3BwcGtrTDo6LmpqbFhYaH5+XC8vIi4uSyAgWzExek9PODs7fD8/'
```

## Running

```
python base64-experiment.py [<num_passes>]
```

where `<num_passes>` is the number of passes to run. If not specified, `1000`
is used.
