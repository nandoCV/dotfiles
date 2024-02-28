#!/bin/python3

from cgitb import text
import subprocess
from time import time
import os
import functools
import shortuuid

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

home = os.path.expanduser('~')
capturePath = os.path.join(home, 'Screenshots')
if not os.path.isdir(capturePath):
    os.mkdir(capturePath)
filename = str(shortuuid.uuid(str(int(time()))))

keys = [
    # ------------ Window Configs ------------

    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    Key([mod, "shift"], "l", lazy.layout.grow()),
    Key([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    Key([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    Key([mod, "mod1"], "r", lazy.restart()),

    Key([mod, "mod1"], "q", lazy.shutdown()),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Rofi
    Key([mod], "m", lazy.spawn(f"rofi -show drun")),
    Key([mod], "r", lazy.spawncmd()),

     # File Explorer
    Key([mod], "e", lazy.spawn("nautilus")),

    # Audio key keybindings
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    #Screenshots
    Key([mod], "s", lazy.spawn("scrot -s -F "+ capturePath+"/"+ filename+".png")),
]

def init_group_names():
    """
    Returns a list of group names.
    """
    return [
        ('1'+'\uf111', {'layout': 'monadtall'}),        # Firefox 
        ('2'+'\uf111', {'layout': 'monadtall'}),        # GitHub
        ('3'+'\uf111', {'layout': 'monadtall'}),        # Code
        ('4'+'\uf111', {'layout': 'monadtall'}),        # Terminal
        ('5'+'\uf111', {'layout': 'monadtall'}),        # StackOverflow
        ('6'+'\uf111', {'layout': 'monadtall'}),        # YouTube
        ('7'+'\uf111', {'layout': 'monadtall'}),        # Chat
        ('8'+'\uf111', {'layout': 'monadtall'})         # Music
    ]

def init_groups():
    """
    Returns a list of groups.
    """
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ['config', '__main__']:
    group_names = init_group_names()
    groups = init_groups()

    for i, (name, kwargs) in enumerate(group_names, 1):
        keys.append(Key([mod], str(i), lazy.group[name].toscreen()))         # Switch to another group
        keys.append(Key([mod, 'shift'], str(i), lazy.window.togroup(name)))  # Send current window to another group

# def create_icon():
#     """
#     Returns an icon to be used in text elements of Qtile.
#     """
#     textbox = widget.TextBox(**widget_defaults)
#     textbox.font = "Font Awesome 6 Free Solid"
#     return textbox

hybrid = {
    "background": "000000",
    "foreground": "ffffff",
    "black":      "393939",
    "red":        "da4939",
    "green":      "9acc79",
    "yellow":     "d0d26b",
    "blue":       "6d9cbe",
    "magenta":    "9f5079",
    "cyan":       "435d75",
    "white":      "c2c2c2"

    # "black":      "474747",
    # "red":        "ff6c5c",
    # "green":      "8fb676",
    # "yellow":     "c8bc45",
    # "blue":       "d0d0ff",
    # "magenta":    "a761c2",
    # "cyan":       "6e98a4",
    # "white":      "c2c2c2"
}

monokai = {
    "background": "272822",
    "foreground": "f1ebeb",
    "black":      "48483e",
    "red":        "dc2566",
    "green":      "8fc029",
    "yellow":     "d4c96e",
    "blue":       "55bcce",
    "magenta":    "9358fe",
    "cyan":       "56b7a5",
    "white":      "acada1"
}

tomorrow = {
    "background": "1d1f21",
    "foreground": "c5c8c6",
    "black":      "969896",
    "red":        "cc6666",
    "green":      "b5bd68",
    "yellow":     "f0c674",
    "blue":       "81a2be",
    "magenta":    "b294bb",
    "cyan":       "8abeb7",
    "white":      "c5c8c6"
}

one_dark = {
    "background": "1e2127",
    "foreground": "dee2e3",
    "black":      "5c6370",
    "red":        "e06c75",
    "green":      "98c379",
    "yellow":     "d19a66",
    "blue":       "61afef",
    "magenta":    "c678dd",
    "cyan":       "56b6c2",
    "white":      "828791"
}

theme = hybrid
accent_color = theme["cyan"]

layout_defaults = {
    "border_width": 2,
    "border_focus": accent_color,
"border_normal": theme["black"],
}

layouts = [
    layout.MonadTall(**layout_defaults),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    layout.Bsp(),
    layout.Matrix(),
    # layout.Tile(),
    # layout.TreeTab(),
    layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Ubuntu Nerd Font",
    fontsize=12,#14
    padding=6,
)
extension_defaults = widget_defaults.copy()

left_arrow = lambda background, foreground: widget.TextBox(
    font="Hack Nerd Font",
    text="\uf438",
    fontsize=60,
    background=background,
    foreground=foreground,
    padding=-8,
)

icon = lambda char, foreground, background: widget.TextBox(
    font="Font Awesome 6 Free Solid",
    text=char,
    background=background,
    foreground=foreground,
)

separator = lambda color: widget.Sep(
    background=color,
    foreground=color,
)

separator_background_color = functools.partial(separator, color=theme["background"])

screens = [
    Screen(
        top=bar.Bar(
            [
                # ------

                # #widget.CurrentLayout(),
                # widget.GroupBox(
                #     font="Font Awesome 6 Free Solid",
                #     highlight_method="text",
                #     this_current_screen_border=theme["magenta"],
                #     #this_other_screen_border=theme["blue"],
                #     #highlight_color=theme["magenta"],
                #     inactive=theme["black"],
                #     borderwidth=2,
                #     rounded=False,
                #     padding=3,
                #     margin=3
                # ),

                # icon("\uf248", foreground=theme["background"], background=theme["blue"]),
                widget.CurrentLayoutIcon(
                    fontsize=9,
                    background=theme["blue"],
                    foreground=theme["background"],

                ),
                widget.CurrentLayout(
                     background=theme["blue"],
                     foreground=theme["background"]
                ),
                separator(color=theme["blue"]),
                widget.GroupBox(
                    font="Font Awesome 6 Free Solid",
                    foreground=theme["foreground"],
                    highlight_method="line",
                    highlight_color=theme['white'],
                    urgent_alert_method='line',
                    hide_unused=True,
                    # this_current_screen_border=accent_color,
                    # this_other_screen_border=theme["blue"],
                    this_current_screen=theme["green"],
                    inactive=theme["background"],
                    active=accent_color,
                    urgent_border=theme["red"],
                    borderwidth=1,
                    rounded=False,
                    padding_x=10,
                    padding_y=8,
                    margin_x=0

                    #margin=0
                ),

                # ------

                separator(color=theme["background"]),
                widget.WindowName(),

                # ------

                # left_arrow(background=theme["background"], foreground=theme["red"]),
                # widget.Systray(
                #     fontsize=12,
                #     background=theme["red"],
                # ),
                # separator(color=theme["red"]),
                # left_arrow(background=theme["red"], foreground=theme["green"]),

                widget.Systray(
                    fontsize=12,
                    background=theme["background"],
                ),
                separator(theme["background"]),

                # -----
                widget.Prompt(
                    fontsize=14, 
                    padding=5, 
                    prompt="  ",
                    cursor= True,
                    background=theme["background"],
                    foreground=theme["green"]
                    ),

                icon("\uf1eb", background=theme["background"], foreground=theme["red"]),
                widget.Net(
                        format="{down} ↓↑{up}",
                        foreground=theme["red"],
                ),

                # ------

                # icon("\uf538", background=theme["green"], foreground=theme["background"]),
                # widget.Memory(
                #     measure_mem="G",
                #     format="{MemUsed:.1f}/{MemTotal:.1f} GiB",
                #     background=theme["green"],
                #     foreground=theme["background"]
                # ),
                # separator(color=theme["green"]),
                # left_arrow(background=theme["green"], foreground=theme["yellow"]),

                separator(color=theme["background"]),
                icon("\uf538", background=theme["background"], foreground=theme["green"]),
                widget.Memory(
                    measure_mem="G",
                    format="{MemUsed:.1f}/{MemTotal:.1f} GiB",
                    background=theme["background"],
                    foreground=theme["green"]
                ),
                separator(color=theme["background"]),

                # ------

                # icon("\uf2db", background=theme["yellow"], foreground=theme["background"]),
                # widget.CPU(
                #     format="{load_percent:.1f}%",
                #     background=theme["yellow"],
                #     foreground=theme["background"]
                # ),
                # separator(color=theme["yellow"]),
                # left_arrow(background=theme["yellow"], foreground=theme["blue"]),

                icon("\uf2db", background=theme["background"], foreground=theme["yellow"]),
                widget.CPU(
                    format="{load_percent:.1f}%",
                    background=theme["background"],
                    foreground=theme["yellow"]
                ),
                separator(color=theme["background"]),


                # ------

                # icon("\uf248", foreground=theme["background"], background=theme["blue"]),
                # widget.CurrentLayout(
                #     background=theme["blue"],
                #     foreground=theme["background"]
                # ),
                # separator(color=theme["blue"]),
                icon("\uf028", foreground=theme["red"], background=theme["background"]),
                widget.Volume(
                        background=theme['background'],
                        foreground=theme['red']
                        ),

                widget.Battery(
                    format="{char} {percent:2.0%}",
                    background=theme["background"],
                    foreground=theme["yellow"],
                    update_interval=20,
                    notify_below=10,
                    charge_char="\uf0e7", # icono cargando
                    discharge_char="\uf241 ", # icono desconectado
                    empty_char="\uf243 ", # icono bateria baja
                    full_char="\uf240"
                ),
                separator(color=theme["background"]),

                icon("\uf248", foreground=theme["blue"], background=theme["background"]),
                widget.CurrentLayout(
                    background=theme["background"],
                    foreground=theme["blue"]
                ),
                separator(color=theme["background"]),

                # ------

                icon("\uf021", foreground=theme["magenta"], background=theme["background"]),
                widget.CheckUpdates(
                    distro="Arch",
                    no_update_string="Up To Date",
                    colour_no_updates=theme["magenta"],
                    colour_have_updates=theme["red"],
                    background=theme["background"],
                    foreground=theme["magenta"],
                    update_interval="60"
                ),
                separator(color=theme["background"]),

                # ------

                # left_arrow(background=theme["black"], foreground=theme["magenta"]),
                # #separator(color=theme["magenta"]),
                # icon("\uf017", foreground=theme["background"], background=theme["magenta"]),
                # widget.Clock(
                #     format="%B %-d, %R",
                #     background=theme["magenta"],
                #     foreground=theme["background"],
                # ),
                # separator(color=theme["magenta"]),

                icon("\uf017", foreground=theme["cyan"], background=theme["background"]),
                widget.Clock(
                    format="%B %-d, %R",
                    background=theme["background"],
                    foreground=theme["cyan"],
                ),
                separator(color=theme["background"]),
                widget.KeyboardLayout(
                        configured_keyboards=['latam', 'en']
                        )
            ],
            28,
            background=theme["background"],
            opacity=0.8
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

secondary_widgets = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    font="Font Awesome 6 Free Solid",
                    foreground=theme["foreground"],
                    highlight_method="line",
                    urgent_alert_method='block',
                    hide_unused=True,
                    this_current_screen_border=accent_color,
                    this_other_screen_border=theme["blue"],
                    this_current_screen=theme["background"],
                    block_highlight_text_color=theme["background"],
                    inactive=theme["background"],
                    active=accent_color,
                    urgent_border=theme["red"],
                    borderwidth=1,
                    rounded=False,
                    padding_x=10,
                    padding_y=8,
                    margin_x=0

                    #margin=0
                ),
                separator(color=theme["background"]),
                widget.WindowName(),
            ],
            28,
            background=theme["background"]
        )
    )
]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"
command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(secondary_widgets)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)



auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = ["feh --bg-fill --randomize ~/.wallpapers/*"]

for x in autostart:
    os.system(x)
