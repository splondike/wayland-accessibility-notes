# DBus

[DBus](https://pythonhosted.org/txdbus/dbus_overview.html) is a inter process communication (IPC) system strongly associated with Linux. Programs connect to a central DBus daemon over a unix socket (or TCP) and send it messages. The daemon routes those messages to individual target processes or to all processes subscribed to an event stream. It can be used by client programs to access desktop functionality like adding a notification, or to communicate with one another (as in the case of AT-SPI).

Processes get a unique identifier when they connect to the bus, but can also register themselves as handlers for well known names. Client programs can then send messages to the well known name for the functionality they want without caring about what program is implementing the handler.

Handlers expose APIs by defining and implementing named interfaces. The interfaces list the RPC methods, read/writeable properties, and events they expose along with the expected argument and return types. DBus also has strong runtime introspection capabilities. These are used by the GUI interface browser [D-Spy](https://gitlab.gnome.org/GNOME/d-spy) for example.

RPC calls can be authorised using [polkit](https://wiki.archlinux.org/title/Polkit) by checking the user or unix group membership of the user.

In a standard Linux desktop there will tend to be two separate DBus daemons, one running as root (called the system bus), and one as the currently logged in user (called the session bus). They will tend to provide interfaces to different functionality. The system bus will also make use of the authorisation capabilities whereas the session bus won't.

Handlers can be lazily loaded; so the daemon would start a handler process (via SystemD I think) when one of its interface methods was first called.

So we might have a process registered to the `org.freedesktop.Notifications` well known name on the session bus that implements an interface called `org.freedesktop.Notifications`. Hopefully it would stick with [the spec](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html#commands) and implement e.g. the `Notify(string app_name, uint32 replaces_id, string app_icon, string summary, ...) -> (uint32 id)` method among others. A process running in the user's session could call that method to display a notification balloon in the appropriate style for the desktop environment.
