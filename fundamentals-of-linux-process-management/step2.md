## Display processes

In the introduction we mentioned briefly the ``ps`` command and showed a possible output. <br>
We said that it stands for **process state** and it displays some information on the process running on the machine.
``ps`` command is used to list the currently running processes and their PIDs (process identification numbers) along with 
some other information depends on different options. It reads the process information from the virtual files in ``/proc`` file-system.<br>
``ps`` command provides numerous options for manipulating the output according to our need. The syntax:

```bash
ps [options]
```

**Options:**

1. Simple process selection: Shows the processes for the current shell
      ```bash
       ps
      ```
      Result contains four columns of information.
      Where,
      * PID – the unique process ID
      * TTY – terminal type that the user is logged into
      * TIME – amount of CPU in minutes and seconds that the process has been running
      * CMD – name of the command that launched the process.
      Note – Sometimes when we execute ps command, it shows TIME as 00:00:00. It is nothing but the total accumulated CPU utilization time for any process and 00:00:00 indicates no CPU time has been given by the kernel till now. In above example we found that, for bash no CPU time has been given. This is because bash is just a parent process for different processes which needs bash for their execution and bash itself is not utilizing any CPU time till now.

2. List all processes: To list all processes on a system use the -e option.
    ```bash
    ps -e
    ```
    This option can be combined with the -f and -F options to provide more information on processes. The -f option offers full-format listing.

    Another commonly used syntax to achieve seeing every process on the system using BSD syntax is 
    ```bash
    ps aux
   ```
    
3. View Processes not associated with a terminal: View all processes except both session leaders and processes not associated with a terminal.
   ```bash
    ps -a
   ```
   Note – You may be thinking that what is session leader? A unique session is assing to evry process group. So, session leader is a process which kicks off other processes. The process ID of first process of any session is similar as the session ID.

4. View all the running processes:
    ```bash
    ps -r
    ```
5. View all processes owned by you: Processes i.e same EUID as ps which means runner of the ps command, root in this case –
    ```bash
    ps -x
    ```

6. Select the process by the command name. This selects the processes whose executable name is given in cmdlist.
There may be a chance you won’t know the process ID and with this command it is easier to search.
    ```bash
    ps -C command_name
    ```

    Example:
$ ps -C dhclient
  PID TTY          TIME CMD
19805 ?        00:00:00 dhclient

View process by process ID.
Syntax :
ps p process_id
ps -p process_id
ps --pid process_id

Example :
$  ps p 27223
  PID TTY      STAT   TIME COMMAND
27223 ?        Ss     0:01 sshd: root@pts/2

$  ps -p 27223
  PID TTY          TIME CMD
27223 ?        00:00:01 sshd

$ ps --pid 27223
  PID TTY          TIME CMD
27223 ?        00:00:01 sshd
You can view multiple processes by specifying multiple process IDs separated by blank or comma –
Example :

$ ps -p 1 904 27223
  PID TTY      STAT   TIME COMMAND
    1 ?        Ss     0:13 /usr/lib/systemd/systemd --switched-root --system --d
  904 tty1     Ssl+   1:02 /usr/bin/X -core -noreset :0 -seat seat0 -auth /var/r
27223 ?        Ss     0:01 sshd: root@pts/2
Here, we mentioned three process IDs – 1, 904 and 27223 which are separated by blank.

Select by parent process ID. By using this command we can view all the processes owned by parent process except the parent process.
$ ps -p 766
  PID TTY          TIME CMD
  766 ?        00:00:06 NetworkManager

$ ps --ppid 766
  PID TTY          TIME CMD
19805 ?        00:00:00 dhclient
In above example process ID 766 is assigned to NetworkManager and this is the parent process for dhclient with process ID 19805.

Select by effective user ID or name.
Syntax :
ps U user_name/ID
ps -U user_name/ID
ps -u user_name/ID
ps –User user_name/ID
ps –user user_name/ID
Output Format control

These options are used to choose the information displayed by ps. There are multiple options to control output format. These option can be combined with any other options like e, u, p, G, g etc, depends on our need.

 Use -f to view full-format listing.
