# Resize Display size of Virtual Machines

## Date

2023-10-06-Friday.

## Environment

* Ubuntu 20.04.4 LTS
  * VirtualBox 6.1.40
 
## Content

Make sure the virtual machine is turned off.

{virtual_machine} > Settings > Display > Screen > Graphics Controller:

Change "VMSVGA" to "VBoxVGA" or "VBoxSVGA"

Start the virtual machine, then the display would resize its display regard in the window size.

---

### Reference
- Resize Display Blog KR, https://sidepower.tistory.com/59, 2023-10-06-Fri.
