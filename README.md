SOGo for Yunohost
=================

[![Integration level](https://dash.yunohost.org/integration/sogo.svg)](https://dash.yunohost.org/appci/app/sogo) ![](https://ci-apps.yunohost.org/ci/badges/sogo.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/sogo.maintain.svg)  
[![Install sogo with YunoHost](https://install-app.yunohost.org/install-with-yunohost.png)](https://install-app.yunohost.org/?app=sogo)

> *This package allow you to install sogo quickly and simply on a YunoHost server.  
If you don't have YunoHost, please see [here](https://yunohost.org/#/install) to know how to install and enjoy it.*

Overview
--------

SOGo is an opensource groupware solution which has Webmail, a global address book and Calender and Contacts which can be synced via caldav or cardav.

**Shipped version:** 3.2.6-2

Screenshots
-----------

| Localized |Drag'n'Drop | Reminders | Delegation |
| :------------: | :------------: | :------------: | :------------: |
| ![](https://sogo.nu/img/features/localized.png) | ![](https://sogo.nu/img/features/dnd_01.png) | ![](https://sogo.nu/img/features/reminders.png) | ![](https://sogo.nu/img/features/delegation.png) |
| SOGo is available in over a dozen languages so you'll always feel at home. If your language is missing, you can easily contribute to the project and submit your translation. | Move messages to folders, drag contacts to address books, and modify events time and duration from the tip of your finger. Just like a desktop app. | Set alarms to important events and get alerted directly from your browser. | Set alarms to important events and get alerted directly from your browser. | Delegate access to your mail account or delegate an invitation to another person. |

| Resource Reservation | HTML | Mail Return Receipt | Forward and Auto-Reply |
| :------------: | :------------: | :------------: | :------------: |
| ![](https://sogo.nu/img/features/resource.png) | ![](https://sogo.nu/img/features/html.png) | ![](https://sogo.nu/img/features/return-receipt.png) | ![](https://sogo.nu/img/features/auto-reply.png) |
| Define resources like projectors and conference rooms to automatically accept invitations for them while avoiding double-booking. | Compose HTML mail with the complete inline [rich-text editor](http://www.ckeditor.com). | Request or answer to return requests to confirm the arrival of messages. | Set an auto reply while on vacation or forward all your incoming mail to one ore many alternate email addresses. |

| S/MIME | Mail Filtering | Sharing | Recurring Events |
| :------------: | :------------: | :------------: | :------------: |
| ![](https://sogo.nu/img/features/security.png) | ![](https://sogo.nu/img/features/mail-filters.png) | ![](https://sogo.nu/img/features/sharing.png) | ![](https://sogo.nu/img/features/recurring-events.png) |
| Sign and encrypt messages using your personal secure certificate. Automatically manage public certificates you receive by email. | Define powerful server-side filters to automatically act on new messages. Forward, discard, reject, flag or move incoming mail depending on complex criteria. | Share your mail, calendars and address books with other users. Define specific rights to each person or group of persons. | Define precise recurrence pattern for your repeating events and create exceptions if necessary. |

| Free/Busy Time | Notifications | Categories | Multiple Mail Accounts  | Export/Import |
| :------------: | :------------: | :------------: | :------------: | :------------: |
| ![](https://sogo.nu/img/features/freebusy.png) | ![](https://sogo.nu/img/features/notifications.png) | ![](https://sogo.nu/img/features/categories.png) | ![](https://sogo.nu/img/features/imap-accounts.png) | ![](https://sogo.nu/img/features/import.png) |
| Before sending an invitation, see the free/busy periods of attendees, either from the local SOGo server or a remote Microsoft Exchange server. Automatically set off-hours as busy if you like. | Be informed if someone modifies your calendar or automatically inform someone if your calendar changes. | Choose from a predefined set of categories or create your own categories and associate them to your events and contacts. | Configure all your mail accounts (IMAP) from SOGo and forget about login-in to multiple webmail services. | Export calendars or import events from a vCalendar file. Export contacts to LDIF or import cards from a LDIF of vCard file. Export a mailbox to zip archive. |


Demo
----

* [Official demo](https://sogo.nu/)

<!--## Configuration

TODO complete-->

Documentation
-------------

 * Official documentation: https://sogo.nu/support.html#/documentation
 * YunoHost documentation: There no other documentations, feel free to contribute.

YunoHost specific features
--------------------------

### Multi-users support

LDAP and HTTP auth are supported.

### Supported architectures

* x86-64 - [![Build Status](https://ci-apps.yunohost.org/ci/logs/sogo%20%28Apps%29.svg)](https://ci-apps.yunohost.org/ci/apps/sogo/)
* ARMv8-A - [![Build Status](https://ci-apps-arm.yunohost.org/ci/logs/sogo%20%28Apps%29.svg)](https://ci-apps-arm.yunohost.org/ci/apps/sogo/)

<!--Limitations
------------

* Any known limitations.

Additional informations
-----------------------

* Other informations you would add about this application-->

Links
-----

 * Report a bug: https://github.com/YunoHost-Apps/sogo_ynh/issues
 * App website: https://sogo.nu/
 * YunoHost website: https://yunohost.org/

---

Install
-------

From command line:

`sudo yunohost app install -l sogo https://github.com/YunoHost-Apps/sogo_ynh`

Upgrade
-------

From command line:

`sudo yunohost app upgrade sogo -u https://github.com/YunoHost-Apps/sogo_ynh`

Developers infos
----------------

Please do your pull request to the [testing branch](https://github.com/YunoHost-Apps/sogo_ynh/tree/testing).

To try the testing branch, please proceed like that.
```
sudo yunohost app install https://github.com/YunoHost-Apps/sogo_ynh/tree/testing --debug
or
sudo yunohost app upgrade sogo -u https://github.com/YunoHost-Apps/sogo_ynh/tree/testing --debug
```

License
-------

Sogo is published under the GPL-v2 and LGPL-v2 liencience : https://github.com/inverse-inc/sogo/blob/master/COPYING.GPL and https://github.com/inverse-inc/sogo/blob/master/COPYING.LGPL

Todo
----

-[ ] More Tests
