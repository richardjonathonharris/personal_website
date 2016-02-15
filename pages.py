from datetime import datetime, tzinfo


def return_page_directory(post_id=None):
    page_directory = {
        'noise-deck-creation': {
            'title': 'Noise!',
            'scatter-json': 'noise-deck',
            'date': datetime(2016, 1, 23, 12, 36, 0),
            'page': 'post.html'
        },
        'about': {
            'title': 'About Me',
            'scatter-json': None,
            'date': datetime(2016, 2, 1, 9, 0, 0),
            'page': 'about.html'
        },
        'index': {
            'title': None,
            'scatter-json': None,
            'date': datetime(2016, 2, 1, 9, 0, 0),
            'page': 'index.html'
        }
    }

    if post_id:
        return page_directory[post_id]
    else:
        return page_directory
