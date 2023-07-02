from fastapi import APIRouter

main_router = APIRouter()


@main_router.get('/')
async def site_root():
    """root"""
    return {"message": "Hello, World!"}
