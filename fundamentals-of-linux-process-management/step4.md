# Netstat command in Linux

Some processes make use of the network, and it can happen that they are *listening* on an address and a port.
Let’s first explain this two concepts. <br>
An **address**, technically the IP address, is like your home address: an identifier that the others use to reach you (that means your computer).
<br>
A **port** is a number associated to a process and it' used by others to communicate with *that specific process* running on the machine. <br>
So it works like this: to establish a connection, those who want to contact you have to specify the address, in order to reach your computer, and the port,
in order to communicate with the specific process they intend to.

There's a useful Linux command to display the running processes that are also listening on a port: ``netstat`` command.


Netstat command displays various network related information such as network connections, routing tables, interface statistics, masquerade connections, multicast memberships etc. This course does not cover these topics, since they are quite advanced. For us, ``netstat`` is a monitoring tool such as ``ps``.

### Examples of some practical ``netstat`` command

We said that we use ``netstat`` as a monitoring tool. For what? It's useful when we search for information about processes listening on addresses and ports. <br>
Here are some flags we can use:

| **Flag** | **Description** |
| -------- | --------------- |
| -a | Displays all connections and listening ports. |
| -b | Displays the executable involved in creating each connection or listening port. |
| -n | Displays addresses and port numbers in numerical form. |
| -o | Displays the owning process ID associated with each connection. |

-a (or -all): Show both listening and non-listening sockets. With the –interfaces option, show interfaces that are not up
netstat.

---
**Exercise 1**



---


---
**Exercise 2**


 
---