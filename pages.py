from datetime import datetime, tzinfo


def return_page_directory(post_id=None):
    page_directory = {
        'noise-deck-creation': {
            'title': 'Noise: Hacker Extraordinaire (Deck Creation)',
            'scatter-json': 'noise-deck',
            'bar-json': 'noise-counts',
            'date': datetime(2016, 2, 15, 12, 0, 0),
            'page': 'post.html',
            'static': 'static/noise-deck-creation.html'
        },
        'about': {
            'title': 'About Me',
            'scatter-json': None,
            'bar-json': None,
            'date': datetime(2016, 2, 1, 9, 0, 0),
            'page': 'about.html'
        },
        'index': {
            'title': None,
            'scatter-json': None,
            'bar-json': None,
            'date': datetime(2016, 2, 1, 9, 0, 0),
            'page': 'index.html'
        },
        'creating-average-decks': {
            'title': 'Netdecking, or the Perfectly Average Deck Project',
            'scatter-json': None,
            'bar-json': None,
            'date': datetime(2016, 2, 15, 14, 56, 0),
            'page': 'post.html',
            'static': 'static/creating-average-decks.html'
        }
    }

    if post_id:
        return page_directory[post_id]
    else:
        return page_directory
