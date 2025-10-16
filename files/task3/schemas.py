from datetime import date
from enum import Enum
import random

from pydantic import AliasGenerator, BaseModel, ConfigDict, EmailStr, Field, field_validator

from pydantic.alias_generators import to_camel


def generate_username() -> str:
    return f"user_{random.randint(1000, 9999)}"

config = ConfigDict(
    alias_generator=AliasGenerator(serialization_alias=to_camel),
    populate_by_name=True
)


class User(BaseModel):
    title: str = Field(default="Пользователь")
    description: str = Field(default="Модель пользователя")
    id: int
    name: str = Field(min_length=1)
    username: str = Field(default_factory=generate_username)
    age: int = Field(gt=0)
    is_supervisor: bool
    email: EmailStr
    phone_number: str = Field(pattern=r"^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$")

    model_config = config


class DealType(str, Enum):
    purchase = "покупка"
    sale = "продажа"


class Deal(BaseModel):
    title: str = Field(default="Сделка")
    description: str = Field(default="Модель сделки")
    id: int
    title_deal: str
    comment: str
    created_at: date
    persons_in_charge: list[User]
    deal_type: DealType

    model_config = config

    @field_validator("created_at", mode="after")
    def validate_created_at(cls, value):
        if value > date.today():
            raise ValueError("Дата создания не может быть в будущем")
        return value
