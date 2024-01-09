from aiogram.dispatcher.filters.state import StatesGroup, State

class EssayState(StatesGroup):
    essay_title = State()
    essay_body = State()

class IELTSResultState(StatesGroup):
    data = State()