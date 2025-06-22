This repository contains notes on the accessibility (a11y) landscape of the Linux desktop. In particular GUI desktops based on the Wayland protocol.

The objective of these notes is to determine what could be done to improve the situation for users of assistive technologies (ATs) like screen readers, voice control, and GUI test automation tools.

# Infrastructure technologies

First a summary of the key infrastructure technologies involved in a Wayland based desktop Linux environment from an a11y perspective:

- [Wayland compositors](wayland-compositors.md) - Software implementing a subset of the Wayland suite of protocols. E.g. GNOME (Mutter), KDE (KWin), Sway. Protocol transport is a unix socket.
- GUI toolkits (e.g. GTK, Qt) - Used to draw buttons/textareas etc., handle within-window focus and input events.
- [XDG Desktop Portal](xdg-desktop-portal.md) - Protocols which provide some generic desktop APIs, e.g. to open a desktop native file chooser dialog, or to take a screenshot. Protocol transport is [DBus](dbus.md).
- [AT-SPI2](https://gitlab.gnome.org/GNOME/at-spi2-core) - Protocols implemented by GUI toolkits that allow ATs to monitor and update the state of controls (e.g. to read from or select some text in a text box). Protocol transport is [DBus](dbus.md).

There is potential overlap between the compositors, XDG Desktop Portals, and other DBus specs. Wayland protocols can isolate apps from one another, but don't currently have a solution for app-specific access controls. DBus specs on the user's session bus don't have any authorisation controls. Portals were originally designed to selectively give more permissions to sandboxed apps (e.g. Flatpak). They have the capability to implement access control policies. Portals may be implemented via Wayland protocols, regular DBus specs, or other methods.

## Narrative overview

This section describes the context around the technologies in a bit more detail. GUI applications (e.g. web browsers, text editors) are written using UI toolkits (e.g. GTK, Qt). They are started, stopped, and displayed by Desktop Environments (e.g. GNOME, Sway).

10 or so years ago almost all Desktop Environments relied on the same display server software called 'X.org' (aka X). This provided a fairly uniform way of handling keyboard/mouse input and managing application windows (including their position, sise, title, and owning process). The content of those application windows (e.g. buttons and text boxes) was not the domain of X, and was not handled in a uniform way.

More recently the 'X.org' display server is being phased out in favour of a wider variety of display servers (called 'compositors') based around the Wayland protocol. The benefit of this move is a lower total maintenance cost for the Linux desktop developer community through simpler codebases, and a more secure protocol architecture where unrelated applications are not able to arbitrarily monitor and interract with one another. A disadvantage is a more fragmented ecosystem where each compositor is its own codebase. Coordination of features must be achieved through agreement around protocol extensions and independent implementations in code.

In the X world we had a standard API for querying and manipulating application windows, but not their content (buttons, textboxes etc.). In the early 2000s the AT-SPI protocol emerged to fill this gap, later updated to AT-SPI2. These protocols would be implemented by various applications and this would allow them to be queried and controlled by ATs like screen readers. In practice the protocols are implemented by the graphical toolkits like GTK and Qt which applications use for drawing the contents of their windows.

Later on the Linux world began to start using containerised/sandboxed desktop applications via Flatpak (and Docker and Snap). This was an opportunity to revisit the security principals covering GUI applications. In short the idea was to limit the access of Flatpak applications rather than giving them full access to all the user's data and capabilities. Like in Android, applications would be able to issue an API call like 'get location' and this might be denied by policy or present the user with a confirmation prompt. In Linux the protocols that describe the available APIs are called 'Portals', and the full collection has the name 'XDG Desktop Portals'. As with the Wayland and AT-SPI2 protocols, there are multiple independent implementations. In the Wayland world the implementations tend to be supplied by the Wayland compositors.

# Key communities

After systematically going through the public fora of a number of [communities](communities.md), it seems like the Linux a11y space is chronically underresourced. I'd guess that at any time over the last 10 years you would have had < 10 programmers in the entire world spending any significant time on it, and at most 2 people full time (most often 0).

The Linux a11y development activity in recent years seems to be centered around the Orca screenreader and attempting to maintain its functionality in the transition to Wayland based desktops. The most active communities are the Orca users and dev(s) and a few people working under the GNOME/GTK/AT-SPI2 banners. The developer of the AccessKit library is putting some work into the Linux infrastructure ecosystem as well (see [here](https://blogs.gnome.org/a11y/2024/06/18/update-on-newton-the-wayland-native-accessibility-project/) and [here](https://blogs.gnome.org/tbernard/2025/04/11/gnome-stf-2024/#newton)).

The most relevant recent discussions I've found (that also indicate key people) are:

- [AT-SPI working group discussion](https://gnome.pages.gitlab.gnome.org/at-spi2-core/devel-docs/meeting-2023-01-13.html) that discusses the state of AT-SPI and recent work for Orca.
- [Design proposal for a next generation AT-SPI API](https://gitlab.gnome.org/GNOME/at-spi2-core/-/issues/143). There is a [prototype of this currently implemented](https://blogs.gnome.org/tbernard/2025/04/11/gnome-stf-2024/#newton).
- [Key capture Wayland protocol for Orca](https://gitlab.freedesktop.org/wayland/wayland-protocols/-/issues/149) and a [continuation on the XDG Desktop Portal repo](https://github.com/flatpak/xdg-desktop-portal/issues/1046) . GNOME has a [DE specific procotol](https://gitlab.gnome.org/GNOME/at-spi2-core/-/merge_requests/178) implemented (as of 2025-04-01).
- [Notes from new Fedora accessibility group meeting](https://discussion.fedoraproject.org/t/2023-10-03-accessibility-working-group-meeting-recap/91647/3) seems like it's just getting stood up.
- [KDE dev on Wayland a11y](https://discuss.kde.org/t/questions-about-ui-automation-on-kwin-wayland/1778/10) - learn the tech and get involved to improve the situation.

# AT Technologies

The following software is using or I think would be interested in using the above Infrastructure technologies:

- [Orca](https://help.gnome.org/users/orca/stable/index.html.en) - Main screenreader used by vision impaired users using Linux.
- [Odilia](https://odilia.app/) - Another newer screen reader for Linux.
- [Talon](https://talonvoice.com/) - Cross platform voice, noise and eye tracker interface and API to control computer desktops. Primarily used by people for whom keyboards and mice are painful or cumbersome to use.
- [Dogtail](https://gitlab.com/dogtail/dogtail) - A UI test automation library for Linux.
- [ydotool](https://github.com/ReimuNotMoe/ydotool) - CLI for controlling the keyboard, and mouse. xdotool (its namesake) could also query and control X windows.
- [warpd](https://github.com/rvaiya/warpd) - Keyboard driven mouse control.

In addition to these there's also the EmacSpeak community, an Emacs plugin for vision impaired users. This is more like it's own embedded mini-OS and so doesn't rely on the above AT infrastructure.

# AT requirements

I've put together a page listing the [features required by the Talon AT](talon-requirements.md) along with their current level of support.
