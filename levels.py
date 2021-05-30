# Некоторые клавиатурные тренажёры предлагают ряд уроков для изучения раскладки,
# ведут статистику обучения.
"""
В русской раскладке все часто употребляемые символы расположены по центру клавиатуры,
что еще раз подтверждает правильность выбранного мною метода.
Проведя статистический подсчет, я определил, что комбинаций из двух символов,
в основном, немного, около 800, а из них наиболее встречающихся – около ста
(по данным анализа одного текста – 65% от всех символов).
Таким образом, если подобрать примерно около 100 слов,
содержащих все основные комбинации символов, то, набирая их,
можно быстрее научиться скоростному набору текста.
"""
level_0 = {
    's_midl': "asdfghjkl",
    's_low': "zxcvbnm",
    's_upp': "qwertyuiop",
    'all_sim': "asdfghjklzxcvbnmqwertyuiop"
}

level_1 = {
    's_1': "aa ss dd ff jj kk ll ;; as as df df jk jk l; l; as as df df jk jk l; l;",
    's_12': "asdf asdf jkl; jkl; fdsa fdsa ;lkj ;lkj",
    's_midl': "asdfghjkl",
    's_low': "zxcvbnm",
    's_upp': "qwertyuiop",
    'all_sim': "asdfghjklzxcvbnmqwertyuiop"

}
