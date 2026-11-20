# Move the Ubuntu Dock "Show Applications" Button

Move the 9-dot "Show Applications" button to the start or end of the Ubuntu Dock with one `gsettings` command.

**Tested on:** Ubuntu 24.04 LTS (GNOME, Ubuntu Dock)

## Steps

Ubuntu Dock is built on the Dash to Dock extension, so the setting lives under its schema. Run these as your normal user, not with `sudo`; the change applies immediately.

Move the button to the **top** (vertical dock) or **left** (horizontal dock):

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock show-apps-at-top true
```

Move it back to the **bottom** or **right** (the default):

```bash
gsettings set org.gnome.shell.extensions.dash-to-dock show-apps-at-top false
```

## Check it worked

```bash
gsettings get org.gnome.shell.extensions.dash-to-dock show-apps-at-top
```

`true` means the button is at the top or left; `false` means bottom or right.

## Related guides

- [KDE Plasma Wayland Shortcuts Cheat Sheet](kde-plasma-wayland-shortcuts-cheat-sheet.md)
