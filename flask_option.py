import os

def start():
    """returns the right message"""
    env = os.getenv('FLASK_ENV')

    if env == 'development':
        return "Starting in development mode..."

    # Pylint kuralı: Yukarıda return olduğu için 'elif' yerine düz 'if' kullanıyoruz.
    if env == 'production':
        return "Starting in production mode..."

    # else kullanmaya gerek yok, yukarıdakilere girmezse burası çalışır.
    return "Starting in empty mode..."

if __name__ == "__main__":
    print(start())
    