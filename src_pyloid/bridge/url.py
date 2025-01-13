from pyloid import (
    PyloidAPI,
    Bridge,
    get_production_path,
)
import os


class URL(PyloidAPI):
    @Bridge(result=str)
    def get_production_path(self):
        return str(os.path.join(get_production_path(), "frontend-dist"))