$ ps -af
tux      17327 17326  0 12:42 pts/0    00:00:00 -bash
tux      17918 17327  0 12:50 pts/0    00:00:00 ps -af
Use -F to view Extra full format.
$ ps -F
UID        PID  PPID  C    SZ   RSS PSR STIME TTY          TIME CMD
tux      17327 17326  0 28848  2040   0 12:42 pts/0    00:00:00 -bash
tux      17942 17327  0 37766  1784   0 12:50 pts/0    00:00:00 ps -F
To view process according to user-defined format.
Syntax :
$ ps --formate column_name
$ ps -o column_name
$ ps o column_name

Example :
$ ps -aN --format cmd,pid,user,ppid
CMD                           PID USER      PPID
/usr/lib/systemd/systemd --     1 root         0
[kthreadd]                      2 root         0
[ksoftirqd/0]                   3 root         2
[kworker/0:0H]                  5 root         2
[migration/0]                   7 root         2
[rcu_bh]                        8 root         2
[rcu_sched]                     9 root         2
[watchdog/0]                   10 root         2
In this example I wish to see command, process ID, username and parent process ID, so I pass the arguments cmd, pid, user and ppid respectively.


View processes using highest memory.
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem
12 – print a process tree

$ ps --forest -C sshd
  PID TTY          TIME CMD
  797 ?        00:00:00 sshd
11680 ?        00:00:03  \_ sshd
16361 ?        00:00:02  \_ sshd
List all threads for a particular process. Use either the -T or -L option to display threads of a process.
$ ps -C sshd -L
  PID   LWP TTY          TIME CMD
  797   797 ?        00:00:00 sshd
11680 11680 ?        00:00:03 sshd
16361 16361 ?        00:00:02 sshd
Note – For the explanation of different column contents refer man page.

## Grep command

When we list processes via `ps` command, usually we see many more lines than we want. So here's where ``grep`` command can come in handy.
The grep command is used to search text. It searches the given file for lines containing a match to the given strings or words. It is one of the most useful commands on Linux and Unix-like system. Let us see how to use grep on a Linux or Unix like system.
Syntax

The syntax is as follows:
```bash
grep [option] 'word-to-search' [filename]
```
Options can be:
| Option | Description |
| ------ | ----------- |
| -i | Ignore case distinctions on Linux and Unix |
|-w	| Force PATTERN to match only whole words |
|-v	| Select non-matching lines |
|-n	| Print line number with output lines |
|-h	| Suppress the Unix file name prefix on output |
|-r	| Search directories recursivly on Linux |
|-R	| Just like -r but follow all symlinks |
|-l	| Print only names of FILEs with selected lines |
|-c	| Print only a count of selected lines per FILE |
|--color | Display matched pattern in colors |

grep 'word' filename
fgrep 'word-to-search' file.txt
grep 'word' file1 file2 file3
grep 'string1 string2'  filename
cat otherfile | grep 'something'
command | grep 'something'
command option1 | grep 'data'
grep --color 'data' fileName
grep [-options] pattern filename
fgrep [-options] words file
How do I use grep to search a file on Linux?

S

Please note that the above command also returns lines where “California” is part of other words, such as “Californication” or “Californian”. Hence pass the -w option with the grep/fgrep command to get only lines where “California” is included as a whole word:
fgrep -w California address.txt

You can force grep to ignore word case i.e match boo, Boo, BOO and all other combination with the -i option. For instance, type the following command:
grep -i "boo" /etc/passwd

grep command examples for Linux and Unix users
The last grep -i "boo" /etc/passwd can run as follows using the cat command too:
cat /etc/passwd | grep -i "boo"

How to use grep recursively

You can search recursively i.e. read all files under each directory for a string “192.168.1.5”
$ grep -r "192.168.1.5" /etc/

OR
$ grep -R "192.168.1.5" /etc/

Sample outputs:

/etc/ppp/options:# ms-wins 192.168.1.50
/etc/ppp/options:# ms-wins 192.168.1.51
/etc/NetworkManager/system-connections/Wired connection 1:addresses1=192.168.1.5;24;192.168.1.2;

 
You will see result for 192.168.1.5 on a separate line preceded by the name of the file (such as /etc/ppp/options) in which it was found. The inclusion of the file names in the output data can be suppressed by using the -h option as follows:
$ grep -h -R "192.168.1.5" /etc/

