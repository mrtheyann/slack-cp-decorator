# Slack copypaste decorator

Simple Python3 script to prettify messages copied from Slack by removing some side effects that could appeared during copying.

### How to use

Clone:

`https://github.com/mrtheyann/slack-cp-decorator.git`

Launch:

`python decorate.py [path-to-file]`

### Example

```bash
>python decorate.py input.txt
Reading..

Formatting..

Decorating..

Decoration complete!

Result: Output.txt
```

##### input.txt

```
jack.london
12:23 AM
refactoring == waste of time
hugh.jackman
12:23 AM
Yeah? I dont think so!
12:23
End of story.
jack.london
12:24 AM
Welp.
```

##### output.txt

```
jack.london [12:23 AM]
refactoring == waste of time

hugh.jackman [12:23 AM]
Yeah? I dont think so!
End of story.

jack.london [12:24 AM]
Welp.
```