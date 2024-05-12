# Postmortem
Learning how to write an Incident Report, also referred to as a Postmortem. This postmortem follows the guidelines used closely by google engineers to file reports. The report is made up of five parts, an issue summary, a timeline, root cause analysis, resolution and recovery, and lastly, corrective and preventative measures. Lets review each of these parts in detail.

## Issue Summary
I have alerted since Oct 21, 2022 at 3 hours EAT gap of the each week after I forked Fix_My_Code_Challenge/0x01-challenge/ to fix the code.<br>
After that day the github alerted me on email as depedance alert every 7 days gap(every week). The root cause was the outage of the software version.
## Timeline
The issue was detected start from Oct 21, 2022 at 8:03 AM EAT. <br>
The issue dectected was dependancy alert because the repository I forked was fulled with the outage version of software. This incident is now present because I don't want to fix since it doesn't matter and I have no time to debug.
## Root Cause
The main cause of the issues were many but for instance I can mention one of them <br>
[Security]<br>
[CRuby] Vendored libxml2 is updated to address CVE-2022-2309, CVE-2022-40304, and CVE-2022-40303. See GHSA-2qc6-mcvw-92cw for more information.
[CRuby] Vendored zlib is updated to address CVE-2022-37434. Nokogiri was not affected by this vulnerability, but this version of zlib was being flagged up by some vulnerability scanners, see #2626 for more information.<br>

[Dependencies]<br>
[CRuby] Vendored libxml2 is updated to v2.10.3 from v2.9.14.
[CRuby] Vendored libxslt is updated to v1.1.37 from v1.1.35.
[CRuby] Vendored zlib is updated from 1.2.12 to 1.2.13. (See LICENSE-DEPENDENCIES.md for details on which packages redistribute this library.)

[Fixed] <br>
[CRuby] Nokogiri::XML::Namespace objects, when compacted, update their internal struct's reference to the Ruby object wrapper. Previously, with GC compaction enabled, a segmentation fault was possible after compaction was triggered. [#2658] (Thanks, @​eightbitraptor and @​peterzhu2118!)
[CRuby] Document#remove_namespaces! now defers freeing the underlying xmlNs struct until the Document is GCed. Previously, maintaining a reference to a Namespace object that was removed in this way could lead to a segfault. [#2658] <br>

## Resolution and Recovery
The resolution and the recovery of this issue is update the dependance issues as it tells.
## Corrective and preventative measures
After Updating the dependant software of this software, it should be updated instantly when alerted by the github by making the github alert ON.
