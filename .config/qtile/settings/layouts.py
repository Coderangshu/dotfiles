from libqtile import layout
from libqtile.config import Match
from settings.theme import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 2
}

layouts = [layout.Bsp(**layout_conf),
           layout.MonadTall(**layout_conf),
           layout.RatioTile(**layout_conf),
           layout.Max(),
        #    layout.MonadWide(**layout_conf),
        #    layout.Matrix(columns=2, **layout_conf),
        #    layout.Columns(),
        #    layout.Tile(),
        #    layout.TreeTab(),
        #    layout.VerticalTile(),
        #    layout.Zoomy(),
        ]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),
    ],
    border_focus=colors["color4"][0]
)
