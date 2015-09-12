Shellper
========
.. image:: https://travis-ci.org/handbox/shellper.svg?branch=master
    :target: https://travis-ci.org/handbox/shellper

.. image:: https://coveralls.io/repos/handbox/shellper/badge.svg
    :target: https://coveralls.io/r/handbox/shellper

**StartUP of Handbox Team.**

This is new project from the young guys! This application will help you
organize your day, remind you of upcoming events, help your to cook dinner or
small lunch and much more! If you need to do some tasks (from school or
university, maybe working) just run our app and create event! It will pick up
the latest information and remind you about this! Very simple! Full
integration with Google Calendar.

**Functionality**

For now we added basic functionality:
    * Integration with Google Calendar and Gmail
    * Adding tasks
    * Deleting tasks
    * Showing tasks
    * Searching information based on the title of tasks

In this version authentication works with our test account. If you want that
application works with your account, please delete files etc/calendar-api.json and
etc/gmail-api.conf.
File etc/template.yaml is a list of events, modify it for your events.\
In your Google Calendar in description of event will be links to information
about your event.

To run app enter in your terminal:

    tox -e run etc/template.yaml

Branches
========
   master
   shellper-a0.1

Tools
=====
Useful links for employee

+------------+--------------------------------------------+
|   Tools    |                    URL                     |
+============+============================================+
| TaskTracker| http://shellhelper.myjetbrains.com/        |
+------------+--------------------------------------------+
| BugTracker | https://launchpad.net/shellper             |
+------------+--------------------------------------------+
| Etherpad   | https://shellhelper.etherpad.mozilla.org   |
+------------+--------------------------------------------+
| ShareDir   | https://goo.gl/TwfFtf                      |
+------------+--------------------------------------------+
