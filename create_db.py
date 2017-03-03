import argparse
import MySQLdb
import settings


def delete_tables():
    db = MySQLdb.connect(settings.db_host, settings.db_user, settings.db_password, settings.db_name)
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS album_total_views")
    cursor.execute("DROP TABLE IF EXISTS album_stats")
    cursor.execute("DROP TABLE IF EXISTS albums")
    db.close()


def create_tables():
    db = MySQLdb.connect(settings.db_host, settings.db_user, settings.db_password, settings.db_name)
    cursor = db.cursor()

    try:
        sql = """CREATE TABLE albums (
                `id` INT NOT NULL AUTO_INCREMENT,
                `album_name`  CHAR(200) NOT NULL,
                PRIMARY KEY (`id`))"""

        cursor.execute(sql)

        sql = """CREATE TABLE album_stats (
                `id` INT NOT NULL AUTO_INCREMENT,
                `photo_id`  CHAR(64) NOT NULL,
                `views` INT,
                `datetime` DATETIME,
                `album` INT NOT NULL,
                PRIMARY KEY (`id`),
                CONSTRAINT `album_fk_1` FOREIGN KEY (`album`)
                    REFERENCES `albums` (`id`))"""

        cursor.execute(sql)

        sql = """CREATE TABLE album_total_views (
                `id` INT NOT NULL AUTO_INCREMENT,
                `views` INT,
                `datetime` DATETIME,
                `album` INT NOT NULL,
                PRIMARY KEY (`id`),
                CONSTRAINT `album_fk_2` FOREIGN KEY (`album`)
                    REFERENCES `albums` (`id`))"""

        cursor.execute(sql)

    except:
        print 'Error creating tables.'

    db.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--delete', dest='delete', action='store_true', help='Delete existing tables')
    args = parser.parse_args()

    if args.delete:
        delete_tables()

    create_tables()

if __name__ == "__main__":
    main()
