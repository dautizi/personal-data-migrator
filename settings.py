CONFIGURATION = {
    'version': 1,
    'sourceDB': {
        'type': 'MySQL',
        'host': 'localhost',
        'port': '3306',
        'dbname' : 'daniele_autizi',
        'username': '',
        'password': '',
        'ssh': {
            'host': '',
            'port': '',
            'username': '',
            'password': ''
        },
        'limit': 20
    },
    'destinationDB': {
        'type': 'MongoDB',
        'host': 'localhost',
        'port': 27017,
        'dbname' : 'danieleautizi',
        'username': '',
        'password': '',
        'collections': {
            'adventure': 'adventure',
            'adventure_media': 'adventureMedia',
            'article': 'article',
            'blog': 'blog',
            'image': 'image',
            'skill': 'skill'
        }
    }
}
