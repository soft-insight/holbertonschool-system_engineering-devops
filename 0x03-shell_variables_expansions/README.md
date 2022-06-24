# More on shell
Let's consider some basic but powerfull linux commands arround Expansion, variables, and `alias`. (This content is based on the web site: [Linux commands](http://linuxcommand.org/))

![Matrix in the shell](matrix.jpg  "Matrix in the shell")

1. Expansion
2. Variables
3. `alias` command

## 1. Expansion

Typing some commands, shell *expands* automatically their implict commands. 
The normal output for `$ echo "somenthing"`  can be exemplfied with
`~$ echo -e "hello, World\n" `
`Hello, World`
However a lot of expansions can be obtained for the `echo` command as in the following examples:

`$echo *` 
![](shell1.jpg)

Or,
`echo D*` list files and dir beginning with D
`echo *s` list files and dirs ending with s
`echo [[:uper]]*` list all elements begining with capital letters.

### Arithmetic Expansion
Arithmetic Expansion uses
`$((expresion))` for the expressions.

By example the simple arithmetic operation
$$ \frac{7^2 + 3}{2} $$
can be executed with
`$echo $(( (7**2 + 3)/2 ))`
`26`
`>`

The usual basic operatos `+, -, *, /, %`  of sum, rest, mult, div, and the remainder.

### Brace Expansion
As an implied loop
Example:
![](/shell2.jpg) 

Another basic examples can be considered as
`$echo {12..20}`
`$echo {z..a}`
And any kind of combinations, 
`$echo a{A{1,2},B{3,4}}b`
`aA1b aA2b aB3b aB4b`
`>`


## 2. Variables
They are usually in uppercase chacarters. 

### Global variables
Obtained by
`$env` or
`printenv`

### Local variables
This are only available in the current shell.

### Creating variables
Capitalized is used by default. To set a variables in shell use`$VARNAME="value"` with no spaces.
![](shell3.jpg)

This variable is available in the current shell or local. In order that all processes are aware of this variable, is necesary to **export it**.

`export VARNAME="value"`



## 3. `alias` command
These are predefines commands defined by the user and constructed from the usual commands.

The general syntax for `alias` is

`alias [-p] [name=”value”]`
where  `-p        print all defined aliases in a reusable format`.

A powerful and simple option for commands.

Some examples:
`$ alias p="pwd"`
`$alias ga="git add ."`
`$alias gp="git push"`

 Don't forget your `$git commit -m "your message"`.
 
 Now, try to create your `alias` for commit with the use of variables and `alias`.
 Or consider create your own bash script.

 Good codding!!

