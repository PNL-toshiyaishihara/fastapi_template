from base import create_app

from .endpoints import (
    main_router
)

app = create_app()
app.include_router(main_router)
