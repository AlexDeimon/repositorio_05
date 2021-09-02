from fastapi import Depends, FastAPI

from routers.car_router import router as router_car

api = FastAPI()

api.include_router(router_car)