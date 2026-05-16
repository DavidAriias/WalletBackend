from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.infraestructure.db.base import Base
from src.infraestructure.db.session import engine

from src.presentation.routes.auth_routes import router as auth_router
from src.presentation.routes.payment_method_routes import router as payment_router
from src.presentation.routes.user_routes import router as user_router
from src.presentation.routes.audit_routes import router as audit_router


from src.infraestructure.middleware.audit_context_middleware import AuthContextMiddleware
from src.infraestructure.middleware.audit_flush_middleware import audit_flush_middleware


app = FastAPI(
    title="Secure Wallet API",
    description="API for secure payment method management",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# CORS para Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(audit_flush_middleware)
app.add_middleware(AuthContextMiddleware)

# Registro de rutas
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(payment_router)
app.include_router(audit_router)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="docs")