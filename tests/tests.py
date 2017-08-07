from headlines import h1, h2, h3, h4


def tmp_test_print_headlines():
    short_txt = 'Lorem ipsum dolor sit amet'
    long_txt = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna'
    long_txt2 = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam'

    print(h1(short_txt))
    print(long_txt2)
    print(h1(long_txt))
    print(long_txt2)
    print(h2(short_txt))
    print(long_txt2)
    print(h2(long_txt))
    print(long_txt2)
    print(h3(short_txt))
    print(long_txt2)
    print(h3(long_txt))
    print(long_txt2)
    print(h4(short_txt))
    print(long_txt2)
    print(h4(long_txt))
    print(long_txt2)


tmp_test_print_headlines()

if __name__ == 'main':
    tmp_test_print_headlines()
