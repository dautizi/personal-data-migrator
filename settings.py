CONFIGURATION = {
    'version': 1,
    'sourceDB': {
        'type': 'MySQL',
        'host': 'localhost',
        'port': '3306',
        'dbname' : '',
        'username': '',
        'password': '',
        'ssh': {
            'host': '',
            'port': 3306,
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
            'education': 'education',
            'image': 'image',
            'skill': 'skill',
            'work_experience': 'workExperience'
        }
    }
}
