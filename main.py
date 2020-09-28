
from weatherParser.wpConfig import config
from weatherParser.wpDo import get_current


def main():
    cur_weather = get_current(config['curWeather_url'])

    print(cur_weather)


if __name__ == '__main__':
    main()
