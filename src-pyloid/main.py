from pyloid import (
    Pyloid,
    PyloidAPI,
    Bridge,
    TrayEvent,
    is_production,
    get_production_path,
)
import os

app = Pyloid(app_name="Pyloid-App", single_instance=True)

production_path = get_production_path()

if is_production() and production_path:
    app.set_icon(os.path.join(production_path, "icons/icon.png"))
    app.set_tray_icon(os.path.join(production_path, "icons/icon.png"))
else:
    app.set_icon("src-pyloid/icons/icon.png")
    app.set_tray_icon("src-pyloid/icons/icon.png")


############################## Tray ################################
def on_double_click():
    print("Tray icon was double-clicked.")


app.set_tray_actions(
    {
        TrayEvent.DoubleClick: on_double_click,
    }
)
app.set_tray_menu_items(
    [
        {"label": "Show Window", "callback": app.show_and_focus_main_window},
        {"label": "Exit", "callback": app.quit},
    ]
)
####################################################################

############################## Bridge ##############################


class custom(PyloidAPI):
    @Bridge(result=str)
    def create_window(self):
        window = self.app.create_window(
            title="Pyloid Browser-2",
            js_apis=[custom()],
        )

        window.set_size(800, 600)
        window.set_position(0, 0)

        if is_production() and production_path:
            window.set_dev_tools(False)
            window.load_file(os.path.join(production_path, "frontend-dist/index.html"))
        else:
            window.set_dev_tools(True)
            window.load_url("http://localhost:5173")

        window.show()
        window.focus()

        return window.id


####################################################################


if is_production() and production_path:
    # production
    window = app.create_window(
        title="Pyloid Browser-production",
        js_apis=[custom()],
        dev_tools=True,
    )
    window.load_file(os.path.join(production_path, "frontend-dist/index.html"))
else:
    window = app.create_window(
        title="Pyloid Browser-dev",
        js_apis=[custom()],
        dev_tools=True,
    )
    window.load_url("http://localhost:5173")

window.show_and_focus()

app.run()  # run
