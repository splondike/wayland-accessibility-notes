# Linux a11y communities

This page includes some notes taken when researching the people working on Linux accessibility technologies. At present they're pretty raw so the most useful thing is probably the actual list I went through.

For many communities I searched for the terms a11y and accessibility. Or if they were a community based around a11y (e.g. Orca) I instead searched for Wayland.

### GNOME

A desktop environment in both X11 and Wayland.

Seemed like Emmanuele Bassi was the main employed accessibility person here, but I think he's moved on to other work, and now just pushes it as a volunteer.

- https://discourse.gnome.org/t/gnu-linux-accessibility/13559/2 - Not many contributors on accessibility stack
- https://discourse.gnome.org/tag/a11y and https://discourse.gnome.org/c/community/accessibility/340 - Not much there, maybe 1 post per week

### GTK

The dominant UI toolkit on Linux.

- https://gitlab.gnome.org/GNOME/gtk/-/issues/1739#note_458101 - Long discussion between Orca users and GTK devs about maintaining AT-SPI2 compatibility. One position for removing it was that it had been badly maintained for so long it might as well be removed.

### Fedora/Red Hat

Two popular Linux distributions. Red Hat the company is involved in both and is a significant contributor to the Linux ecosystem.

- https://fedoramagazine.org/accessibility-in-fedora-workstation/ - Red Hat hired a blind guy in June 2022 to work on accessibility
- https://discussion.fedoraproject.org/t/fedora-strategy-2028-focus-area-review-accessibility/46898/4 - Accessibility is a current priority in Fedora
- https://discussion.fedoraproject.org/t/accessibility-wg-meeting-poll-2023/87935/6 - The diversity, equity, inclusion team are the people working on a11y generally in Fedora. They're next meeting October 3rd. They've had some contact with a Red Hat team responsible for a11y.
- https://pagure.io/fedora-workstation/issue/395 https://discussion.fedoraproject.org/t/f40-change-proposal-kde-plasma-6-system-wide/89794/48 - Considering dropping default X11 support for GNOME and KDE
- https://gitlab.com/fedora/dei/a11y/-/issues/10 - Somebody from the Talon community asking about a11y in Fedora.

### Sway/wlroots

A pretty popular Wayland desktop environment.

https://gitlab.freedesktop.org/wlroots
https://github.com/swaywm/sway

Couldn't find anything in sway, wlroots, or wlr-protocols. Orca mentioned, and the main sway dev said he doesn't know about it, but it should work (believing it was just about AT-SPI2 I think).

### Ubuntu

The most popular desktop linux distribution. Backed by a large company called Canonical.

- https://discourse.ubuntu.com/t/accessibility-testers-needed-web-site-and-flutter-installer/26485/6 (2022) - Sounds like somebody saying they don't do that well on it but want to do better
- https://lists.ubuntu.com/archives/ubuntu-accessibility/ - Not much mention of Wayland here
- https://ubuntuforums.org/forumdisplay.php?f=145 - (accessibility subforum) Nothing here about Wayland

### KDE

A popular desktop environment on X11 and Wayland.

- https://discuss.kde.org/t/questions-about-ui-automation-on-kwin-wayland/1778/10 - Comment about how you can contribute to making a11y etc. work better in Linux. Basically, get involved with Wayland.
- https://community.kde.org/Goals/Wayland - Lists out various bugs wrt. to KDE/Wayland
- https://mail.kde.org/pipermail/kde-accessibility/ - Doesn't have much to say on Wayland

### Arch Linux

A popular community Linux distribution.

Don't think there's much, the search wasn't easy to use though.

### Suse

A Linux distribution backed by a commercial company.

Couldn't find much in their wiki, forums, or mailing lists

### Orca

The main linux screenreader (Accessibility Technology for blind users).

Sounds like they use mailing lists mostly. Used to be here: https://mail.gnome.org/archives/orca-list/ moved here in late 2022: https://www.freelists.org/archive/orca/ . Have read through all the threads in the latter

The community here (and on Linux in general) seems to have mostly focussed on key event interception via xdg-desktop-portal, mostly pushed by TTWNO.

Things to look at maybe:
- https://mail.gnome.org/archives/orca-list/

### Slint

A linux distro for blind users.

https://slint.fr/

From a quick scan it mostly looked like people have stuck with X11.

### AT-SPI

Accessibility protocol for Linux.

https://gitlab.gnome.org/GNOME/at-spi2-core

Appears to have quite a small number of contributors and intested parties, maybe 6 or so.

- https://gnome.pages.gitlab.gnome.org/at-spi2-core/devel-docs/new-protocol.html#project-plan
  https://gitlab.gnome.org/GNOME/at-spi2-core/-/issues/143
  Added 2023-09-09. Discussion in 2023-10-30. Matt Campbell from AccessKit pushing a new a11y protocol for Linux. Not sure whether to base on Wayland or DBus, but has a preference for Wayland.

  Neither he nor Federico (an AT-SPI maintainer) know much about Wayland currently.
- https://bugzilla.gnome.org/show_bug.cgi?id=709999#c5 - A description of how ponytail implemented absolute mouse position clicking in a Wayland security compatible fashion.

### Linux Foundation

Peak body for Linux in general.

https://wiki.linuxfoundation.org/accessibility/start links to a11y.org, but that has been unresponsive over a more than 2 week period.

### People

Individuals who seem to be particularly active in the a11y space.

- Tait Hoyem (TTWNO) - Getting paid to work on input grabbing Wayland protocol - https://gitlab.freedesktop.org/wayland/wayland-protocols/-/issues/149
- AT-SPI2 folks https://gnome.pages.gitlab.gnome.org/at-spi2-core/devel-docs/meeting-2023-01-13.html
- Emmanuele Bassi - Seemed to be the key accessibility guy at GTK/GNOME previously. Was employed by GNOME foundation (at least in 2020), and now works for https://www.igalia.com/ (he may have been hired by GNOME as a contractor in 2020 though as well)
- Samuel Thibault - Involved in Wayland, a11y, GTK, GNOME, Debian, and Orca
- Joanmarie Diggs - Main Orca dev
- David Edmundson - Somebody heavily involved in KWin and QT dev in the Wayland world. http://blog.davidedmundson.co.uk/blog/new-ideas-using-wayland-input-methods/
- Matt Campbell - Main AccessKit dev, is doing some recent (2023-10-30) thinking about a next generation AT-SPI like API.
