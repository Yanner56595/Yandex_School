from geo_func import get_coords, show_map, get_span


def main():
    toponym = input()
    try:
        lat, lon = get_coords(toponym)
        type_map = 'sat'
        ll = f'{lat},{lon}'
        d = get_span(toponym)
        show_map(ll, type_map, delta=d, point=ll)
    except Exception as e:
        print('Error', e)


if __name__ == '__main__':
    main()