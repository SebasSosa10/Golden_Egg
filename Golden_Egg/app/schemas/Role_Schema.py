from pydantic import BaseModel

class RoleBase(BaseModel):
    roleName: str

class RoleCreate(RoleBase):
    pass


class RoleResponse(RoleBase):
    id: int
    class Config:
        orm_mode = True