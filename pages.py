from datetime import datetime, tzinfo
from text import about_me


def return_page_directory(post_id=None):
    page_directory = {
        'noise-deck-creation': {
            'title': 'Noise: Hacker Extraordinaire -- Deck Creation',
            'text': ['temporary text'],
            'json': 'noise-deck',
            'date': datetime(2016, 1, 23, 12, 36, 0)
        },
#        'personal-evolution-deck-creation': {
#            'title': 'Jinteki: Personal Evolution -- Deck Creation',
#            'text': ['temporary text'],
#            'json': None,
#            'date': datetime(2016, 1, 24, 9, 0, 0)
#        },
        'about': {
            'title': 'About Me',
            'text': about_me,
            'json': None,
            'date': datetime(2016, 2, 1, 9, 0, 0)
        }
    }

    if post_id:
        return page_directory[post_id]
    else:
        return page_directory
