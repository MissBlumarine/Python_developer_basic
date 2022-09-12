
import configparser

DEMO_CONFIG_FILE = "demo_config.ini"

def demo_config():
    config = configparser.ConfigParser()
    config.read(DEMO_CONFIG_FILE)

    # print(config)
    # print(config.sections())
    # print(config["DEFAULT"])
    # print(dict(config["DEFAULT"].items()))
    print("environ:", config["DEFAULT"].get("environ"))
    print("foobar:", config["DEFAULT"].get("foobar"))

    port = config["mysql"].getint("port")   #чтобы получить int
    print("port:", port, type(port))

    port += 1
    print(port)

    'как изменить порт на +1 в файле ini'

    config["mysql"]["port"] = str(port)
    config["files"]["home"] = "home/svetlana"

    'Записываем новые переменные в demo_config.ini'

    with open(DEMO_CONFIG_FILE, "w") as f:
        config.write(f)

def main():
    demo_config()

if __name__ == '__main__':
    main()