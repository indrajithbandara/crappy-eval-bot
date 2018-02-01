# crappy-eval-bot
Sometimes you just need a bot that can eval stuff. This is very unsafe and should not be used ever.

Oh. This uses the Discord.py rewrite too, not the async-branch version. So... yeah.

## Usage:

Your command prefix is `#!`. Stick your token as plaintext in `token.txt` before running the 
script.

You have three commands:

- `eval` - this simply `eval`s the input, and then returns the result as a string representation,
    sending it to the channel you invoked the command on.
- `aeval` - same as `eval`, except it `await`s whatever you pass in. This allows you to invoke
    coroutines properly. If you end the string you wish to eval with `!r` then instead of 
    calling `str()` on the result, we call `repr()`. This is only for this command, as the
    syntax of python means you can't put repr around the coroutine you are calling without getting
    a syntax error.
- `exec` - this temporarily redirects `stdout` and `stderr` to an `io.StringIO` stream object, and
    calls your input via `exec`. This will not return anything, but it is useful for executing
    things such as assignments, which are not valid in `eval` and `aeval` always.

## Globals:

Your globals are anything in the script.

- The bot object itself is accessible under the `bot` identifier.
- Both `eval` and `aeval` will store the most recent invocations result in a variable called `_`.
    This will persist between commands.
- There is a global dict for you to use called `bucket` if you want.

## Example usage

This is run in the discord chat. Lines beginning with `//` are notes.
```
// Get the Guild object for guild ID `134073775925886976` and store in _
#!eval bot.get_guild(134073775925886976)

// Store the Guild object in the bucket to use later (not required, but it is
// a good example of how to use it).
#!exec bucket['my_guild'] = _

// Get the Member object for user `150376112944447488` in the guild.
#!eval bucket['my_guild'].get_member(150376112944447488)

// Edit their nickname. This is a coroutine call, so we use `aeval`
#!aeval _.edit(nick='Steve the Boat Bot.')

// If the bot had permission, then it should now have renamed FredBoat to 
// 'Steve the Boat Bot.' in that guild.

// To turn the bot off, just close the event loop.
#!aeval bot.logout()

// Ded.
```
