from .admin import admin
from .contact import edit_contact, add_contact
from .root import get_locale, get_timezone, index, not_found_error, internal_error
from .task import task, task_dashboard, add_task
from .user import register, profile, login, logout
from .offer import offer_dashboard, add_offer, edit_offer