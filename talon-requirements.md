# Talon requirements

This page lists the OS features required by the [Talon platform](https://talonvoice.com/). Talon is an Accessibility Technology that allows the user to control their computer via voice, noises, facial expressions, keyboard, or an eye tracker. It provides a cross platform API for window management for user defined scripts, and allows behaviour to vary depending on the focussed application window.

## Feature index

The sections below aim to logically group the features. The items in the list are prefixed with some indicators. First a 2 digit id. Next by 'L', 'M', 'H' for an estimate of low, medium, and high priority. Lastly by the letters G K and W suffixed with +, ^, -, ?. These correspond to whether the feature seems possible, seems possible in a non-optimal way, not currently possible, or unknown under GNOME, KDE, and Wlroots (the top three compositor families). So G+ would say it was available under GNOME, and W? would say unknown under Wlroots.

Generally the 'seems possible' means it's in a stable wayland protocol or desktop portal, most haven't actually been verified to work.

Features for querying and updating the state of arbitrary application windows:

- 01 H G^ K^ W^ Enumerate all windows, whether minimised or visible
- 02 H G^ K- W- Get PID associated with a given window
- 03 H G^ K^ W^ Get window title
- 04 M G^ K- W^ Focus window
- 05 L G^ K^ W^ Close window
- 06 L G^ K- W^ Set window position and size
- 07 L G^ K^ W- Get window position and size
- 08 L G^ K^ W^ Get window minimised/hidden
- 09 L G^ K- W^ Set window minimised/hidden
- 10 L G^ K^ W^ Get window maximised
- 11 L G^ K- W^ Set window maximised
- 12 L G- K^ W- Get window virtual desktop/workspace
- 13 L G^ K^ W- Set window virtual desktop/workspace
- 14 L G- K^ W^ Subscribe to events for window state change (e.g. opened, closed, minimised)

Features for emulating keyboard and mouse devices and responding to state changes:

- 15 H G- K- W- Get absolute mouse position
- 16 H G+ K+ W+ Move mouse to absolute position
- 17 H G+ K+ W+ Emulating press mouse buttons
- 18 H G+ K+ W+ Emulate pressing keyboard keys
- 19 H G+ K+ W+ Get/set clipboard contents without having active window
- 20 M G? K? W? Query which mouse buttons are pressed down currently
- 21 M G- K- W- Register for keyboard shortcuts that change as window focus changes. Ideally edge events sent (key up/down).

Screen capture:

- 22 M G+ K+ W+ Capture the contents of the screen to a readable buffer

Application UI:

- 24 H G^ K? W^ System tray with right click menu support
- 23 M G^ K? W^ Draw transparent 'always on top' overlays on all virtual desktops/workspaces

Audio:

- 25 H G+ K+ W+ Capture audio from any system microphones

Accessibility API:

- 26 L G+ K+ W+ Access to the accessibility API (e.g. AT-SPI) for the current window
- 27 L G? K? W? Correlate DE level window id to accessibility API object id

## Feature details

This section contains more details on the current state of the above features. The subsections use the same feature id as above.

### 01 Enumerate all windows

[Wlroots](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) and [KWin](https://wayland.app/protocols/kde-plasma-window-management) have compositor specific protocols for this.

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 03 Get window title

[Wlroots](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) and [KWin](https://wayland.app/protocols/kde-plasma-window-management) have compositor specific protocols for this.

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 04 Focus window

[Wlroots](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) has a compositor specific protocol for this.

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 05 Close window

[Wlroots](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) and [KWin](https://wayland.app/protocols/kde-plasma-window-management) have compositor specific protocols for this.

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 06 Set window position and sise

Wlroots has a protocol for this: https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1#zwlr_foreign_toplevel_handle_v1:request:set_rectangle

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

Applications are not supposed to be able to set their window position:
https://lists.freedesktop.org/archives/wayland-devel/2022-August/042305.html . But XWayland applications can do so (this is what Talon's canvas window uses).

Potentially ATs could be allowed to manipulate other windows via some API.
There's a recent thread discussing the concept of a [generic desktop automation API](https://lists.freedesktop.org/archives/wayland-devel/2023-November/043247.html) for positioning of windows.

### 07 Get window position and sise

KWin has a protocol for this: https://wayland.app/protocols/kde-plasma-window-management#org_kde_plasma_window:request:set_minimized_geometry

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 08 Get window minimised

[Wlroots](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) and [KWin](https://wayland.app/protocols/kde-plasma-window-management) have compositor specific protocols for this.

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 09 Set window minimised

[Wlroots](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) has a compositor specific protocol for this.

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 10 Get window maximised

[Wlroots](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) and [KWin](https://wayland.app/protocols/kde-plasma-window-management) have compositor specific protocols for this.

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 11 Set window maximised

[Wlroots](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) has a compositor specific protocol for this.

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 12 Get virtual desktop

[KWin](https://wayland.app/protocols/kde-plasma-window-management) has a compositor specific protocol for this.

### 13 Set virtual desktop

[KWin](https://wayland.app/protocols/kde-plasma-window-management) has a compositor specific protocol for this.

The [window-calls](https://github.com/ickyicky/window-calls) GNOME shell extension provides a DBus interface for this.

### 14 Window state change events

[Wlroots](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) and [KWin](https://wayland.app/protocols/kde-plasma-window-management) have compositor specific protocols for this.

### 15 Get absolute mouse position

Sounds like this isn't something that's wanted: https://lists.freedesktop.org/archives/wayland-devel/2022-September/042404.html

### 16 Move mouse to position

Can use the Remote Desktop portal: https://flatpak.github.io/xdg-desktop-portal/docs/#gdbus-org.freedesktop.portal.RemoteDesktop

### 17 Emulate press mouse buttons

Can use the Remote Desktop portal: https://flatpak.github.io/xdg-desktop-portal/docs/#gdbus-org.freedesktop.portal.RemoteDesktop

### 18 Emulate pressing keyboard keys

Can use the Remote Desktop portal: https://flatpak.github.io/xdg-desktop-portal/docs/#gdbus-org.freedesktop.portal.RemoteDesktop

Or use https://gitlab.freedesktop.org/libinput/libei for a general abstraction layer

### 19 Get/set clipboard

Can use clipboard portal: https://flatpak.github.io/xdg-desktop-portal/docs/#gdbus-org.freedesktop.portal.Clipboard

Or can use the wl_data_device_manager in the core Wayland protocol: https://wayland.app/protocols/wayland#wl_data_device_manager

See also https://github.com/bugaevc/wl-clipboard

### 21 Keyboard shortcuts

There is a portal: https://flatpak.github.io/xdg-desktop-portal/docs/#gdbus-org.freedesktop.portal.GlobalShortcuts . But it says you can only bind once per application and it's probably going to present a dialog for the user to change the shortcuts.

There's some ongoing work around making this more dynamic for the Orca use case: https://github.com/flatpak/xdg-desktop-portal/issues/1046

### 22 Screen capture

This is available as a portal: https://flatpak.github.io/xdg-desktop-portal/docs/#gdbus-org.freedesktop.portal.Screenshot

### 23 Draw transparent always on top

This works fine currently because we're using XWayland which lets windows absolutely position themselves. It seems not ideal to be relying on that, but it works OK.

### 24 System tray

The default tray in Sway doesn't support popup menus (not yet implemented). It works using the [waybar](https://github.com/Alexays/Waybar) alternative tray though.

Under GNOME you can activate this extension: https://github.com/ubuntu/gnome-shell-extension-appindicator
