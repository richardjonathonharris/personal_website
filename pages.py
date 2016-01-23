from datetime import datetime, tzinfo

def return_page_directory(post_id=None):
    page_directory = {
        'noise-deck-creation': {
            'title': 'Noise: Hacker Extraordinaire -- Deck Creation',
            'text': 'temporary text',
            'json': '1',
            'date': datetime(2016, 1, 23, 12, 36, 00)
        }
    }
    if post_id:
        return page_directory[post_id]
    else:
        return page_directory
