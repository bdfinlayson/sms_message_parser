import re
import sys


def highlight_place_and_time(message):
    time_words = 'weekend|noon|tonight|tomorrow|evening|night|morning|afternoon|week|month|today|year|minutes|seconds|hours|days|weeks|months|years|soon'
    place_prepositions = 'at|on|around|in|next|the|this|that|on the|in the|from now|until|as early as|as soon as|between|and|or'
    number_words = 'one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve'
    numerical_time = '(\d+)(:\d+)?'
    am_pm = 'p\.m\.|a\.m\.|P\.M\.|A\.M\.|am|pm|AM|PM'
    generic_pattern = r'\w.?\s+?\d.?\w?\.?\w?\.?\s?\w*'

    # build the time regex
    time_pattern = fr'((({place_prepositions}) ({numerical_time}) ({place_prepositions}) ({numerical_time}) ({time_words})|({time_words}) ({place_prepositions}) ({numerical_time}) ({place_prepositions}) ({numerical_time}) ({am_pm})|({place_prepositions}) ({numerical_time}) ({time_words})|({time_words}) ({place_prepositions}) ({numerical_time}) ({am_pm})|({place_prepositions}) ({numerical_time}) ({am_pm}) ({time_words})?|({number_words}) ({time_words}) ({place_prepositions})|({place_prepositions}) ({time_words}))|({time_words}) ({place_prepositions})? ({numerical_time})?|(({place_prepositions})? {time_words} (({place_prepositions})? ({numerical_time})? ({am_pm})?))|({generic_pattern}))'

    # ensure it can match despite extra whitespace
    time_pattern = time_pattern.replace(" ", r"(\s+)?")

    # highlight time segment
    message = re.sub(time_pattern, r'_\1_', message)

    # then try to highlight place
    # look-benhind worked well but re doesn't allow non-fixed width look-behinds: ((?<=the|about) (\w+) (?=_))|((?<=_ (^at|the|at the)) (\w+))
    # so try a lesser work around
    prepositions = '^about|the|in|on|at|about|around|among|inside|outside|beside|next to'
    place_pattern = fr'(?:{prepositions}) ([^{prepositions}]\w+) (?:(?:.*)?_.*_)|(?:_.*_ (?:.*)?) (?:{prepositions}) ([^{prepositions}]\w+)'

    search_result = re.search(place_pattern, message)
    if search_result:
        match = search_result.groups()[0]
        message = re.sub(fr'({match})', r'_\1_', message)

    return message


if __name__ == '__main__':
    sms = sys.argv[1]
    result = highlight_place_and_time(sms)
    print(result)
