from decimal import Decimal
from typing import Literal

from fluent_compiler.types import FluentType
from typing_extensions import TypeAlias

PossibleValue: TypeAlias = str | int | float | Decimal | bool | FluentType

class TranslatorRunner:
    def get(self, path: str, **kwargs: PossibleValue) -> str: ...
    command: Command
    card: Card
    lang: Lang

class Command:
    @staticmethod
    def start_message(*, body: PossibleValue, intro: PossibleValue) -> Literal["""{ $intro }


{ $body }"""]: ...

class Card:
    @staticmethod
    def greeting(*, username: PossibleValue) -> Literal["""Hello, { $username } 👋"""]: ...
    @staticmethod
    def body(*, projects_count: PossibleValue, updated_at: PossibleValue, years_exp: PossibleValue) -> Literal["""Ivan Ivanov — Backend Developer
I build reliable Python applications.


About
• Built systems, tested tests.
• Experience: { $years_exp } years


Skills
• Python · FastAPI · AsyncIO
• PostgreSQL · Redis · RabbitMQ
• Docker · GitHub Actions · Very smart


Projects ({ $projects_count } projects)
• MyApp — my application
• MyApp — my application
• MyApp — my application


Contacts / Links
• Email: ivan.ivanov@example.com
• Telegram: @ivan_visit
• Website: https://ivan-visit.dev
• GitHub: github.com/ivan-visit


Meta
• Preferred contact: any channel
• Availability:
    availability on request
• Updated: { $updated_at }"""]: ...

class Lang:
    @staticmethod
    def ru() -> Literal["""Русский 🇷🇺"""]: ...
    @staticmethod
    def en() -> Literal["""English 🇬🇧"""]: ...
