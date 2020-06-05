# Signals
Signals are software interrupts sent to a program to indicate that an important event has occurred. The events can vary from user requests to illegal memory access errors. 
Some signals, such as the interrupt signal, indicate that a user has asked the program to do something that is not in the usual flow of control.
The following table lists out common signals you might encounter and want to use in your programs:

| **Signal Name** |	**Signal Number** | **Description** |
| --- | --- | --- |
| SIGHUP | 1 | Hang up detected on controlling terminal or death of controlling process. |
| SIGINT | 2 | Issued if the user sends an interrupt signal (Ctrl + C). |
| SIGQUIT | 3 | Issued if the user sends a quit signal (Ctrl + D). |
| SIGFPE| 8 | Issued if an illegal mathematical operation is attempted. |
| SIGKILL| 9 | If a process gets this signal it must quit immediately and will not perform any clean-up operations. |
| SIGALRM | 14 | Alarm clock signal (used for timers). |
| SIGTERM | 15 | Software termination signal (sent by kill by default). |

**List of Signals**

There is an easy way to list down all the signals supported by your system. Just issue the ``kill -l`` command and it would display all the supported signals:

#signalist
```bash
$ kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL
 5) SIGTRAP      6) SIGABRT      7) SIGBUS       8) SIGFPE
 9) SIGKILL     10) SIGUSR1     11) SIGSEGV     12) SIGUSR2
13) SIGPIPE     14) SIGALRM     15) SIGTERM     16) SIGSTKFLT
17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU
25) SIGXFSZ     26) SIGVTALRM   27) SIGPROF     28) SIGWINCH
29) SIGIO       30) SIGPWR      31) SIGSYS      34) SIGRTMIN
35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3  38) SIGRTMIN+4
39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12
47) SIGRTMIN+13 48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14
51) SIGRTMAX-13 52) SIGRTMAX-12 53) SIGRTMAX-11 54) SIGRTMAX-10
55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7  58) SIGRTMAX-6
59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

Every signal has a default action associated with it. The default action for a signal is the action that a script or program performs when it receives a signal.<br>
Some of the possible default actions are:

* Terminate the process.
* Ignore the signal.
* Dump core. This creates a file called core containing the memory image of the process when it received the signal.
* Stop the process.
* Continue a stopped process.

**Sending Signals**

There are several methods of delivering signals to a program or script. One of the most common is for a user to type Control+c or the INTERRUPT key while a script is executing.

When you press the **Ctrl+c** key, a **SIGINT** is sent to the script and as per defined default action script terminates.

The other common method for delivering signals is to use the ``kill`` command, the syntax of which is as follows:
```bash
$ kill -signal pid
```
Note that the word *kill* might be misleading, since it sounds like something that is specifically designed to end a process, which is not. The ``kill`` command is designed for sending a signal of the set we [listed](#signalist) above: the most proper word, maybe, should have been "hit".
<br>
Let's go back to the command itself.<br>
The *signal* is either **the number or name of the signal to deliver** and *pid* is the **process ID that the signal should be sent to**. For example:

```bash
$ kill -1 666
```
The above command sends the SIGHUP (or hang-up signal) to the program that is running with process ID 666.

To send a SIGKILL signal to the same process, use the following command:
```bash
$ kill -9 666
```
This kills (terminates) the process running with process ID 666.

## The nohup command

When exiting the shell of a Linux System, all running processes are usually terminated or hang up. So what do you do if you want your process to "survive" the terminale, which means to be independent, to keep running even though you end the shell session?<br>
This is where the ``nohup`` command comes in.<br>
Nohup, short for *no hang up* is a command in Linux systems that keep processes running even after quitting the shell or terminal.
Nohup prevents the processes or jobs from receiving the **SIGHUP** (Signal Hang UP) signal, that is sent to a process upon closing or exiting the terminal.

**Nohup command syntax**

Nohup command syntax is as follows:
```bash
nohup command arguments
```
or
```bash
nohup options
```

Let’s see how the command comes into play.


**Starting a process using Nohup**

When you start a process on a shell, the *parent process* of this new process launched is the shell itself. But if you use nohup, the process becomes indepedent from the "destiny" of the shell: if the terminal dies, or if you quit the session, the process will continue its run.
```bash
nohup ./hello.sh 
```

Output
```bash
$ nohup ./hello.sh
nohup: ignoring input and appending output to 'nohup.out'
```

**Nohup command with regular commands**

From the output above, the output of the command has been saved to nohup.out to verify this run,
```bash
less nohup.out
```

Additionally, you can specify the output file in which redirecting the output:

```bash
nohup ./some-executable > custom-output-file.txt
```

**Starting a process in the background using Nohup**

To start a process in the background use the **&** symbol at the end of the command. 
In this example, we are pinging google.com and sending it to the background.
```bash
nohup ping google.com &
```

---
**Exercise 1**

1. Launch *script1* in background and also using *nohup*.
2. Find the launched process running.
3. Kill it using its pid.

  [Hint: if you type a second enter, the shell should display ``[1]+  Killed``.]

---


---
**Exercise 2**


 
---
