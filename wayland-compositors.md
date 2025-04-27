# Wayland Compositors

Wayland compositors are desktop environments responsible for managing application windows and routing input events. They implement the core Wayland protocol and potentially a number of protocol extensions.

This page describes the Wayland tech stack a bit and lists out known compositors.

## Wayland theory

Wayland is an extensible client server system using a unix domain socket as its transport. The clients are different applications and the server is the compositor that draws the windows.

Wayland has a a small core protocol and large number of extension protocols for additional functionality. All protocols use the same [wire format](https://wayland.freedesktop.org/docs/html/ch04.html) and are documented as XML, [this website](https://wayland.app/protocols/) aggregates the key XML documents into a nice UI.

A Wayland compositor can be nested so that it is a client to its parent compositor and also a server to the applications it's managing. This is used by login managers like GDM. In this case GDM is a parent compositor that starts up a child compositor like GNOME's Mutter which in turn manages the user's actual applications.

A goal of the move to Wayland was to increase isolation between applications for security reasons. This is partially enabled by the unix sockets, an application gets a unique identity corresponding to its connection to the socket. The other part is just considering the goal of isolation by default when setting up new protocols.

There was a bit of work around authorising access to Wayland protcols around 2014. The [wayland security module](https://github.com/mupuf/libwsm) library was implemented as a policy engine, but hasn't been worked on since or adopted by compositors. More recently (late 2021) people have been discussing [how to identify applications](https://gitlab.freedesktop.org/wlroots/wlroots/-/issues/3339) for the purpose of doing authorisation checks.

## Known compositors

The following (mostly taken from the [Arch Linux wiki](https://wiki.archlinux.org/title/Wayland)) are the compositors I know about. While there are a lot, many share a few common base libraries. I believe this means they implement the same Wayland protocols and would also work with the same XDG Desktop Portal implementations.

I've grouped them below underneath the library they use:

- Mutter: GNOME, Gala
- KWin: KDE, Polonium
- wlroots: Sway, Hyprland, Hikari, labwc, wayfire, wio, phoc, kiwmi, cage, vivarium, swayfx, river, qtile, newm-atha, japokwm, dwl, cagebreak, treeland
- Smithay: Cosmic, Niri
- Weston
- Enlightenment
- Liri
- Velox
- Jay
- Mir (apparently no longer used by Ubuntu)