OR
$ grep -hR "192.168.1.5" /etc/

Sample outputs:

# ms-wins 192.168.1.50
# ms-wins 192.168.1.51
addresses1=192.168.1.5;24;192.168.1.2;
How to use grep to search words only

When you search for boo, grep will match fooboo, boo123, barfoo35 and more. You can force the grep command to select only those lines containing matches that form whole words i.e. match only boo word:
$ grep -w "boo" file

How to use grep to search 2 different words

Use the egrep command as follows:
$ egrep -w 'word1|word2' /path/to/file

How can I count line when words has been matched

The grep can report the number of times that the pattern has been matched for each file using -c (count) option:
$ grep -c 'word' /path/to/file

Pass the -n option to precede each line of output with the number of the line in the text file from which it was obtained:
$ grep -n 'root' /etc/passwd

1:root:x:0:0:root:/root:/bin/bash
1042:rootdoor:x:0:0:rootdoor:/home/rootdoor:/bin/csh
3319:initrootapp:x:0:0:initrootapp:/home/initroot:/bin/ksh
Force grep invert match

You can use -v option to print inverts the match; that is, it matches only those lines that do not contain the given word. For example print all line that do not contain the word bar:
$ grep -v bar /path/to/file

Display lines before and after the match

Want to see the lines before your matches? Try passing the -B to the grep:
grep -B NUM "word" file
grep -B 3 "foo" file1

Similarly, display the lines after your matches by passing the -A to the grep:
grep -A NUM "string" /pth/to/file
grep -A 4 "dropped" /var/log/ufw.log

We can combine those two options to get most meaningful outputs:
grep -C 4 -B 5 -A 6 --color 'error-code' /var/log/httpd/access_log

Here is a sample shell script that fetches the Linux kernel download urls:

.......
...
_out="/tmp/out.$$"
curl -s https://www.kernel.org/ > "$_out"
#######################
## grep -A used here ##
#######################
url="$(grep -A 2 '<td id="latest_button">' ${_out}  | grep -Eo '(http|https)://[^/"]+.*xz')"
gpgurl="${url/tar.xz/tar.sign}"
notify-send "A new kernel version ($remote) has been released."
echo "* Downloading the Linux kernel (new version) ..."
wget -qc "$url" -O "${dldir}/${file}"
wget -qc "$gpgurl" -O "${dldir}/${gpgurl##*/}"
.....
..
UNIX / Linux pipes

grep command often used with shell pipes. In this example, show the name of the hard disk devices:
# dmesg | egrep '(s|h)d[a-z]'

Display cpu model name:
# cat /proc/cpuinfo | grep -i 'Model'

However, above command can be also used as follows without shell pipe:
# grep -i 'Model' /proc/cpuinfo

model		: 30
model name	: Intel(R) Core(TM) i7 CPU       Q 820  @ 1.73GHz
model		: 30
model name	: Intel(R) Core(TM) i7 CPU       Q 820  @ 1.73GHz
One of my favorite usage of grep or egrep command to filter the output of the yum command/dpkg command/apt command/apt-get command:
dpkg --list | grep linux-image
yum search php | grep gd
apt search maria | egrep 'server|client'


grep command in Linux with examples
Linux grep commands explained with shell pipes examples
How do I list just the names of matching files?

Use the -l option to list file name whose contents mention main():
$ grep -l 'main' *.c

Finally, we can force grep to display output in colors, enter:
$ grep --color vivek /etc/passwd

Grep command in action on Linux and Unix like system
Grep command in action

In conclusion, the --color option increase readblity. For example, the GREP_COLOR environment variable and the grep --color=always can be used as follows:
GREP_COLOR='1;35' grep --color=always 'vivek' /etc/passwd
GREP_COLOR='1;32' grep --color=always 'vivek' /etc/passwd
GREP_COLOR='1;37' grep --color=always 'root' /etc/passwd
GREP_COLOR='1;36' grep --color=always nobody /etc/passwd

Visual grepping
In addition, to default red color now we can define colors using GREP_COLOR shell variable. The differnt color helps us massivly with visual grepping.
Conclusion

The grep command is a very versatile and many new Linux or Unix users find it complicated. Hence, I suggest you read the grep man page too. Let us summarize most import options:


