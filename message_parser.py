import re
import sys


def highlight_place_and_time(message):
    time_names = 'weekend|noon|tonight|tomorrow|evening|night|morning|afternoon|week|month|today|year|minutes|seconds|hours|days|weeks|months|years|soon'
    place_prepositions = 'at|on|around|in|next|the|this|that|on the|in the|from now|until|as early as|as soon as|between|and|or'
    written_numbers = 'one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve'
    numerical_time = '(\d+)(:\d+)?'
    am_pm = 'p\.m\.|a\.m\.|P\.M\.|A\.M\.|am|pm|AM|PM'
    generic_pattern = r'\w.?\s+?\d.?\w?\.?\w?\.?\s?\w*'
    time_placeholder = 'TIME'

    # build the time regex
    time_pattern = fr'((({place_prepositions}) ({numerical_time}) ({place_prepositions}) ({numerical_time}) ({time_names})|({time_names}) ({place_prepositions}) ({numerical_time}) ({place_prepositions}) ({numerical_time}) ({am_pm})|({place_prepositions}) ({numerical_time}) ({time_names})|({time_names}) ({place_prepositions}) ({numerical_time}) ({am_pm})|({place_prepositions}) ({numerical_time}) ({am_pm}) ({time_names})?|({written_numbers}) ({time_names}) ({place_prepositions})|({place_prepositions}) ({time_names}))|({time_names}) ({place_prepositions})? ({numerical_time})?|(({place_prepositions})? {time_names} (({place_prepositions})? ({numerical_time})? ({am_pm})?))|({generic_pattern}))'

    # ensure it can match despite extra whitespace
    time_pattern = time_pattern.replace(" ", r"(\s+)?")

    # highlight time segment
    message = re.sub(time_pattern, r'_\1_', message)

    return message


if __name__ == '__main__':
    sms = sys.argv[1]
    highlight_place_and_time(sms)
