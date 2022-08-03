import habr

KEY_WORDS = ['дизайн', 'фото', 'web', 'python']

if __name__ == '__main__':
    item = habr.Habr()
    print('Поиск по всей доступной preview-информации:')

    # Поиск по ключевым словам в превью статьи
    item.preview_info(KEY_WORDS)
    print('\n')
    print('Поиск целиком по всей статье:')

    # Поиск по ключевым словам в основном тексте статьи
    item.article_text(KEY_WORDS)
