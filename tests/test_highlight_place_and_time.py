import pytest

from message_parser import highlight_place_and_time


@pytest.mark.parametrize("message, expected", [
    ('Meet me at the bank at 5 p.m. today, thanks bye', 'Meet me at the bank _at 5 p.m. today_, thanks bye'),
    ("Let's get together in the park at 7 tonight", "Let's get together in the park _at 7 tonight_"),
    ('I want to see you at 7', 'I want to see you _at 7_'),
    ("I'll see you in the park tonight.", "I'll see you in the park _tonight_."),
    ("I'll see you around noon.", "I'll see you _around noon_."),
    ("Let's meet today at 8.", "Let's meet _today at 8_."),
    ("Let's meet today at 12:30 p.m.", "Let's meet _today at 12:30 p.m._"),
    ("Let's meet today at 12:30 AM.", "Let's meet _today at 12:30 AM_."),
    ("Great, I'll be there in 10 minutes.", "Great, I'll be there _in 10 minutes_."),
    ("How about next weekend?", "How about _next weekend_?"),
    ("Let's get together at 10 tonight", "Let's get together _at 10 tonight_"),
    ("Be there around 7 am", "Be there _around 7 am_"),
    ("See you next month", "See you _next month_"),
    ("In 10 minutes I'll be there", "_In 10 minutes_ I'll be there"),
    ("The eclipse is one year from now", "The eclipse is _one year from now_"),
    ("How about SoKno tomorrow at 7.", "How about SoKno _tomorrow at 7_."),
    ("How about SoKno tomorrow     at      7.", "How about SoKno _tomorrow     at      7_."),
    ("Great, I'll be there in          10          minutes.", "Great, I'll be there _in          10          minutes_."),
    ("Be there soon", "Be there _soon_"),
    ("Be there as soon as 10 pm", "Be there _as soon as 10 pm_"),
    ("I'll be there tomorrow between 10 and 2 pm", "I'll be there _tomorrow between 10 and 2 pm_"),
    ("See you around 4 or 5 tonight", "See you _around 4 or 5 tonight_"),
])
def test_highlight_place_and_time(message, expected):
    assert highlight_place_and_time(message) == expected
