from .app import create_app


# run server
def server():
    if __name__ == '__main__':
        create_app().run()
